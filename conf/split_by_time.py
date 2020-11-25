# coding:utf-8
# author caturbhuja
# date   2020/11/25 11:12 上午 
# wechat chending2012
import sys
import logging


def set_log_config(
        debug, log_level_info=logging.INFO, log_level_warning=logging.WARNING, log_level_error=logging.ERROR,
        info_log_path=None, warning_log_path=None, error_log_path=None, when="midnight", backup_count=7,
        encoding='utf-8'
):
    """暂时这样，更大自由度，请后续扩充。"""
    log_config_dict = {
        "version": 1,
        'disable_existing_loggers': True,
        'loggers': {
            'log.info': {
                'handlers': ['console'] if debug else ['info', 'console'],
                'level': log_level_info,
                'propagate': False,  # 是否传递给父记录器
            },
            'log.warning': {
                'handlers': ['console'] if debug else ['warning', 'console'],
                'level': log_level_warning,
                'propagate': False,  # 是否传递给父记录器
            },
            'log.error': {
                'handlers': ['console'] if debug else ['error', 'console'],
                'level': log_level_error,
                'propagate': False,  # 是否传递给父记录器
            }
        },
        'handlers': {
            # 输出到控制台
            'console': {
                'level': log_level_info,
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'stream': sys.stdout
            },
            # 输出到文件
            'info': {
                'level': log_level_info,
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'standard',
                'filename': info_log_path,
                'when': when,  # 切割日志的时间
                'backupCount': backup_count,  # 备份份数
                'encoding': encoding
            },
            'warning': {
                'level': log_level_warning,
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'standard',
                'filename': warning_log_path,
                'when': when,  # 切割日志的时间
                'backupCount': backup_count,  # 备份份数
                'encoding': encoding,
            },
            'error': {
                'level': log_level_error,
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'standard',
                'filename': error_log_path,
                'when': when,  # 切割日志的时间
                'backupCount': backup_count,  # 备份份数
                'encoding': encoding,
            },
        },
        'filters': {},
        'formatters': {
            # 标准输出格式
            'standard': {
                'format': '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
            }
        }
    }
    return log_config_dict
