#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

input_folder = r'C:\Documentos\Ivo\GitHub\EZMotion\funcs'

files_list = [x for x in os.listdir(input_folder) if x.startswith('eval')]

for file in files_list:
    print(file)

