def nomeCompleto():
    completo = lambda nome, sobrenome: nome + " " + sobrenome
    return completo
meunome = nomeCompleto()

print(meunome("Diego", "dos Santos"))