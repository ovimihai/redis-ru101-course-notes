# Homework week 2

- 2.1 - The difference between the sets is only "A" case sensitive
- 2.2 - "xyz" will be inserted after c, so "b", "c", "xyz" will be the result
- 2.3 - Use `ZCARD hw2-3` for the cardinality. The `zremrangebyrank` command removes avery element from rank 2 to the end, only elements 0 and 1 remains, so the cardinalty is 2.
- 2.4 - Can not cap while adding elements. Use zrem for that
- 2.5 - Can use `SSCAN fs:disabled_access:True 0` to find all 31 elements
- 2.6 - O(1) means constant time complexity
- 2.7 - `HMGET` time complexity is also affected by the size of the data stored in each requested field
- 2.8 - SINTER for A= False, B=Female, C=E
    - A=False => 80% from 20k = 16k
    - B=Female => 45% from 10k = 4.5k
    - C=E => 20% from 15k = 3k
    - the intersection cardinality will be as the smallest set - 3k

