# coding:utf-8
# author caturbhuja
# date   2020/11/25 2:33 下午 
# wechat chending2012
"""
-------------------------------------------------
   Description:  单例模式
   Author:       Caturbhuja
   date:         2020/8/31
   WeChat:       chending2012
-------------------------------------------------
   Change Activity:
       2020/8/31:   DB工厂类创建

-------------------------------------------------
"""
__author__ = 'Caturbhuja'


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""

    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class MetaClass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    # 直接指定 bases 为空，忽略 MixinFunction ，实现 MixinFunction 作为IDLE提示
    return type.__new__(MetaClass, 'temporary_class', (), {})


class Singleton(type):
    """
    Singleton Metaclass
    """
    _inst = dict()

    def __call__(cls, *args, **kwargs):
        singleton = kwargs.get("singleton", False)
        if singleton:
            if "singleton" not in cls._inst:
                cls._inst["singleton"] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._inst["singleton"]
        else:
            return super(Singleton, cls).__call__(*args, **kwargs)
