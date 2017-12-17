# -*- coding: utf-8 -*-
import os

# 定义一个检查文件是否存在的函数checkfile()
def checkfile(filepath):
    file_Base = os.path.split(filepath)
    if(file_Base[0] == ''):
        file_dir = os.getcwd()
    else:
        file_dir = file_Base[0]
    if(os.path.exists(file_dir)):
        if(file_Base[1] in os.listdir(file_dir)):
            return True

    return False

# 定义一个复制文件的函数copyfile()
def copyfile(sourcefile,targetfile = None):
    if(not checkfile(sourcefile)):
        raise FileExistsError('源文件不存在，请检查文件路径！')

    with open(sourcefile, mode = 'rb') as inFile:
        File_text = inFile.read()

    on_tag = 1   #1 为复制，0 为取消
    if(targetfile):
        if(checkfile(targetfile)):
            while(True):
                req = input('目标文件已经存在，请确认是否覆盖:Y or N')
                if(req.lower() == 'y' or req.lower() == 'yes'):
                    on_tag = 1
                    break
                elif(req.lower() == 'n' or req.lower() == 'no'):
                    on_tag = 0
                    break
                else:
                    print('输入错误，请重试！')
        else:
            new_dir = os.path.split(targetfile)[0]
            if(new_dir):
                if(not os.path.exists(new_dir)):
                    os.makedirs(new_dir)
            else:
                targetfile = os.path.join(os.getcwd(), targetfile)

    else:   #不指定输出目标文件路径，则默认复制到源文件目录下，复制文件名称后+'copy'
        copy_file_path = os.path.split(sourcefile)
        copy_file_name = os.path.splitext(copy_file_path[1])
        targetfile = os.path.join(copy_file_path[0], copy_file_name[0] + '_copy' + copy_file_name[1])

    if(on_tag):
        with open(targetfile, mode = 'wb') as outFile:
            outFile.write(File_text)
        print('文件已成功复制到：%s' %(targetfile))
    else:
        print('取消复制，程序结束！')


# ====== 主程序 ======
sourcefile = 'F:/documents/python/测试数据/leaf/python常用模块资料.txt'
targetfile = 'copytest.dat'

copyfile(sourcefile,targetfile)