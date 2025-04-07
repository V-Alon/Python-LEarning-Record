import os
#删除
# os.remove('./a.txt')#不能删不存在的文件
#重命名
# os.rename('./aa.txt', './new_aa.txt')
#转换时间格式
import time
def date_format(longtime):
    s=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))
    return s
#获取文件信息
info=os.stat('./new_aa.txt')
print(type(info),info)

print('最近一次访问时间',date_format(info.st_atime))
print('在Windows的创建时间',date_format(info.st_ctime))
print('最后一次修改时间',date_format(info.st_mtime))
print(info.st_size)


#打开（启动）文件
# os.startfile('calc.exe')
os.startfile('')