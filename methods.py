import matplotlib.pyplot as plt


def flash(w, h, n, a, b, rc, rn):
    if a == 0:
        n = 0 - int(n)
    if b == 1:
        plt.annotate("",
                     xy=(w, h + int(n)), xycoords='data',
                     xytext=(w, h), textcoords='data',
                     arrowprops=dict(arrowstyle="simple",
                                     connectionstyle="arc3"),
                     )
    if b == 2:
        plt.annotate("",
                     xy=(w + int(n), h), xycoords='data',
                     xytext=(w, h), textcoords='data',
                     arrowprops=dict(arrowstyle="simple",
                                     connectionstyle="arc3"),
                     )
