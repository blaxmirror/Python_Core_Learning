# 1-5 根据读者当地的格式，匹配街道地址（足够灵活来匹配任意数量的街道单词，包括类型名称）
# 美国街道地址格式：1180 Bordeaux Drive
# 足够灵活可以匹配诸如：3120 De la Cruz Boulevard

import re


def p1_5(str):
    """
    >>> p1_5('1180 Bordeaux Drive')
    1180 Bordeaux Drive
    1180
    Bordeaux Drive
    >>> p1_5('123 The 23rd Avenue')
    123 The 23rd Avenue
    123
    The 23rd Avenue
    >>> p1_5('23rd downtown')
    0
    >>> p1_5('3120 De la Cruz Boulevard')
    3120 De la Cruz Boulevard
    3120
    De la Cruz Boulevard
    >>> p1_5('downtown')
    0
    """
    # 美式街道
    patt = '^(\d+)\s+((?:\w+ )*\w+)$'
    i = re.match(patt, str)
    if i is not None:
        print(i.group())
        print(i.group(1))
        print(i.group(2))
    else:
        print('0')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
