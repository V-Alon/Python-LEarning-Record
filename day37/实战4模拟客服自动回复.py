def find_answer(qusetion):
    with open('replay.txt', 'r', encoding='gbk') as file:
        while True:
            line = file.readline()
            if line=='':
                break
            keyword=line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question=input('Hi,请输入你要咨询的问题:')
    while True:
        if question=='bye':
            break
        else:
            #开始找答案
            reply=find_answer(question)
            if reply==False:
                question=input('不知道你在说什么，请问问别的吧，退出输入bye:')
            else:
                print(reply)
                question=input('你还要问什么，退出输入bye:')
    print('再见！！！')