# Redis University RU101 Course Notes


## Notes
- [Week 1](Week-1.md)
    - Keys, Strings
    - Setup
    - Hashes
    - Lists
    - Sets, Sorted Sets
- [Week 2](Week-2.md)
    - Cardinality
    - Capped Collections
    - Faceted Search
    - Big O notation
- [Week 3](Week-3.md)
    - Transactions
    - Hashes
    - Use case: Inventory Control
- [Week 4](Week-4.md)
    - Bit Data
    - Use case: Seat reservation
    - Publish / Subscribe
    - Use case: Notifications & Fan Out
- [Week 4](Week-4.md)
    - Geospatial
    - Lua scripts


## Materials
- [Code repo](https://github.com/redislabs-training/ru101) - [snapshot here](code/redisu/)

## Try a ready to use development instance
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ovimihai/redis-ru101-course-notes)
- import course data using the code container
    `docker exec -ti code sh import_data.sh`
- use `redis-cli` alias to run redis commands
- run tests in code container
    `docker exec -ti code python redisu/ru101/uc05-finding-venues/finding_venues.py`
