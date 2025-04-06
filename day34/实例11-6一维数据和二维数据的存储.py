#存储一维数据
def my_write():
    lst=['aa','bb','cc','dd','ee']
    with open('studeen.csv','w',encoding='utf-8') as file:
        file.write(','.join(lst))#转成字符串

if __name__ == '__main__':
    my_write()