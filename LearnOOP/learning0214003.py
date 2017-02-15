# 学习类的多重继承
# -*- coding: utf-8 -*-

class Adate(object):
    def __init__(self,type = 'int',value = 'None',length = '0'):
        self.type = type
        self.value = value
        self.length = length
    # __slots__ = ('type','value','length')
    # # pass
    # def showdate(self):
    #     print(self.type,self.value,self.length)

class AField(object):
    def __init__(self,fieldname,tablename,if_only,fieldID):
        # self.type = type
        # self.value = value
        # self.length = length
        self.fieldname = fieldname
        self.tablename = tablename
        self.if_only = if_only
        self.fieldID = fieldID
    # __slots__ = ('fieldname','tablename','if_only','fieldID')
    # def set_field(self,value1,value2,value3,value4):
    #     self.fieldname = value1
    #     self.tablename = value2
    #     self.if_only = value3
    #     self.fieldID = value4
        # return self.fieldname,self.tablename,self.if_only,self.fieldID


class FieldDate(AField,Adate):

    # def __init__(self,fieldname,tablename,if_only,fieldID):
    #     # self.type = type
    #     # self.value = value
    #     # self.length = length
    #     self.fieldname = fieldname
    #     self.tablename = tablename
    #     self.if_only = if_only
    #     self.fieldID = fieldID

    @property
    def fieldissue(self):
        return self._fieldissue

    @fieldissue.setter
    def fieldissue(self,value):
        if (not isinstance(value,str)):
            raise ValueError('the type of fieldissue is WRONG !')
        self._fieldissue = value


# title = FieldDate('int','welcome',255,'title','books01234',True,'000001')
# author = Adate()
# print(author.type,author.value,author.length)
# author.showdate()
title = FieldDate('title','books01234',True,'000001')
# title = FieldDate('content','webnews',False,0000999)
# title = FieldDate()
# title.set_field('content','webnews',False,999000)
# title.showdate()
# title.fieldname = 'title'
# title.fieldID = '00002'
# title.if_only = True
# title.tablename = 'books111'
title.fieldID = 11110000
title.type = 'string'
title.value = 'welcome to beijing'
title.length = 255
title.fieldissue = '123'
title.issue = 'have a good day !'
print(title.type,title.value,title.length)
print(title.fieldname,title.fieldID,title.tablename,title.if_only)
# for value in title_arr:
#     print(value)
# print(list(title_arr))
print(title.fieldissue,title.issue)

