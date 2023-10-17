# import module_a #导⼊
# from module import xx # 导⼊某个模块下的某个⽅法 or ⼦模块
# from module.xx.xx import xx as rename #导⼊后⼀个⽅法后重命令
# from module.xx.xx import * #导⼊⼀个模块下的所有⽅法，不建议使⽤
# module_a.xxx #调⽤

import os
import sys

print(__file__) # 当前脚本的路径
print(os.path.dirname(os.path.dirname(__file__))) # 获取动态的路径
base_path = os.path.dirname(os.path.dirname(__file__)) # 根目录下的路径

sys.path.append(base_path) # 自定义模块的路径append目录e:\pythonDevelopement查找
print(sys.path)

import my_first_model

print(os.listdir())
print(os.system("uname")) # 获取操作系统的版本号 MINGW64: c语言的编译器可以在win下面运行
print(os.stat("my_first_model.py")) # 获取文件的详细信息
sys.argv # 获取详细参数