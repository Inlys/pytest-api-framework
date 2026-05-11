# 启动项目的入口

import pytest
import os


# 启动框架。加上["-v"]，显示详细执行日志
# 1. 运行 pytest，生成 Allure 结果数据到 temps 文件夹
pytest.main(["-v", "--alluredir=temps"])

# 输出报告，等同于在终端输入命令
# 2. 生成 HTML 报告到 report 文件夹
os.system("allure generate temps -o report --clean")

# 3. （可选）直接打开报告，自动启动浏览器
os.system("allure serve temps")
