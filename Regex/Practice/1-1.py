# 1-1 识别后续的字符串：bat、bit、but、hat、hit或者hut

import re


def p1_1(str):
    """
    >>> p1_1('gap')
    非法: gap
    >>> p1_1('hat')
    hat 符合规则
    >>> p1_1('bit')
    bit 符合规则
    """
    patt = '^[bh][aui]t'
    i = re.match(patt, str)
    if i is not None:
        print(i.group()+' 符合规则')
    else:
        print('非法: %s' % str)


if __name__ == '__main__':
    import doctest
    doctest.testmod()