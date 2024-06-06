# RU101 Week 1

[Documentation for Key commands at redis.io](https://redis.io/commands#generic)  
[Wikipedia article on Glob style wildcards](https://en.wikipedia.org/wiki/Glob_(programming))

## Keys
- used for primary access to data values
- Unique
- Binary Safe: "Foo", 42, 3.1215. 0xff, any sequence of bytes
- Up to 512MB in size, super long keys not recomanded

### Key Spaces
- no classic databases but uses Logical databases
- Logical database 
    - single flat key space
    - no automatic separation of key names
    - keep it simple, no namespacing complexity
    - identified by a zero-based index
    - default db is: `Database zero`
    - best suited for different key spaces for the same application
    - Restrictions
        - Redis cluster supports only 0
        - many tools asume you use only db0

### Key names structure
    - can use a separator like `:`  
        - `user:id:followes` - `user:100:followers`
    - make sure is consistent between teams
    - case sensitive

### Manipulate keys
- `SET key value [EX seconds] [PX miliseconds] [NX|XX]`
    - set TTL
        - EX - expire after seconds
        - PX - expire after miliseconds
    - check for existance
        - NX - not exists
            - set will not work if the key already exists
        - XX - already exists
            - set will work only if the key already exists
- `GET key`
- `KEYS pattern`
    - blocks everything
    - ! Don't use in production
    - useful for dev
    - `KEYS user:1*`
- `SCAN slot [MATCH pattern] [COUNT count]`
    - iterates using a cursor
    - returns a slot reference
    - safe for production, blocks a small  chunk
    - may return 0 or more keys per call
    - use slot to go further
    - bigger count value might block for a longer time
    - returns cursor 0 when no more keys to iterate
- `DEL key [key ...]`
    - remove the key and the memory associated with the key
    - blocking operation
- `UNLINK key [key ...]`
    - unlink the key
    - memory reclaimed by an async process
    - non-blocking operation
- Keys don't need to exist before is manipulated
- `EXISTS  key [key ...]`
    - 1 exists
    - 0 doesn't exist
- `GETRANGE key start stop` - get elements from string
- `APPEND key string` - appends a string to another value (can be int, wil result string)

### Keys expiration
- Expiration times set in: milliseconds, seconds or UNIX timestamp
- Keys will eventually be deleted after the expiration time passes
- TTL - time to live
    - `EXPIRE key seconds`
    - `EXPIREAT key timestamp`
    - `PEXPIRE key milliseconds`
    - `PEXPIREAT key milliseconds-timestamp`
- insect with
    - `TTL key`
    - `PTTL key`
- remove expiration
    - `PERSIST key`
    - TTL will return -1
- can set with `EX` or `PX` params in `SET`

## Strings
- Binary sequence of bytes
- can store anything: string, integer, binary, comma-separates, json, larger objects like images or videos
- most common use: caching: API response, sessions storage, HTML pages
- can implement counters

- Manipulate with `SET`, `GET`
- classic use case: 
    - cache database response as JSON to offload the database
- Manipulate as a number, but stored still as string
- `INCR`, `INCRBY`, `DECR`, `DECRBY`
    - increment - `INCR key`
    - if not existed will be created as 0 then increment with 1
    - `INCRBY key -1` can also decrement
    - will throw error if not int
- `INCRBYFLOAT key `
- `TYPE key` - string
- `OBJECT ENCODING key` - eg: int, embstr

- supports Polymorphism - can change data type
- no schema enforcing

## Hashes
- similar to a Python dictionaries
- mutable: add, change, increment, remove
- store values as strings
- schemaless, but can think as lightweight objects or as rows
- create - `HSET key field value [field value ..]`
- get one `HGET key field`
- get all - `HGETALL key`
- update - `HSET key field other_value`
- delete one field - `HDEL key field`
- increment - `HINCRBY key field value` or `HINCRBYFLOAT`
- performance O(1)
- `HGETALL` - O(n)
- good for small number of fields
- not good for JSON, better use RedisJSON
- delete full hash `DEL key`
- `HEXISTS key field`
- set if not exists `HSETNX key field value` 
- `HSCAN key cursor MATCH pattern` - more efficient than HGETALL
- `HMGET key field [field ..]`
- `HKEYS key` - get all fields from hash - dev only
- `HVALS key` - get all values from hash - dev only
- good for sessions, rate limiting

## Lists
- similar to a Python list
- can add duplicate elements
- implemented as a doubly linked list
- great for sorting strings, implementing stacks and queues
- add elements `LPUSH key value` to the left,  `RPUSH key value` to the right
- remove elements `LPOP key value` from the left, `RPOP key value` from the right
- when you remove the last element, the list will not exist any more
- find first 5 elements `LRANGE key 0 5`
- find last 5 elements `LRANGE key -5 -1`
- get all elements `LRANGE key 0 -1`
- length `LLEN`
- LPOP, RPUSH, LLEN - O(1)
- LRANGE - O(s+n) start+number of elements
- `LMOVE` atomically moves elements from one list to another
- `LTRIM` reduces a list to the specified range of elements
- stack: `LPUSH` & `LPOP`
- queue: `RPUSH` & `LPOP`
- `LINDEX key index`
- `LINSERT key BEFORE/AFTER pivot_value`
- `LSET key index value`
- `LREM key cout value`
- usage: activity stream (recent activity), producer-consumer

## Sets
- set of values with no duplicates
- good for deduplication
- order not guaranteed
- efficient membership check
- `SADD key value` - add an element
- `SCARD key` - number of members
- `SISMEMBER key value` - check value exists
- `SINTER key1 key2` - find common elements in sets
- `SMEMBERS key` - get all values, not for prod
- `SSCAN key cursor [MATCH pattern] [COUNT count]`
- `SREM key value`
- `SPOP key count` - removes count elements, default 1
- `SUNION a b` - all distinct elements
- `SDIFF a b` - elements in a but not in b
- `SINTERSTORE`, `SUNIONSTOR`, `SDIFFSTORE` - store the result
- use cases:
    - tag cloud
    - unique visitors about.html:20240311, can set expire
- logged visitors pattern
    - `SADD online:1000 42` & `SADD online:1050 42` 
        - add to the current and next 5min interval
        - set ttl to 5min, 10min
    - read from the `online:1000` set
    - no need to remove players

## Sorted sets
- ordered list of elements
- useful for: priority queues, leader boards and secondary indexing in general
- set member and score (float)
    - sort by score, then member lexicographic
- can have same score, but the set contains unique values
- `ZADD key score member`
- `ZADD key [NX|XX] [CH] [INCR] score member [score member]`
    - NX - adds if not exists
    - XX - updates an existing element
    - CH - return the number of elements changed
    - INCR - increment score member pair
- `ZINCRBY key increment member`
- `ZRANGE key start end [WITHSCORES]`
- `ZREVRANGE key start end [WITHSCORES]`
- `ZRANK key member` - get the member rank, 0 based
- `ZREVRANK key member` - element 0 has the largest score
- `ZSCORE key member` - returns the members score
- suports Union and Intersection
- not nestable
- `ZCOUNT key min max` - count elements between min and max score inclusive
- `ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]` - get elements by score, starting at min
- `ZREM key member [member]` - match by value, not score
- `ZREMRANGEBYLEX key min max` - remove by value for the same score
    - `ZREMRANGEBYLEX myzset (alpha [omega` can specify exclusive or inclusive
- `ZREMRANGEBYRANK` - remove by position
- `ZREMRANGEBYSCORE` - remove by score

- allow Intersection and Union, not Diff
    - the results are only available through another set
```
ZINTERSTORE dest numkeys key [key ..]
[WEIGHTS weight [weight]]
[AGGREGATE SUM|MIN|MAX]
```
```
ZUNIONSTORE dest numkeys key [key ..]
[WEIGHTS weight [weight]]
[AGGREGATE SUM|MIN|MAX]
```
- use cases
    - leaderboard
        - `ZADD lb ...`
        - `ZINCRBY lb 50 jane`
        - `ZREVRANGE lb 0 2 WITHSCORES` - top 3
        - `ZREMRANGEBYRANL lb 0 -4` - reduce the list to 3 elements
    - priority queue
        - `ZRANGE pq 0 0` - get the first by priority
        - `ZREM pq p1-item1` - remove by value
        - can be combined in a transction to make them safe
        