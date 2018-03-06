
arq = open("testeAula.txt", "w")

arq.write("dsdsdsdsd Olá estou escrevendo no arquivo\n")
arq.write("Olá Diego estou escrevendo no arquivo denovo\n")
arq.close()

arq = open("testeAula.txt", "r")
lerArquivo = arq.read()
print(lerArquivo)
arq.close()

arq = open("testeAula.txt", "r")
lerArquivo = arq.readline()
print(lerArquivo)
lerArquivo2 = arq.readline()
print(lerArquivo2)
arq.close()

arq = open("testeAula.txt", "r")
lerArquivo = arq.readlines()
print(lerArquivo)
arq.close()

arq = open("testeAula.txt", "r")
for lin in arq.readlines():
    print(lin)
arq.close()