#!/bin/sh

# Set the password in the redis.conf
if [ "$REDIS_PASSWORD" ]; then
  echo "requirepass $REDIS_PASSWORD" >> /usr/local/etc/redis/redis.conf
fi

# Execute Redis
exec redis-server /usr/local/etc/redis/redis.conf
