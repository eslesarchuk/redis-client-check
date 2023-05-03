#!/usr/bin/env python

import redis

hosts = ['redis3', 'redis4', 'redis5', 'redis6', 'redis62', 'redis7']

for host in hosts:
  r = redis.Redis(host=host, port=6379, decode_responses=True)
  print r.info('server')['redis_version']
