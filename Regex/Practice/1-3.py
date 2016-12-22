# 1-3 匹配由单个逗号和单个空白符分隔的任何单词或单个字母，如姓氏的首字母

import re


def p1_3(str):
    """
    >>> p1_3('Ryan, Alex')
    Ryan, Alex
    >>> p1_3('Ryan Alex')
    0
    >>> p1_3('A,d3')
    0
    >>> p1_3('muller, thomas')
    muller, thomas
    """
    patt = '^[a-zA-Z]+, [a-zA-Z]+$'
    i = re.match(patt, str)
    if i is not None:
        print(i.group())
    else:
        print('0')

if __name__ == '__main__':
    import doctest
    doctest.testmod()