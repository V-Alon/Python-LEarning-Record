try:
    line1=int(input('请输入第一条边的长度:'))
    line2=int(input('请输入第二条边的长度:'))
    line3=int(input('请输入第三条边的长度:'))
    if line1+line2>line3 and line2+line3>line1 and line3+line1>line2:
        print(f'这是一个三角形,{line1},{line2},{line3}')
    else:
        raise Exception(f'这不是一个三角形,{line1},{line2},{line3},不能组成三角形')

except Exception as e:
    print(e)