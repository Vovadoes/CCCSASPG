import math

# from Charts import *


# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


def myround(x: float, lst: list):
    for i in lst:
        if x < i:
            return i
    return lst[-1]


class Calculation:
    def __init__(self, n: int, m: int, lst: list, U: float, nl: float, cos_fi: float, P_kpd: float,
                 q: float):
        P_i = P_kpd / n

        lst_P = []
        for i in range(m):
            lst_P.append(lst[i][1] * P_i)
        print(f"{lst_P=}")

        lst_I = []
        for i in range(m):
            lst_I.append(lst_P[i] / (U * cos_fi))
        print(f"{lst_I=}")

        dU = nl * U * 10
        print(f"{dU=}")

        lst_R = []
        for i in range(m):
            lst_R.append(dU / lst_I[i])
        print(f"{lst_R=}")

        lst_S = []
        for i in range(m):
            lst_S.append(q * lst[i][2] / lst_R[i])
        print(f"{lst_S=}")

        self.lst_S = [myround(lst_S[i], [35, 50, 70, 95, 120, 150, 185, 240]) for i in range(len(lst_S))]
        print(f"{self.lst_S=}")


if __name__ == "__main__":
    n = 96
    m = 7
    lst = [
        ["1", 62, 350],
        ["2", 34, 390],
        ["3", 12, 120],
        ["4", 18, 172],
        ["5", 20, 200],
        ["6", 8, 80],
        ["7", 14, 120],
    ]
    U = 0.4
    nl = 5
    cos_fi = 0.95
    P_kpd = 80
    q = 0.028
    calculation = Calculation(n, m, lst, U, nl, cos_fi, P_kpd, q)

    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
