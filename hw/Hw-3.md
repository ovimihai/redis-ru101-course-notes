# Homework week 3

- 3.1 - That is an example of an atomic operation
- 3.2 - In a `WATCH` command you can observe one or more keys
- 3.3 - The `WATCH` command canbe called multiple times in a `MULTI` command
- 3.4 - The `DISCARD` throws aray the queued commands, but does not undo the already executed commands in a Transaction
- 3.5 - There are multiple ways to store objects with relationships in redis
    - Serialize the object into a String datatype
    - Flatten the relationships and hierarchy into fields in a Hash
    - Normalize the structure into multiple Hashes
    - Normalize the structure into multiple Hashes and Sets
- 3.6 - An `EXEC` command would fail due to a syntax error or if a watched key is modified by another client
