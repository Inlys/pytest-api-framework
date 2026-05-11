# 封装函数，统一遍历yaml文件的内容

# 判断先执行的是请求？响应？返回值？

from venv import logger
import jsonschema
import requests
from responses_validator import validator
import responses_validator
from commons.extract_utils import extract

def runner(k, v, my_var):
    # 用case方法进行判断
    match k:
        # 发送请求
        case 'request':
            # 打印一些log
            logger.info('1、正在发送请求......')
            logger.info(f'请求内容：{v}')

            # 字典需要用**
            # 这里返回接口响应，先存起来，存到一个自己定义的键名resp里，形成键值对
            my_var['resp'] = requests.request(**v)

        # 断言响应
        case 'response':
            logger.info('1、正在断言响应......')
            logger.info(f'响应内容：{v}')

            # 响应断言器，validator( 接口响应 , 预期结果 )
            # 这里的my_var['resp']是响应本身、是一个字典，而my_var是字典套字典
            responses_validator.validator(my_var['resp'], **v)

        # 提取变量
        case 'extract':
            logger.info('1、正在提取变量......')
            logger.info(f'变量内容：{v}')

            # 列表用*，即把列表拆成两个参数传给函数
            for var_name, var_exp in v.items():
                value = extract(my_var['resp'], *var_exp)
                my_var[var_name] = value

