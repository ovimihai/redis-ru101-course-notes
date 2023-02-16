# RU101 Week 1

[Documentation for Key commands at redis.io](https://redis.io/commands#generic)  
[Wikipedia article on Glob style wildcards](https://en.wikipedia.org/wiki/Glob_(programming))

## Keys
- used for primary access to data values
- Unique
- Binary Safe: "Foo", 42, 3.1215. 0xff, any sequence of bytes
- Up to 512MB in size, super long keys not recomanded

### Key Spaces
- no classic databasesc but uses Logical databases
- Logical database 
    - single flat key space
    - no automatic separation of key names
    - keep it simple, no namespacing complexity
    - identified by a zero-based index
    - dafault db is: `Database zero`
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
    - usefull for dev
    - `KEYS user:1*`
- `SCAN slot [MATCH pattern] [COUNT count]`
    - iterates using a cursor
    - returns a slot reference
    - safe for production, blocks a small  chunk
    - may return 0 or more keys per call
    - use slot to go further
    - bigger count value might block for a longer time
    - returns cursor 0 whan no more keys to iterate
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

### Keys expiration
- Expiration times set in: miliseconds, seconds or UNIX timestamp
- Keys will eventually be deleted after the expiration time passes
- TTL - time to live
    - `EXPIRE key seconds`
    - `EXPIREAT key timestamp`
    - `PEXPIRE key miliseconds`
    - `PEXPIREAT key miliseconds-timestamp`
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
- clasic usecase: 
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

