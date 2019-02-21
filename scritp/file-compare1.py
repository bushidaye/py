# _*_coding:utf-8_*_
'''
选出两个文件的交集
192.168.0.1 项目 --> 192.168.0.1
'''
with open('im') as im,open('zx') as zx:
    fim=im.readlines()
    fzx=zx.readlines()
    im.close() #可省略，with open模式会自动关闭
    zx.close()
    
    for i in fim:
        for j in fzx:
            if i.find(j.split()[0])==0:
                print i
