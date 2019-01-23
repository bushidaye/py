# _*_coding:utf-8_*_
'''
选出两个文件的交集
'''
with open('im') as im,open('zx') as zx:
    fim=im.readlines()
    fzx=zx.readlines()
    im.close()
    zx.close()
    for i in fim:
        if i in fzx:
            print i

