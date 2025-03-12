fruits=['apple','orange','pear','grape']
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('十个苹果')
        case 'orange',3:
            print('三个橘子')
        case 'pear',4:
            print('四个梨')
        case 'grape',5:
            print('五串葡萄')