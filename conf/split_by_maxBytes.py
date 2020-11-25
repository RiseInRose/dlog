# coding:utf-8
# author caturbhuja
# date   2020/11/25 11:14 上午 
# wechat chending2012 
import sys
import os
import logging

log_level_build_in = {
    "info": logging.INFO,
    "warning": logging.WARNING,
    "warn": logging.WARNING,
    "error": logging.ERROR,
    "debug": logging.DEBUG,
}


class ConfigCook:
    @staticmethod
    def _make_handlers(handler_name, log_level, log_path, max_bytes, backup_count, encoding):
        handler_dict = {
            handler_name: {
                'level': log_level,
                'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
                'formatter': 'standard',
                'filename': log_path,
                'maxBytes': 1024 * 1024 * int(max_bytes),  # 当达到50MB时分割日志
                'backupCount': backup_count,  # 备份份数
                'encoding': encoding,
            }
        }
        return handler_dict

    @staticmethod
    def _make_loggers(logger_name, handler_name, only_console, log_level):
        logger_dict = {
            logger_name: {
                'handlers': ['console'] if only_console else [handler_name, 'console'],
                'level': log_level,
                'propagate': False,  # 是否传递给父记录器
            }
        }
        return logger_dict

    @staticmethod
    def _make_logger_framework(debug):
        log_framework_dict = {
            "version": 1,
            'disable_existing_loggers': True,
            'loggers': {
            },
            'handlers': {
                # 输出到控制台
                'console': {
                    'level': logging.DEBUG if debug else logging.INFO,
                    'class': 'logging.StreamHandler',
                    'formatter': 'standard',
                    'stream': sys.stdout
                },
                # 输出到文件
            },
            'filters': {},
            'formatters': {
                # 标准输出格式
                'standard': {
                    'format': '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                }
            }
        }
        return log_framework_dict

    @classmethod
    def cook(
            cls, file_list, log_dir_path, debug=False, only_console=False, max_bytes=50, backup_count=7,
            encoding='utf-8'
    ):
        frame = cls._make_logger_framework(debug)
        for each in file_list:
            # make loggers
            log_level = log_level_build_in[each["log_level"].lower()]
            loggers = cls._make_loggers(
                logger_name=each["file_name"], handler_name=each["file_name"],
                only_console=only_console, log_level=log_level
            )
            frame["loggers"].update(loggers)

            # make handlers
            log_path = os.path.join(log_dir_path, "{}.log".format(each["file_name"]))
            handlers = cls._make_handlers(
                handler_name=each["file_name"], log_level=log_level, log_path=log_path,
                max_bytes=max_bytes, backup_count=backup_count, encoding=encoding
            )
            frame["handlers"].update(handlers)
        return frame


"""
配置样例，供参考使用：
    log_model_config = {
        "version": 1,
        'disable_existing_loggers': True,
        'loggers': {
            'log.info': {
                'handlers': ['console'] if debug else ['info', 'console'],
                'level': logging.INFO,
                'propagate': False,  # 是否传递给父记录器
            },
            'log.warning': {
                'handlers': ['console'] if debug else ['warning', 'console'],
                'level': logging.WARNING,
                'propagate': False,  # 是否传递给父记录器
            },
            'log.error': {
                'handlers': ['console'] if debug else ['error', 'console'],
                'level': logging.ERROR,
                'propagate': False,  # 是否传递给父记录器
            },
            
        },
        'handlers': {
            # 输出到控制台
            'console': {
                'level': logging.INFO,
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'stream': sys.stdout
            },
            # 输出到文件
            'info': {
                'level': logging.INFO,
                'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
                'formatter': 'standard',
                'filename': info_log_path,
                'maxBytes': 1024 * 1024 * int(max_bytes),  # 当达到50MB时分割日志
                'backupCount': backup_count,  # 备份份数
                'encoding': encoding
            },
            'warning': {
                'level': logging.WARNING,
                'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
                'formatter': 'standard',
                'filename': warning_log_path,
                'maxBytes': 1024 * 1024 * int(max_bytes),  # 当达到50MB时分割日志
                'backupCount': backup_count,  # 备份份数
                'encoding': encoding,
            },
            'error': {
                'level': logging.ERROR,
                'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
                'formatter': 'standard',
                'filename': error_log_path,
                'maxBytes': 1024 * 1024 * int(max_bytes),  # 当达到50MB时分割日志
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

"""
