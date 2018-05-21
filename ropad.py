# به نام خداوند ویروس گارد


import matplotlib.pyplot as plt
import methods as m

# چرخه ی ورود روپاد
while 1:
    # دریافت مبدا
    _orgX = input("lotfan tool mabda ra vared konid: ")
    _orgY = input("lotfan arz mabda ra vared konid: ")

    # دریافت دستور های ترکیبی
    _codeS = {}
    while 1:
        _temp = input("dar soorat tamayol be vared kardan dastoor tarkibi, name dastoor ra vared konid: \n "
                      "1:namikhaham dastoor jadid vared konam. \n")
        if _temp == "1":
            break
        else:
            _codeS[_temp] = input("code dastoor tarkibi ra vared konid: ")

    # دریافت دستور های اصلی
    _string = input("code dastoor asli ra vared konid: ")

    # تعریف متغیر های اولیه
    _width = int(_orgX)
    _height = int(_orgY)
    _heightS = [_height]
    _widthS = [_width]
    _num = "0"

    # ساده کردن دستور وارد شده
    RC = m.RopadCompiler
    RC.STR = _string
    RC.codeS = _codeS
    RC.NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    RC.NUM = "0"
    _string = RC.compile(RC)

    # محاسبه و رسم بردار ها
    for i in _string:
        if i == "N":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 1, 1)
            _height += 1 * int(_num)
            _num = "0"

            _heightS.append(_height)
            _widthS.append(_width)
            continue
        if i == "S":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 0, 1)
            _height -= 1 * int(_num)
            _num = "0"
            _heightS.append(_height)
            _widthS.append(_width)
            continue
        if i == "W":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 0, 2)
            _width -= 1 * int(_num)
            _num = "0"
            _heightS.append(_height)
            _widthS.append(_width)
            continue
        if i == "E":
            if _num == "0":
                _num = 1
            m.flash(_width, _height, _num, 1, 2)
            _width += 1 * int(_num)
            _num = "0"
            _heightS.append(_height)
            _widthS.append(_width)
            continue

    # رسم مسیر اصلی
    plt.plot(_widthS, _heightS)

    # خروجی مختصات
    print(_width)
    print(_height)
    print(_widthS)
    print(_heightS)
    plt.text(_width, _height, r'$\vert\stackrel{%d}{%d}$' % (_width, _height))

    # روپاد جدید
    a = input("ropad jadid mikhahid? \n 1:bale  2:kheir")
    if a == "2":
        break
# نمایش پلات
plt.show()
