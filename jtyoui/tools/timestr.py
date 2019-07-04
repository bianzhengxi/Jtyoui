#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/7/4 14:39
# @Author: Jtyoui@qq.com
import datetime


# 两个日期相减得差数
def plus_date(start: str, end: str, format_='%Y-%m-%d %H:%M:%S') -> datetime:
    """两个日期相减得差数
    :param start: 一个正确的日期
    :param end: 另一个正确的日期
    :param format_: 日期格式化
    :return: 被加后的日期
    """
    if '%H:%M:%S' in format_:
        if ':' not in start: start += ' 00:00:00'
        if ':' not in end: end += ' 00:00:00'
    start = datetime.datetime.strptime(start, format_)
    end = datetime.datetime.strptime(end, format_)
    plus = end - start
    return plus


# 一个日期加多少天或者时间
def add_day(date: str, format_='%Y-%m-%d', to_str=False, **kwargs) -> datetime:
    """一个日期加多少天或者时间
    :param date: 一个正确的日期
    :param format_: 日期格式化
    :param to_str: 是否打印字符串
    :param kwargs: 可以填写 :days=xx，seconds=xx,microseconds=xx,milliseconds=xx,minutes=xx,hours=xx,weeks=xx
    :return: 被加后的日期
    """
    start = datetime.datetime.strptime(date, format_)
    end = datetime.timedelta(**kwargs)
    if to_str:
        add = start + end
        return add.strftime(format_)
    return start + end


if __name__ == '__main__':
    p = plus_date(start='2018-02-01', end='2018-01-01')
    print(p.days)
    print(add_day(date='2018-02-01', days=-1, to_str=True))
