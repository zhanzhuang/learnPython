# 文件格式很固定
from distutils.core import setup

setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="itheima's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="itheima",  # 作者
      author_email="itheima@itheima.com",  # 作者邮箱
      url="www.itheima.com",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
# 1.第一步创建setup.py

# 2.第二步 命令行输入：python setup.py build

# 3.使用tree查看目录 发现目录中有压缩包

# 4.命令行中输入：python setup.py sdist

# 5.最终生成的tar.gz就是打包好的源文件
