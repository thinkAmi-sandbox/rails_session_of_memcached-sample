import sys
from pymemcache.client.base import Client
from memcached_stats import MemcachedStats

if __name__ == '__main__':
    port = sys.argv[1]
    mem = MemcachedStats('localhost', port)

    client = Client(f'localhost:{port}')
    for key in mem.keys():
        print(client.gets(key))
