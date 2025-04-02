import prettytable as pt
#显示座席
def show_ticket(row_num):
    tb=pt.PrettyTable()#创建表
    #设置标题
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    #遍历有票
    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)