# -*- coding: utf-8 -*-
"学习类的动态属性调用"

class API_url(object):

    def __init__(self,path = ''):
        self.path = path

    def __getattr__(self,Apath):
        if (Apath == 'aggregation'):
            return lambda one:API_url('%s?%s' %(self.path,one))
        return API_url('%s/%s' %(self.path,Apath))

    def __call__(self,name = ''):
        if (name != ''):
            return API_url('%s:%s' %(self.path,name))
        else:
            return API_url('%s' % self.path)

    def __str__(self):
        return self.path

    __repr__ = __str__

msp_api = API_url('192.168.10.5')

print(msp_api('7071').jcoder.mssapi.search.aggregation('keyword')('好好学习'))
