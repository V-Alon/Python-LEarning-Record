s='HelloPython,HelloJava,hellophp'
search_str=input('请输入要统计的字符(大写):')
print('{0}在{1}中一共出现了{2}次'.format(search_str,s,s.upper().count(search_str)))
