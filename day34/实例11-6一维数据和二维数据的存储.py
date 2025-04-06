#存储一维数据
def my_write():
    lst=['aa','bb','cc','dd','ee']
    with open('studeen.csv','w',encoding='utf-8') as file:
        file.write(','.join(lst))#转成字符串

def my_read():
    with open('studeen.csv','r',encoding='utf-8') as file:
        s=file.read()
        lst=s.split(',')
        print(lst)



if __name__ == '__main__':
    # my_write()
    my_read()