import pdfplumber
#打开pdf文件
with pdfplumber.open('小学数学公式.pdf') as pdf:
    for i in pdf.pages:#遍历页
        print(i.extract_text())#extract_text()方法提取内容
        print(f'----------第{i.page_number}结束')