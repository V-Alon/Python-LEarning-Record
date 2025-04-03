import datetime
#输入日期
def input_date(): 
    inputdate=input('请输入开始日期（20030815）:')
    datestr=inputdate[0:4]+'-'+inputdate[4:6]+'-'+inputdate[6:]#切出年月日

    dt=datetime.datetime.strptime(datestr, '%Y-%m-%d')
    return dt


if __name__ == '__main__':
    date=input_date()
    in_num=eval(input('请输入间隔间隙:'))
    date=date+datetime.timedelta(days=in_num)
    print(f'最终的日期是{date}')