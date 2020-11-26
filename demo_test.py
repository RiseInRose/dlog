# coding:utf-8
# author caturbhuja
# date   2020/11/25 2:43 下午 
# wechat chending2012
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
    new_log_file_list = [{"file_name": "access", "log_level": "info"}, ]
    log1 = DLog(new_log_file_list=new_log_file_list).get_log
    log1.access('access my lord')

    # ----------- 修改日志格式 -----------
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
