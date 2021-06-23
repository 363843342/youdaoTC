# -*- coding: utf-8 -*-
import os



def main():
    os.system('taskkill /IM YoudaoTC.exe /F')
    with open("init.ini", "r", encoding='utf8') as f:
        data = f.readlines()
    if os.path.exists(data[0].replace('\r', '').replace('\n', '')):
        os.remove(data[0].replace('\r', '').replace('\n', ''))
        print('移除成功')
    else:
        print("要删除的文件不存在！")
    os.system(data[1])


if __name__ == '__main__':
    main()
