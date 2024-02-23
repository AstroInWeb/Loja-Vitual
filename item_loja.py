from produto_loja import Produto

class Item:
    def __init__(self, produto_sendo_adquirido:Produto, copias:int):
        self.produto_sendo_adquirido = produto_sendo_adquirido
        self.copias = copias
        
    def dump_item(self):
        return (self.produto_sendo_adquirido, self.copias)

    @staticmethod
    def load_item(produto, quantidade):
        return Item(produto, quantidade)
"""     
    def custo(lista:list ):
        custo = 0.0
        for i in lista:
            custo += float(i.preco * i.copias)
        print(f"{float(i.produto_sendo_adquirido.preco * i.copias)}")
        return custo """