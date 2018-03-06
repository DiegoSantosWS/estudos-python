class Documento():
    def __init__(self, nome):
        self.nome = nome

    def abrir(self):
        raise NotImplementedError("O metodo abrir deve ser implementado na sub-classe")

class Pdf(Documento):
    def abrir(self):
        return 'Foi aberto um pdf'

class Doc(Documento):
    def abrir(self):
        return 'Foi aberto um doc'

class Xls(Documento):
    def abrir(self):
        pass

documentos = [Pdf("a.pdf"), Pdf("b.pdf"), Doc("a.doc"), Xls("a.xls")]

for doc in documentos:
    print(doc.abrir(), "de nome", doc.nome)