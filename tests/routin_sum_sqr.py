import time

s1, s2 = 0, 0


def as_sum(frm: int = 0, to: int = 100000):
    global s1
    for i in range(frm, to):
        s1 += i


def as_sqr(frm: int = 0, to: int = 100000):
    global s2
    for i in range(frm, to):
        s2 += i ** 2


def main():
    start = time.time()
    as_sum()
    as_sqr()
    print(s1 + s2, time.time() - start)


if __name__ == '__main__':
    main()  # 333333333300000 0.02808856964111328
