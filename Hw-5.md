# Homework week 5

Quizz Usecase 1
- `geodist geo:venues "National Stadium" "Ariake Arena" mi`
- `geodist geo:events:Football "Olympic Stadium" "International Stadium Yokohama" km`

Quizz Usecase 2
- iterating over Lua tables requires ipairs() and you can assign keys to a throw-away variable `_`
    - `for _, value in ipairs(values) do`


- 5.1 - having 3 points
    - `geoadd hw5-1 139.75 35.693333 "Nippon Budokan" 139.860339 35.648333 "Kasai Rinkai Park" 139.815139 35.651411 "Olympic Aquatics Centre"`
    - use geodist to find distance in km
    - `geodist hw5-1 "Olympic Aquatics Centre" "Nippon Budokan" km`
- 5.2 - Redis Geospatial objects are stored as Sorted Sets
- 5.3 - Use Sorted Sets specific commands to delete: `ZREM`
- 5.4 - redis.call will return an error if it fails
- 5.5 - `eval "return KEYS[2]" 3 key1 key2 key3` 3 keys are passed one-indexed so key2
- 5.6 - `SCRIPT LOAD` command returns a sha1 hash
- 5.7 - the Lua script gets a list of keys stored in the set and expires them

