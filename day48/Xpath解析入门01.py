#xpath是在xml文档中搜索内容的一门语言
#html是xml的一个子集

#安装lxml模块
#pip install lxml
from lxml import etree
xml='''
<book>
    <id>1</id>
    <name>遍地野花香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了1</nick>
        </div>
        <span>
            <nick>惹了2</nick>
        </span>
    </author>
    author/div/nick
    author/span/nick
    
    
    
    <partner>
        <nick id="pcc">ppc</nick>
        <nick id="ppbc">ppbc</nick>
    </partner>
</book>
'''
tree=etree.XML(xml)
#result=tree.xpath('/book')#/代表层级关系。第一个/ 是根节点
# result =tree.xpath('/book/name')
# result =tree.xpath('/book/name/text()')#text()拿文本
# result =tree.xpath('/book/author//nick/text()')#//两个“/”后代
# result =tree.xpath('/book/author/*/nick/text()')#   * 任意节点.通配符
result=tree.xpath('/book//nick/text()')
print(result)