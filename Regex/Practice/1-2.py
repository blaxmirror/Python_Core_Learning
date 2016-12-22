# 1-2 匹配由单个空格分割的任意单词对，也就是姓和名

import re


def p1_2(str):
    """
    >>> p1_2('Alex Ryan')
    Alex Ryan
    >>> p1_2('2gether forever')
    0
    >>> p1_2('Thomas Muller')
    Thomas Muller
    """
    patt = '^[a-zA-Z]+ [a-zA-Z]+$'
    i = re.match(patt, str)
    if i is not None:
        print(i.group())
    else:
        print('0')


if __name__ == '__main__':
    import doctest
    doctest.testmod()