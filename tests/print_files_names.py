import os

folder = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\funcs'

files_list = [x for x in os.listdir(folder) if x.endswith('py')]

for file in files_list:
    print(file)