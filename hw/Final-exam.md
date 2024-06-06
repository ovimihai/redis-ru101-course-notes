# Final exam

## Final exam part 1

- 1.1 - or between 3 on #0 position and 3 on #1 position
    ```
    00000000 00000011
    00000011 00000000
    00000011 00000011 - 771
    ```
- 1.2 - Redis guarantees messages order in a single node setup
- 1.3 - Geospatial data is stored in a Sorted Set, so you need to do a ZINTERSTORE
    `ZINTERSTORE dest1 2 geo:events:Football geo:events:Athletics`
- 1.4 - Changes within a transaction are visible in the next commands in the same transaction
- 1.5 - Can't compute distance between two keys
    ```
    ZUNIONSTORE dest15 2 geo:events:Football geo:events:Softball
    GEODIST dest15 "Sapporo Dome" "Yokohama Stadium" km
    ```
- 1.6 - TTL will show the seconds until the key expires
- 1.7 - the BITFIELD is stored as a binary string so you can check the length
- 1.8 - ZUNIONSTORE for Geospatial data does SUM on the common members, you can get the good result with MIN-MAX aggregations

## Final exam part 2

- 2.1 - missing keys type check is none
- 2.2 - when intersecting sets the limiting factors are the smallest set and the number of sets
- 2.3 - ZADD command also accepts inf values as score
- 2.4 - there is no support for nested MULTI commands
- 2.5 - you can watch multiple keys
- 2.6 - pubsub numsub counts only normal subscriptions
- 2.7 - you can HINCRBY a field in a hash with -1
- 2.8 - lists are zero indexed, first index is 0, last index is -1, complexity is the number of elements traversed. 0, 1 and -1, -2 are two elements each


## Final exam part 2

- 3.1 - all ok, you cand get elements from a sorted sets by
    - index (zero-based) and can use negative values
    - score and can use intervals and inf value
- 3.2 - BITCOUNT uses bytes as default for start end position, but you also can specify bit
- 3.3 - you have to add the two tiers (Reserved + General) to get the total
- 3.4 - commands are queued but from the client's perspective it gets the BUSY response
- 3.5 - ```
    ZUNION dest35 2 geo:events:Cycling geo:events:Marathon
    ZUNION dest35 2 geo:events:Cycling geo:events:Marathon
    ```
- 3.6 - in Lua you have to return floats as strings to Redis so they are not converted into ints
- 3.7 - you have to run all WATCH commands before the transactions
- 3.8 - you can store and retrieve UTF-8 data

