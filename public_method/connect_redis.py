# -*- coding: utf-8 -*-
"""
@Time    : 2020/10/12 9:13
@Author  : liufubin
@FileName: connect_redis.py
@description: 连接redis公共方法
"""
import redis


class ConnectRedis(object):
    """redis操作，初始化传入连接信息并连接"""
    def __init__(self, host='192.168.1.29', port=6379, password='twznW28grxzk', db='2'):
        redis.ConnectionPool(host=host, port=port, password=password, decode_responses=True)
        self.redisdb = redis.Redis(host=host, port=port, password=password, decode_responses=True, db=db)

    def redis_type(self, name):
        """获取redis-key的type(类型)"""
        redis_type = self.redisdb.type(name=name)
        return redis_type

    def redis_keys(self, pattern='*'):
        """redis使用keys查看所有的key"""
        redis_keys = self.redisdb.keys(pattern=pattern)
        return redis_keys

    def redis_set(self, name, value, ex=None, nx=False):
        """redis的string类型数据set数据方法,需要传入key和value,ex为设置过期时间,假如nx设置为true，只有当key不存在的时候才可以写入"""
        redis_set = self.redisdb.set(name=name, value=value, ex=ex, nx=nx)
        return redis_set

    def redis_mset(self, mapping):
        """redis的string类型数据set多个key与value，传入的值为字典"""
        redis_mset = self.redisdb.mset(mapping=mapping)
        return redis_mset

    def redis_get(self, key):
        """redis的string类型数据获取value方法"""
        redis_get = self.redisdb.get(key)
        return redis_get

    def redis_mget(self, keys):
        """redis的string数据类型get多个key的值,传入的值为key组成的list"""
        redis_mget = self.redisdb.mget(keys=keys)
        return redis_mget

    def redis_hset(self, name, key, value):
        """redis的hash数据类型hset数据方法"""
        redis_hset = self.redisdb.hset(name=name, key=key, value=value)
        return redis_hset

    def redis_hget(self, name, key):
        """redis的hash数据类型获取某个key对应value方法"""
        redis_hget = self.redisdb.hget(name=name, key=key)
        return redis_hget

    def redis_hgetall(self, name):
        """redis的hash数据类型获取某个name对应所有key的value方法"""
        redis_hgetall = self.redisdb.hgetall(name=name)
        return redis_hgetall

    def redis_hkeys(self, name):
        """获取redis的hash数据name对应的所有key"""
        redis_hkeys = self.redisdb.hkeys(name=name)
        return redis_hkeys


if __name__ == '__main__':
    connect = ConnectRedis()
    # Type = connect.redis_type(name='"USER_CELLPHOME_13055866827"')
    result = connect.redis_get(key='"USER_CELLPHOME_18888888880"')
    keys = connect.redis_keys(pattern='*USER_CELLPHOME*')
    # dict1 = {'key1': '1', 'key2': '2'}
    # result1 = connect.redis_mset(dict1)
    print(result)
    # print(Type)
    # print(keys)
