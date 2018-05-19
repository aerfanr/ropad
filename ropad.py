# به نام خداوند ویروس گارد

# about:
#   developed by aer

import matplotlib.pyplot as plt
import methods as m

while 1:
    _orgX = input("lotfan tool mabda ra vared konid: ")
    _orgY = input("lotfan arz mabda ra vared konid: ")
    _string = input("code ra vared konid: ")

    _width = int(_orgX)
    _height = int(_orgY)
    _heightS = [_height]
    _widthS = [_width]
    _num = "0"
    rN = 0
    rC = ["r", "b", "g", "y", "p"]

    for i in _string:
        if i == "N":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 1, 1, rC, rN)
            _height += 1 * int(_num)
            _num = "0"

            _heightS.append(_height)
            _widthS.append(_width)
            continue
        if i == "S":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 0, 1, rC, rN)
            _height -= 1 * int(_num)
            _num = "0"
            _heightS.append(_height)
            _widthS.append(_width)
            continue
        if i == "W":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 0, 2, rC, rN)
            _width -= 1 * int(_num)
            _num = "0"
            _heightS.append(_height)
            _widthS.append(_width)
            continue
        if i == "E":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 1, 2, rC, rN)
            _width += 1 * int(_num)
            _num = "0"
            _heightS.append(_height)
            _widthS.append(_width)
            continue
        else:
            if i == "(" or i == ")":
                continue
            _num = _num + i

    plt.plot(_widthS, _heightS, rC[rN] + "-o")
    rN += 1

    print(_width)
    print(_height)
    print(_widthS)
    print(_heightS)
    plt.text(_width, _height, r'$\vert\stackrel{%d}{%d}$' % (_width, _height))

    a = input("ropad jadid mikhahid? \n 1:bale  2:kheir")
    if a == "2":
        break
plt.show()
