import matplotlib.pyplot as plt


def flash(w, h, n, a, b):
    if a == 0:
        n = 0 - int(n)
    if b == 1:
        plt.annotate("",
                     xy=(w, h + int(n)), xycoords='data',
                     xytext=(w, h), textcoords='data',
                     arrowprops=dict(arrowstyle="simple",
                                     connectionstyle="arc3", color="red"),
                     )
    if b == 2:
        plt.annotate("",
                     xy=(w + int(n), h), xycoords='data',
                     xytext=(w, h), textcoords='data',
                     arrowprops=dict(arrowstyle="simple",
                                     connectionstyle="arc3", color="red"),
                     )


def line():
    print("-----------------------------------------------------")


class RopadCompiler:
    def __init__(self):
        self.STR = ""
        self.codeS = {}
        self.NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.NUM = "0"

    def compile(self):
        _STRC = ""
        for _D in self.STR:
            if _D in self.codeS.keys():
                if self.NUM == "0":
                    self.NUM = "1"
                _STRC = _STRC + self.codeS[_D] * int(self.NUM)
            elif _D in self.NUMS:
                self.NUM = self.NUM + _D
            elif _D == '(' or _D == ')':
                continue
            else:
                if self.NUM == "0":
                    self.NUM = "1"
                _STRC = _STRC + int(self.NUM) * _D
                self.NUM = "0"
        return _STRC
