n = int(input())

# bin = 0
# fv = 1
# while n > 0:
#     bin = bin + fv * (n % 2)
#     n = n // 2
#     fv = fv * 10
#
# print(bin)


def dec_bin(m):
    if m>1:
        dec_bin(m//2)
    print(m%2, end='')


dec_bin(n)