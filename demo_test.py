# coding:utf-8
# author caturbhuja
# date   2020/11/25 2:43 下午 
# wechat chending2012
from dlog import DLog

if __name__ == '__main__':
    # ----------- 设定日志目录绝对路径（强烈建议） -----------
    import os

    RootPath = os.path.dirname(os.path.realpath(__file__))
    log_dir_path = os.path.join(RootPath, 'logs')

    log = DLog(log_dir_path=log_dir_path).get_log
    log.info('nice')
    log.warning('nice')
    log.error('nice')

    # ----------- 添加新的日志类型 -----------
    new_log_file_list = [{"file_name": "access", "log_level": "info"}, ]
    log1 = DLog(new_log_file_list=new_log_file_list).get_log   # 这个方式，日志目录在 现在这个文件平级目录下。
    log1.access('access my lord')

    # ----------- 开启单例模式 -----------
    log2 = DLog(singleton=True).get_log

    log2.info('nice')
    log2.warning('nice')
    log2.error('nice')

    # ----------- 一般方式 -----------
    log3 = DLog().get_log   # 这个方式，日志目录在 现在这个文件平级目录下。
    
    log3.info('nice')
    log3.warning('nice')
    log3.error('nice')
