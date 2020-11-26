[TOC]

### 介绍
呆log：工业中，python日志模块，安装即用。理论上支持 python2,  python3  

为什么需要这个模块：    

    1. 规范化日志，且开箱即用
    2. 解决了多进程丢失日志问题
    3. 支持单例模式
    4. 可能，真的很优雅
    5. 很简单创建新的日志文件类型
    6. 未来会变成python日志最佳实践
   
注意：作者仅提供使用，作生产使用前，请自行测试。出了问题，不要说自己当时大意，年轻人，要讲码德，望好自为之。  
目前在 centos7.5 环境，mac环境，python3.6， 3.7 测试过。  

[github 地址](https://github.com/RiseInRose/dlog)

### 好的功能
    1. 规范化日志（可能是最佳日志实践）

### 安装方法  

    pip3 install dlog


### 参数介绍
#### 呆log 参数与 使用方法
```python
from dlog import DLog

if __name__ == '__main__':
    # ----------- 设定日志目录绝对路径（强烈建议） -----------
    # 如果没有指定日志目录，则日志目录在 现在现在的执行文件的平级目录下。
    import os

    RootPath = os.path.dirname(os.path.realpath(__file__))

    log = DLog(log_dir_path=RootPath).get_log
    log.info('nice')
    log.warning('nice')
    log.error('nice')

    # ----------- 添加新的日志类型 -----------
    # 1.0.2 新功能
    new_log_file_list = [{"file_name": "access", "log_level": "info"}, ]
    log1 = DLog(new_log_file_list=new_log_file_list).get_log
    log1.access('access my lord')

    # ----------- 修改日志格式 -----------
    # 1.0.3 新功能
    new_log_file_list = [
        {"file_name": "access", "log_level": "warning", "format": "%(levelname)s: %(message)s"},
        {"file_name": "info", "log_level": "info", "format": "%(asctime)s: %(message)s"},
    ]
    log5 = DLog(new_log_file_list=new_log_file_list)
    print(log5.show_log_config)     # 显示日志配置文件
    log5 = log5.get_log
    log5.info('change my info format')
    log5.access('warning my info format')

    # ----------- 设置日志分割大小为10Mb，备份数量 7 份-----------
    log4 = DLog(max_bytes=10, backup_count=7).get_log

    log4.info('nice')
    log4.warning('nice')
    log4.error('nice')

    # ----------- 开启单例模式 -----------
    log2 = DLog(singleton=True).get_log

    log2.info('nice')
    log2.warning('nice')
    log2.error('nice')

    # ----------- 一般方式 -----------
    log3 = DLog().get_log 

    log3.info('nice')
    log3.warning('nice')
    log3.error('nice')
```
   
### 版本说明
    1.0.4 优化用户自定义输入路径。      caturbhuja
    1.0.3 支持 用户 设置日志输出样式，详见文档 《添加新的日志类型》。    caturbhuja
    1.0.2 支持 用户新添加 新日志文件，详见文档 《添加新的日志类型》。    caturbhuja
    1.0.1 第一个版本，能用，但是没有达到最佳实践。    caturbhuja


### 后期版本规划
    整理出日志最佳实践，完成一个开箱能用的工具  
    

### todo
    
    
### 感谢
dlog本身，集合了很多不知名的前辈的杰作，我的贡献和他们比起来，微乎其微。
非常感谢各位前辈的贡献。也希望未来的使用者能一起让这个库更好用。