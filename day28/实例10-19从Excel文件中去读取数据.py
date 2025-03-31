import openpyxl
#打开工作表
workbook = openpyxl.load_workbook('景区天气.xlsx')
#选择要操作的工作表
sheet=workbook['景区天气']
#表格是二维数组，先遍历的是行，再遍历列
lst=[]#存储的是行数据
for row in sheet.rows:
    sublst=[]
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)


for item in lst:
    print(item)