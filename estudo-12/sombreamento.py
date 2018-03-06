class Ponto():
    x = 25
    y = 75

p = Ponto()

print(p.x)
print(p.y)

p.x = 12
print(p.x)
print(Ponto.x)

del p.x
print(p.x)
