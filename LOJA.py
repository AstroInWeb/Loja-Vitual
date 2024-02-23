from compra_loja import Compra
from produto_loja import Produto
from pessoa_loja import Pessoa
from item_loja import Item
import pickle
import os
endereco = "/home/gabriel/Área de Trabalho/Loja-Vitual"

class Loja:
    def __init__(self):
        self.produtos = []
        self.compras = []
        self.compra_aberta = None

    def cadastrar_produto(self):
        nome = input("nome: ")
        codigo = input("codigo: ")
        preco = float(input("preco: "))
        categoria = input("categoria: ")
        produto = Produto(nome, codigo, preco, categoria)
        self.produtos.append(produto)
        self.Salvar()

    def lista_produtos(self):
        for i in self.produtos:
            print(f"codigo: {i.codigo},nome: {i.nome},preco: {i.Preco()}\n")
        
    def detalhes_produtos(self):
        codigo = input("codigo: ")
        for i in  self.produtos:
            if i.codigo == codigo:
                print(f"nome:{i.nome}\ncodigo:{i.codigo}\npreco:{i.preco}\nestoque:{i.quant_estoque}\ndesconto:{i.desconto_percentual}\ncategoria;{i.categoria}\n")
        
    def imprimir_clientes(self):
         for c in self.compras:
            print(f"{c.cliente}\n")

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
                return 1
            
        return 0
        
    def Cancelar_compra(self):
        if self.compra_aberta == None:
            print("Não ha compra aberta no momento\n")
        else:
            self.compra_aberta = None
        
    def Finalizar_compra(self):
        if self.compra_aberta == None:
            print("Não ha compra aberta no momento\n")
        else:
            self.compras.append(self.compra_aberta)
            self.compra_aberta = None
            print("compra finalizada\n")

        self.Salvar()
        print(f"{self.compras[0].cliente}\n")
        
    def Número_de_produtos(self):
        return len(self.produtos)
        
    def Número_de_vendas(self):
        return len(self.compras)
        
    def Valor_total_vendido(self):
        total = 0
        for i in self.compras:
            for x in i.itens:
               preco = float(x.produto_sendo_adquirido.preco )
               total += preco * float( x.copias)

        return total
    
    def Valor_médio_das_compras(self):
        total = 0
        for i in self.compras:
            for x in i.itens:
               preco = float(x.produto_sendo_adquirido.preco )
               total += preco * float( x.copias)
        return (total/float(len(self.compras)))
    
    def Número_de_usuários(self):
        usuario = []

        for i in self.compras:
            if i.cliente not in usuario:
                usuario.append(i.cliente)
            """ for a in usuario:
                if i.cliente == a:
                    usuario.remove(i.cliente) """
                    
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
            
                
    def verifica_produto_salvo(self):

        arquivop = open(endereco+"/produtos.bin","rb")
        objp = pickle.load(arquivop)
        print(f"{objp.type()}\n")
        
    
    def Compras_por_pessoa(self):
        for x in self.compras:
            print(f"\n{x.cliente.nome}, {len(x.itens)} itens")
            for y in x.itens:
                print(f"{y.produto_sendo_adquirido.nome}, {y.copias}")

        print("\n")


        

    def Salvar(self):

        with open("arquivos/produtos.bin","wb") as arquivop:
            pickle.dump([a.dump_produto() for a in self.produtos ],arquivop)
            arquivop.close()

        # Salvar a compra em um arquivo binário
        with open('arquivos/compras.pickle', 'wb') as arquivoc:
             pickle.dump([compra.dump_compra() for compra in self.compras], arquivoc)
             arquivoc.close()

    def Carregar(self):
        if not os.path.exists('arquivos/compras.pickle'):
            open('arquivos/compras.pickle', 'w').close()

        with open("arquivos/produtos.bin","rb") as arquivop:
            """ if EOFError:
                print("arquivo inexixtente\n")
                pass
            else : """
            self.produtos = [Produto.load_produto(*x) for x in pickle.load(arquivop)]
            arquivop.close()


        # Carregar a compra de um arquivo binário
        with open('arquivos/compras.pickle', 'rb') as arquivoc:
            """ if FileNotFoundError:
                print("arquivo inexixtente\n")
                pass
            else : """
            self.compras = [Compra.load_compra(*compra) for compra in pickle.load(arquivoc)]
            arquivoc.close()
                 

