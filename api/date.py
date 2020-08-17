#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

def Get_age_by_ID_number(ID_number):
	'''
	@comment:通过身份证号获取年龄
	'''
	birth_str = ID_number[6:14]
	birth_date = datetime.datetime.strptime(birth_str, "%Y%m%d")
	cur_date = datetime.datetime.now()
	birth_t = birth_date.replace(year=cur_date.year)

	if cur_date > birth_t:
		age = cur_date.year - birth_date.year
	else:
		age = cur_date.year - birth_date.year - 1
	return int(age)

if __name__ == '__main__':
	ID_number = '621402198903137421'
	age = Get_age_by_ID_number(ID_number)
	print age

