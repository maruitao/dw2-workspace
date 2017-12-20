
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name = 'eggtest-mrt',  #egg包名
    version = '0.1',
    package = find_packages('my-package'),  # 包含my-package文件夹下的包，排除一些特定的包
#    package_dir = {"","my-package"} ,
    zip_safe = False ,
    
#     package_data={
#         "": ["*.txt"],  # 任何包中含有txt的文件
#         "demo": ["data/*.dat", "doc/*.txt"],  # demo包中data目录下的dat文件
#     }
    
    description = 'egg test demo by mrt',
    long_description = 'egg test long descriptin ',
    author = 'Andre Ma',
    author_email = 'ma.ruitao@cesgroup.com.cn',
    
    license = 'GPL',  # MIT  CMU  
    keywords = ('test', 'egg'),
    platforms = 'CentOS7.2' ,
    url = '' ,
)