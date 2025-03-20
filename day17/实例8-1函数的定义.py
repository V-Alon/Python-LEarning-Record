def get_sum(num):
    s=0
    for i in range(1,1+num):
        s+=i
    print(f'1到{num}之间的累加和为{s}')
    #函数的调用
get_sum(10)     #10是实际参数
get_sum(100)
get_sum(1000)
get_sum(10000)