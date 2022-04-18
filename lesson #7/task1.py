"""Hello"""
# task 1
import os
if not os.path.exists('my_project'):
    os.mkdir('my_project')
    os.makedirs('my_project\\mainapp')
    os.makedirs('my_project\\settings')
    os.makedirs('my_project\\adminapp')
    os.makedirs('my_project\\authapp')

##################


import os

path = r'C:\Users\ббб\PycharmProjects\pythonProject7'
project_name = 'my_project'
folders = ['settings',
           'mainapp',
           'authapp',
           'adminapp']


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


fullpath = os.path.join(path, project_name)
create_folder(fullpath)
