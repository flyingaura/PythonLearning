# -*- coding: utf-8 -*-

from LearnModule import StringSplit

# 定义一个过滤的行政区划名表
#
filter_province = ('省', '市', '自治区')
filter_city = ('区', '县')
filter_towns = ('街道', '镇', '乡', '回民乡')
filter_street = ('社区','村')

class wordlist(object):  #定义一个词表内词输出的类

    def __init__(self,word_name,word_nominal,word_freq,word_note):
        self.word_name = word_name
        self.word_nominal = word_nominal
        self.word_freq = word_freq
        self.word_note = word_note

class toponymy(object):  #定义一个地名词的类

    def __init__(self,province,city,towns,street):
        self.province = province
        self.city = city
        self.towns = towns
        self.street = street

    def alias_province(self):
        alias_province_list = []
        for astr in filter_province:
            if(len(self.province) > len(astr) and len(self.province) > 2):
                filter_index = len(self.province) - len(astr)
                if(self.province.find(astr) == filter_index):
                    alias_province_list.append(self.province[:filter_index])
        if (alias_province_list):
            return alias_province_list
        else:
            return None

    def alias_city(self):
        alias_city_list = []
        for astr in filter_city:
            if (len(self.city) > len(astr) and len(self.city) > 2):
                filter_index = len(self.city) - len(astr)
                if(self.city.find(astr) == filter_index):
                    alias_city_list.append(self.city[:filter_index])
        if(alias_city_list):
            return alias_city_list
        else:
            return None

    def alias_towns(self):
        alias_towns_list = []
        for astr in filter_towns:
            if (len(self.towns) > len(astr) and len(self.towns) > 2):
                filter_index = len(self.towns) - len(astr)
                if(self.towns.find(astr) == filter_index):
                    alias_towns_list.append(self.towns[:filter_index])
        if (alias_towns_list):
            return alias_towns_list
        else:
            return None

    def alias_street(self):
        alias_street_list = []
        for astr in filter_street:
            if (len(self.street) > len(astr) and len(self.street) > 2):
                filter_index = len(self.street) - len(astr)
                if(self.street.find(astr) == filter_index):
                    alias_street_list.append(self.street[:filter_index])
        if (alias_street_list):
            return alias_street_list
        else:
            return None

toponymy_list = []
the_towns = '-'
with open('C:/Users/flyingaura/Desktop/昌平区.dat', mode = 'rb') as in_file:
    the_province = '北京市'
    the_city = in_file.readline().decode('utf-8').strip()
    for rec in in_file.readlines():
        rec_data = rec.decode('utf-8').strip()
        if ('\t' in rec_data):
            rec_TS = StringSplit.stringsplit(rec_data,'\t')
            the_towns = rec_TS[0]
            rec_street = rec_TS[1].strip('\"')
        else:
            rec_street = rec_data.strip('\"')

        if(rec_street):
            for the_street in StringSplit.stringsplit(rec_street,'、'):
                rec_toponymy = toponymy(the_province, the_city, the_towns, the_street)
                toponymy_list.append(rec_toponymy)

# for rec_ty in toponymy_list:
#     print('============ %s' %rec_ty.street)

province_list = []
city_list = []
towns_list = []
street_list = []
Aprovince_list = []
Acity_list = []
Atowns_list = []
Astreet_list = []

for A_toponymy in toponymy_list:
    if(A_toponymy.province not in Aprovince_list):
        province_list.append(wordlist(A_toponymy.province, 'tag', 1000, A_toponymy.province))
        Aprovince_list.append(A_toponymy.province)
    alias_PL = A_toponymy.alias_province()
    if(alias_PL):
        for A_province in alias_PL:
            if(A_province not in Aprovince_list):
                province_list.append(wordlist(A_province, 'tag', 1000, A_toponymy.province))
                Aprovince_list.append(A_province)
    # print(province_list)

    if (A_toponymy.city not in Acity_list):
        city_list.append(wordlist(A_toponymy.city, 'tag', 1000, A_toponymy.province))
        Acity_list.append(A_toponymy.city)
    alias_CL = A_toponymy.alias_city()
    if(alias_CL):
        for A_city in alias_CL:
            if (A_city not in Acity_list):
                city_list.append(wordlist(A_city, 'tag', 1000, A_toponymy.province))
                Acity_list.append(A_city)

    if (A_toponymy.towns not in Atowns_list):
        towns_list.append(wordlist(A_toponymy.towns, 'tag', 1000, A_toponymy.city))
        Atowns_list.append(A_toponymy.towns)
    alias_TL = A_toponymy.alias_towns()
    if(alias_TL):
        for A_towns in alias_TL:
            if (A_towns not in Atowns_list):
                towns_list.append(wordlist(A_towns, 'tag', 1000, A_toponymy.city))
                Atowns_list.append(A_towns)

    # if (A_toponymy.street not in street_list):
    street_list.append(wordlist(A_toponymy.street, 'tag', 1000, A_toponymy.towns))
    alias_SL = A_toponymy.alias_street()
    if(alias_SL):
        for A_street in alias_SL:
            # if (A_street not in street_list):
            street_list.append(wordlist(A_street, 'tag', 1000, A_toponymy.towns))

with open('C:/Users/flyingaura/Desktop/北京地址1.txt', mode = 'a') as out_file:
    for A_province in province_list:
        print('%s\t%s\t%d\t%s' %(A_province.word_name, A_province.word_nominal,
                                 A_province.word_freq, A_province.word_note))
        out_file.write('%s\t%s\t%d\t%s\n' %(A_province.word_name, A_province.word_nominal,
                                 A_province.word_freq, A_province.word_note))
    for A_city in city_list:
        print('%s\t%s\t%d\t%s' % (A_city.word_name, A_city.word_nominal,
                                  A_city.word_freq, A_city.word_note))
        out_file.write('%s\t%s\t%d\t%s\n' % (A_city.word_name, A_city.word_nominal,
                                             A_city.word_freq, A_city.word_note))

    for A_towns in towns_list:
        print('%s\t%s\t%d\t%s' % (A_towns.word_name, A_towns.word_nominal,
                                  A_towns.word_freq, A_towns.word_note))
        out_file.write('%s\t%s\t%d\t%s\n' % (A_towns.word_name, A_towns.word_nominal,
                                             A_towns.word_freq, A_towns.word_note))

    for A_street in street_list:
        print('%s\t%s\t%d\t%s' % (A_street.word_name, A_street.word_nominal,
                                  A_street.word_freq, A_street.word_note))
        try:
            out_file.write('%s\t%s\t%d\t%s\n' % (A_street.word_name, A_street.word_nominal,
                                             A_street.word_freq, A_street.word_note))
        except UnicodeEncodeError as e:
            out_file.write('******\t%s\n' %e)











