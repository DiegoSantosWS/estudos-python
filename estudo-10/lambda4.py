def inc(n):
    return lambda x: x + n

somar2  = inc(2)
somar15 = inc(15)

a = 4
b = somar15(a)

print(b)