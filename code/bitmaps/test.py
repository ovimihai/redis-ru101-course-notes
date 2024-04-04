from redis import Redis
import os

def format_binary(key, size):
  data = redis.execute_command("GET", key)
  
  result = []
  for b in data:
    result.append( bin(b)[2:].rjust(size, '0') )
    # ' - ' + str(data)
  
  return ' '.join(result)
    

def test_bits():
    size = 8
    size_str = "u" + str(size)
    key = 'bf1'
    
    print('size: ' + size_str)

    for i in range(0, 16):
      offset = 5
      val = i
      print('offset: ' + str(offset) + ' value: ' + str(val).rjust(2, ' '), end = ' - ')
      redis.execute_command("DEL", key)
      redis.execute_command("BITFIELD", key, "SET", size_str, offset, val)

      print(format_binary(key, size))

    # res = redis.execute_command("BITFIELD", key, "GET", size_str, 2)
    # print(res)


def main():
  """ Main, used to call test cases for this use case"""

  global redis
  redis = Redis(host=os.environ.get("REDIS_HOST", "redis"),
                port=os.environ.get("REDIS_PORT", 6379),
                password=os.environ.get("REDIS_PASSWORD", None),
                db=0, decode_responses=False)
  test_bits()

if __name__ == "__main__":
  main()