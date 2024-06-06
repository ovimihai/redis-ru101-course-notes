# Homework week 1

- 1.1 - You can not define an expiration time for a Hash
- 1.2 - Use `HSETNX` to set a Hash value if the field does not already exist
- 1.3 - Redis checks for datatype and value encoding to determine if an operation can be performed against a key
- 1.4 - Running the commands corectly in order will result 24. Directly pasting can result ab.
- 1.5 - `HGET event:UOYW-ZJAB-SZZQ-RLUJ name`
- 1.6 - `ZRANGE invoice_totals -1 -1 WITHSCORES`
- 1.7 - After spop the last element, the key will not exist any more
- 1.8 - You have to use a `ZRANGEBYSCORE` command starting ar 3 exclusively "(" to infinity
    `ZRANGEBYSCORE hw1-8 (3 +inf`
