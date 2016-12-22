# 匹配所有有效的Python标识符的集合

import re


def p1_4(str):
    """
    >>> p1_4('alexryan')
    alexryan
    >>> p1_4('alex ryan')
    0
    >>> p1_4('alex_ryan')
    alex_ryan
    >>> p1_4('__alexryan95')
    __alexryan95
    >>> p1_4('_alexryan')
    _alexryan
    >>> p1_4('9alexryan')
    0
    >>> p1_4('**alex')
    0
    """
    patt = '^[_a-zA-Z]{1,2}\w*$'
    i = re.match(patt, str)
    if i is not None:
        print(i.group())
    else:
        print('0')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
