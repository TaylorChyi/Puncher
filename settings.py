# -*- coding: utf-8 -*-
# @Time : 2021/2/19 4:37 下午
# @Author : Qi Tian yue
# @Github : Orange-66
# @PROJECT : Puncher 
# @File : settings.py
# @Remark : 
# -----------------------------
info_file = open('./info.txt')
username = info_file.readline()[9:].strip()
password = info_file.readline()[9:].strip()