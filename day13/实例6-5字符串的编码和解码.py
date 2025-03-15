#编码解码
s='伟大的中国梦'
#编码是将str转为bytes
scode=s.encode(errors='ignore')#默认UTF-8，中文占3个字节
print(scode)

scode_gbk=s.encode('gbk',errors='ignore')
print(scode_gbk)


#编码中出错问题
s2='耶✌️'
s2code=s2.encode('gbk',errors='replace')
print(s2code)
#'gbk' codec can't encode character '\u270c' in position 1: illegal multibyte sequence
#encoding with 'gbk' codec failed改为严格strict


#解码过程bytes转换为str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))


