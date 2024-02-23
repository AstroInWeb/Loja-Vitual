from item_loja import Item
from pessoa_loja import Pessoa
from produto_loja import Produto 
from item_loja import Item

class Compra:
    def __init__(self, cliente:Pessoa):
        self.cliente = cliente
        self.itens = [] 
               
    def dump_compra(self):
        return (self.cliente, [item.dump_item() for item in self.itens])

    @staticmethod
    def load_compra(cliente, itens):
        compra = Compra(cliente)
        compra.itens = [Item.load_item(*item) for item in itens]
        return compra
    
    def Adicionar_produto(self, produto:Produto, quantidade:int ):

        item = Item(produto , quantidade)
        self.itens.append(item)
        print(f"Quantidade de produtos na compra: {len(self.itens)}\n")
    
    def Remover_produto(self, indice):
        self.itens.remove(self.itens[indice])
    
    def Atualizar_quantidade(self, indice:int, new_quant:int):
        self.itens[indice].copias = new_quant
    
    def Visualizar_compra(self):
        
        valor_total = 0
        indice =0
        if len(self.itens) == 0:
            print("Nao ha itens\n")
        else:
            for produto in self.itens:
                valor_total += (float(produto.produto_sendo_adquirido.preco) * float(produto.copias))
                print(f"nome: {produto.produto_sendo_adquirido.nome}\nvalor:{float(produto.produto_sendo_adquirido.preco)}\nvalor total do produto:{float(produto.produto_sendo_adquirido.preco) * float(produto.copias)}\nindice{indice}\n")
                indice+=1
            print(f"valor total: {valor_total}")
                
        