# coding:utf-8
# author caturbhuja
# date   2020/11/24 2:43 下午
# wechat chending2012
import logging
from logging import config as log_config
import os
import inspect
from collections import namedtuple
from dlog.conf.split_by_maxBytes import ConfigCook  # todo 还有一个按照日期分割，暂时不测试了。
from dlog.decorator import with_metaclass, Singleton


class DLog(with_metaclass(Singleton)):
    def __init__(
            self, debug=False, singleton=False, log_dir_path=None, new_log_file_list=None, user_config=None, **kwargs
    ):
        """
        :param debug: debug模式
        :param singleton: 开启单例模式
        :param log_dir_path: 日志文件夹绝对路径
        :param new_log_file_list: 自添加新的日志文件类型，例如添加新日志 [{"file_name": "access", "log_level": "info"}, ]
        :param user_config: 用户自定义日志配置，适合高级用户使用。这个会覆盖原本日志配置。
        :param kwargs: 其他参数
        """
        path = os.path.dirname(inspect.stack()[2].filename)
        log_dir_path = log_dir_path or "{}{}logs".format(path, os.sep)
        self._check_dir_exists(log_dir_path)
        # 准备参数
        if user_config:
            self._final_config = user_config
        else:
            self._build_in_log_args = [
                {"file_name": "info", "log_level": "info"},
                {"file_name": "warning", "log_level": "warning"},
                {"file_name": "error", "log_level": "error"},
            ]
            if new_log_file_list is not None:
                if not isinstance(new_log_file_list, list):
                    raise TypeError("new_log_file_list must be list, now is type{}".format(type(new_log_file_list)))
                self._build_in_log_args.extend(new_log_file_list)
            self._final_config = ConfigCook.cook(
                only_console=False, debug=debug, file_list=self._build_in_log_args, log_dir_path=log_dir_path, **kwargs
            )
        self.log = self._cook_log(self._final_config)

    @staticmethod
    def _check_dir_exists(log_dir_path):
        if not os.path.exists(log_dir_path):
            os.mkdir(log_dir_path)

    def _cook_log(self, config: dict):
        log_config.dictConfig(config)
        log_name_list = [each["file_name"] for each in self._build_in_log_args]
        log_nt = namedtuple('log', log_name_list)
        log_nt_dict = dict()
        for each in self._build_in_log_args:
            file_name = logger_name = each["file_name"]
            log_level = each["log_level"]
            log_nt_dict[file_name] = getattr(logging.getLogger(logger_name), log_level)
        return log_nt(**log_nt_dict)

    @property
    def get_log(self):
        return self.log

    @property
    def show_log_config(self):
        return self._final_config
