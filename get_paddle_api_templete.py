'''
template:
    get paddle chinese api
'''

import re
import pandas as pd
from pathlib import Path
from typing import Generator

# 给定需要遍历的目录
# 相对路径
# search_dir: Path = Path(__file__).parent / 'docs' / 'api' / 'paddle'
# 绝对路径
search_dir: Path = Path('xxxxx')
need_list: list[str] = ['.. py:function:: ','.. py:class:: ']
api_list: list[str] = []

# 遍历param目录下的所有文件
def path_find_files(path: Path) -> Generator[Path, None, None]:
    return path.rglob("*.*")

# 需要处理的文件
def unexclude_files(file: Path) -> bool:
    return (file.name != "Overview_cn.rst"
            and file.name != "index_cn.rst"
            and file.suffix == ".rst")

# 需要处理的行
def unexclude_lines(line: str) -> str | None:
    for need in need_list:
        if line.startswith(need):
            match: re.Match[str] | None = re.match(f'{need}(.*?)\\(', line)
            if match:
                return match.group(1).strip()
    return None

# rst路径生成api
def ApiGen(files: Generator[Path, None, None]) -> None:
    for file in files:
        if not unexclude_files(file):
            continue
        with open(file, 'r', encoding='utf-8') as f:
            lines: list[str] = f.readlines()
            for line in lines:
                result: str | None = unexclude_lines(line)
                if result is not None:
                    api_list.append(result)

# 从 xls 文件中获取所有英文 api
def get_api_from_xls(path: Path) -> list[str]:
    df: pd.DataFrame = pd.read_excel(path)
    en_api_list: list[str] = df.iloc[:,0].to_list()
    return en_api_list

if __name__ == '__main__':
    ApiGen(path_find_files(search_dir))
    # print(api_list)
    en_api_list: list[str] = get_api_from_xls(Path('xxxxx'))
    for api in api_list:
        if api not in en_api_list:
            print(api)