# coding:utf-8
# author caturbhuja
# date   2020/11/25 2:43 下午
# wechat chending2012
from dlog.logger import DLog

__version__ = '1.0.3'


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


VERSION = tuple(map(int_or_str, __version__.split('.')))

__all__ = [
    'DLog',
]
