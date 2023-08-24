import redis

class RedisWrapper:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating a new Redis connection")
            cls._instance = super(RedisWrapper, cls).__new__(cls)
            cls._instance.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')
        return cls._instance

    def lpush(self, key, value):
        self.redis_client.lpush(key, value)

    def ltrim(self, key, start, end):
        self.redis_client.ltrim(key, start, end)
