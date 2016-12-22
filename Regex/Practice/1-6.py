# 1-6 匹配以"www"起始并以".com"（或edu net等其他高级域名）结尾的简单web域名
# eg. http://www.yahoo.com/ http://www.foothill.edu/


import re


def p1_6(str):
    """
    >>> p1_6('http://www.yahoo.com/')
    http://www.yahoo.com/
    yahoo.com
    >>> p1_6('www.yahoo.com')
    www.yahoo.com
    yahoo.com
    >>> p1_6('http://www.foothill.edu/')
    http://www.foothill.edu/
    foothill.edu
    >>> p1_6('www.foothill.edu/')
    www.foothill.edu/
    foothill.edu
    >>> p1_6('http://alex.edu')
    0
    """
    # patt = r'^(?:http://|https://)?www.((?:/w+.)+(?:com|edu|org|net|gov))/?$' 搞错了斜线方向，忘记对"."进行转义!
    patt = r'^(?:http://|https://)?www\.((?:\w+\.)+(?:com|edu|org|net|gov))/?$'
    i = re.match(patt, str)
    if i is not None:
        print(i.group())
        print(i.group(1))
    else:
        print('0')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
