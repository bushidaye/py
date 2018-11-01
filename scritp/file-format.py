# _*_coding:utf-8_*_
'''
在每一行末尾追加‘；’不能在同一文件修改，写到另一个文件
'''
with open('log1.sql', 'r') as f1, open('log2.sql', 'w') as f2:
    for line in f1.readlines():
        if not line.strip().endswith(';'):
            line = line.replace(line, line.strip() + ';\n')
        f2.write(line)


print 'cd vcdv '.strip()