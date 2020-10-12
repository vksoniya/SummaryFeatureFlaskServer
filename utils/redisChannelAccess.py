import redis
import json

CHANNEL_NAME = "from-voice-conf-redis-channel"

def subscribeToRedisChannel():
    #This function will listen to the Redis channel and returns channel message
    r = redis.Redis(host='127.0.0.1', port=6379)
    p = r.pubsub()
    p.subscribe(CHANNEL_NAME)
    #p.subscribe('to-voice-conf-redis-channel')

    p.get_message()

    return p.listen()