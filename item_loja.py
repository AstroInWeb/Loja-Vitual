from produto_loja import Produto

class Item:
    def __init__(self, produto_sendo_adquirido:Produto, copias:int):
        self.produto_sendo_adquirido = produto_sendo_adquirido
        self.copias=copias
    
    def custo(self):
        custos = self.produto_sendo_adquirido.preco * self.copias
        return custos