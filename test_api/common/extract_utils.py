# 统一在这里提取变量,封装成函数

import jsonpath

def extract(resp, var_name, exp):
    # resp.json() 是 requests 库的方法，用来把接口响应的JSON转成 Python 字典，并把结果存到resp.json
    # 这里的json是resp的键，转成的字典是对应的值
    try:
        resp.json = resp.json()
    except Exception:
        # 解析失败（比如响应不是 JSON 格式），就把 resp.json 设为空字典 {}，避免程序崩溃
        resp.json = {}

    # 反射方式获取响应。
    # var_name是yaml文件extract的"json"，是字符串
    # getattr()用字符串取属性，下面表达式等价于name = resp.json，返回json字典
    # 去 resp 里面，找到名字叫 json 的属性，把它对应的值取出来
    name = getattr(resp, var_name)
    # 用 jsonpath 库，根据yaml内的表达式 $.data.token，从响应字典里提取对应的值
    res = jsonpath.jsonpath(name, exp)
    return res[0]