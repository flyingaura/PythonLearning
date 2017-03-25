# -*-coding: utf-8 -*-

class Hello(object):
    def hello(self,name = 'world'):
        # print('hello,%s' % name)
        return 'hello,%s' % name

h = Hello()
h.hello('aaaa')
print(type(Hello))
print(type(Hello()))
print(type(h))
print(Hello())