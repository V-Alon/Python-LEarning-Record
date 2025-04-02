import prettytable as pt
from numpy.ma.core import choose


#显示座席
def show_ticket(row_num):
    tb=pt.PrettyTable()#创建表
    #设置标题
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    #遍历有票
    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)



#订票
def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(1,row_num+1):
        if int(row)==i:
            lst=[f'第{i}行','有票','有票','有票','有票','有票']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst=[f'第{i}行','有票','有票','有票','有票','有票']
            tb.add_row(lst)








if __name__ == '__main__':
    show_ticket(6)
    row_num=6

    show_ticket(row_num)


    choose_num=input('请输入选择的座位，如4,3:')
    row,column=choose_num.split(',')
    order_ticket(row_num,row,column)