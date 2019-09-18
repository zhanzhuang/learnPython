# from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as module2_say_hello
from hm_01_测试模块1 import say_hello

say_hello()
module2_say_hello()
"""
后导入的模块会将先导入的模块覆盖
可以使用别名的方式解决
"""
