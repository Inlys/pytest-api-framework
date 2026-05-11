# 在这里统一读取yaml文件。安装插件pip install pyyaml

import yaml

def load_yaml(path):
    # 读取yaml文件，并保证中文不报错、不乱码
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data