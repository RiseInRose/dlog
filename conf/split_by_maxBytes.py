# coding:utf-8
# author caturbhuja
# date   2020/11/25 11:14 上午 
# wechat chending2012 
import sys
import os
import logging
import time

log_level_build_in = {
    "info": logging.INFO,
    "warning": logging.WARNING,
    "warn": logging.WARNING,
    "error": logging.ERROR,
    "debug": logging.DEBUG,
}


class ConfigCook:
    @staticmethod
    def _make_handlers(
            handler_name, log_level, log_path, max_bytes, backup_count, encoding,
            formatter_name='standard', debug=False
    ):
        handler_dict = {
            # 输出到文件
            handler_name: {
                'level': log_level,
                'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
                'formatter': formatter_name,
                'filename': log_path,
                'maxBytes': 1024 * 1024 * int(max_bytes),  # 当达到50MB时分割日志
                'backupCount': backup_count,  # 备份份数
                'encoding': encoding,
            },
            # 输出到控制台
            '{}_console'.format(handler_name): {
                'level': logging.DEBUG if debug else logging.INFO,
                'class': 'logging.StreamHandler',
                'formatter': formatter_name,
                'stream': sys.stdout
            },
        }
        return handler_dict

    @staticmethod
    def _make_loggers(logger_name, handler_name, only_console, log_level):
        console_name = '{}_console'.format(logger_name)
        logger_dict = {
            logger_name: {
                'handlers': [console_name] if only_console else [handler_name, console_name],
                'level': log_level,
                'propagate': False,  # 是否传递给父记录器
            }
        }
        return logger_dict

    @staticmethod
    def _make_formatters(formatter_name, format_):
        _dict = {
            formatter_name: {
                'format': format_,
            }
        }
        return _dict

    @staticmethod
    def _make_logger_framework():
        log_framework_dict = {
            "version": 1,
            'disable_existing_loggers': True,
            'loggers': {
            },
            'handlers': {
                # 输出到控制台
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
        frame = cls._make_logger_framework()
        for each in file_list:
            # --------------- make loggers ---------------
            log_level = log_level_build_in[each["log_level"].lower()]
            loggers = cls._make_loggers(
                logger_name=each["file_name"], handler_name=each["file_name"],
                only_console=only_console, log_level=log_level
            )
            frame["loggers"].update(loggers)

            # --------------- make formatters ---------------
            formatter_name = str(time.time())
            format_ = each.get("format")

            if format_:
                formatters = cls._make_formatters(formatter_name, format_)
                frame["formatters"].update(formatters)

            # --------------- make handlers ---------------
            log_path = os.path.join(log_dir_path, "{}.log".format(each["file_name"]))
            make_handlers_kwargs = {
                "handler_name": each["file_name"], "log_level": log_level, "log_path": log_path,
                "max_bytes": max_bytes, "backup_count": backup_count, "encoding": encoding, "debug": debug
            }
            if format_:
                make_handlers_kwargs["formatter_name"] = formatter_name
            handlers = cls._make_handlers(**make_handlers_kwargs)
            frame["handlers"].update(handlers)

            # --------------- make filters ---------------

        return frame
"""
# 配置样例，供参考使用：
debug = None
max_bytes = 50
backup_count = 7
encoding = 'utf-8'
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
            'filename': '',
            'maxBytes': 1024 * 1024 * int(max_bytes),  # 当达到50MB时分割日志
            'backupCount': backup_count,  # 备份份数
            'encoding': 'utf-8'
        },
        'warning': {
            'level': logging.WARNING,
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'formatter': 'standard',
            'filename': '',
            'maxBytes': 1024 * 1024 * int(max_bytes),  # 当达到50MB时分割日志
            'backupCount': backup_count,  # 备份份数
            'encoding': encoding,
        },
        'error': {
            'level': logging.ERROR,
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'formatter': 'standard',
            'filename': '',
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