import redis

publisher = redis.Redis(host = 'localhost', port = 6379)
message = ''
channel = 'test'
while (message != 'exit'):
    message = input('Enter a message to publish: ')
    publisher.publish(channel, message)