from compra_loja import Compra
from produto_loja import Produto
from pessoa_loja import Pessoa
from item_loja import Item
import pickle
class Loja:
    def __init__(self):
        self.produtos =[]
        self.compras = []
        self.compra_aberta = None
    
    def Iniciar_compra(self, cliente:Pessoa):
        compra = Compra(cliente)
        if self.compra_aberta == None:
         self.compra_aberta = compra
        else:
            print("erro, compra ja aberta\n")
        
    def inserir_produtos(self, produto: Produto):
        self.produtos.append(produto)
    
    def inserir_compra(self, compra:Compra):
        self.compras.append(compra)
    
    def remover_produto(self, produto: Produto):
        indice = 0
        for produtor in self.produtos:
            if produto.codigo == produtor.codigo:
               self.produtos.remove[ self.produtos[indice]]
            indice +=1
            
    def remover_compra(self, compra:Compra):
        indice = 0
        for comprar in self.compras:
            if compra.codigo == comprar.codigo:
               self.compras.remove[ self.compras[indice]]
            indice +=1
    
    
    def Buscar_produto(self, codigo:str):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
            
        return None
        
    def Cancelar_compra(self):
        self.compra_aberta = None
        
    def Finalizar_compra(self):
        self.compras.append(self.compra_aberta)
        self.compra_aberta = None
        
    def Número_de_produtos(self):
        return len(self.produtos)
        
    def Número_de_vendas(self):
        return len(self.compras)
        
    def Valor_total_vendido(self):
        total =0
        for i in self.compras:
            total += i.custos()
        return total
    def Valor_médio_das_compras(self):
        total =0
        for i in self.compras:
            total += i.custos()
        return (total/len(self.compras))
    def Número_de_usuários(self):
        usuario = []
        for i in self.compras:
            usuario.append(i.cliente)
            for a in usuario:
                if i.cliente == a:
                    usuario.remove(i.cliente)
                    
        return len(usuario)
            
                    
        
    def Usuário_que_mais_fez_compras(self):
        mais_comprou = Pessoa(None,None,None)
        quant_compras_mais_comprou = 0
        quant_compras =0
        for a in self.compras:
            for b in self.compras:
                if a.cliente == b.cliente:
                    quant_compras +=1
            if quant_compras > quant_compras_mais_comprou:
                quant_compras_mais_comprou =quant_compras
                mais_comprou = a.cliente
        return mais_comprou
     
    def produtos_mais_caros(self):
        produtos = []
        valor_mais_caro = 0
        produto_mias_caro = None
        for a in range(0,len(self.produtos)):
            for b in self.produtos:
                if b in produtos:
                    continue
                elif b.preco > valor_mais_caro:
                    valor_mais_caro = b.preco
                    produto_mias_caro = b
            produtos.append(produto_mias_caro)
        
        return produtos
        
     
    def produtos_mais_vendidos(self):
        produtos = []
        quant = []
        valor = []
        produtos_ordem = []
        quant_ordem = []
        valor_ordem =[]
        produto_maior = None
        quant_maior =0
        for a in self.compras:
            for b in a.itens:
                if b.produto_sendo_adquirido in produtos:
                    quant[produtos.index(b.produto_sendo_adquirido)] += b.copias
                else:
                    produtos.append(b.produto_sendo_adquirido)
                    quant.append(b.copias)
                    valor.append(b.produto_sendo_adquirido.preco)
                    
        for c in range(0,len(produtos)):
            for d in produtos:
                if d in produtos_ordem:
                    continue
                elif quant[produtos.index(d)] > quant_maior:
                    quant_maior = quant[produtos.index(d)]
                    produto_maior = d
            produtos_ordem.append(produto_maior)
            quant_ordem.append(quant_maior)
            valor_ordem.append(valor[produtos.index(produto_maior)])
        indicex=0
        if len(produtos_ordem) < 5:
            for s in produtos_ordem:
                print(f"{produtos_ordem.nome},{produtos_ordem.codigo},{quant_ordem[indicex]*valor_ordem[indicex]}")
                indicex +=1
        else:
            for x in range(0,5):
                print(f"{produtos_ordem[x].nome},{produtos_ordem[x].codigo},{quant_ordem[x]*valor_ordem[x]}")
            
                
        
    def Compras_por_pessoa(self):
        pass
    def Salvar(self):
        arquivop = open("LojaVirtual/produtos.bin","wb")
        arquivoc = open("LojaVirtual/compras.bin","wb")
        for p in self.produtos:
            pickle.dump(p,arquivop)
        for c in self.compras:
            pickle.dump(c,arquivoc )
    def Carregar(self):
        arquivop = open("LojaVirtual/produtos.bin","rb")
        arquivoc = open("LojaVirtual/compras.bin","rb")
        while True:
            try:
                objp = pickle.load(arquivop)
                self.produtos.append(objp)
            except EOFError:
             break
         
        while True:
            try:
                self.compras.append(pickle.load(arquivoc))
            except EOFError:
             break