n=int(input())

fv=1
dec=0
def bin_dec(n):
    global dec
    global fv
    dec=dec +fv*(n%10)
    n=n//10
    fv=fv*2
    if n>0:
        bin_dec(n)


bin_dec(n)
print(dec)