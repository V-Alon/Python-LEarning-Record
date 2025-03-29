from my_info import *
from introduce import *
#导入模块中有同名模块和变量函数，后导入的会覆盖前面的
info()


#如果不想覆盖，使用import
import my_info
import introduce
#使用模块的函数和变量模块名打点调用
my_info.info()
introduce.info()