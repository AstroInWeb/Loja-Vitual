from LOJA import Loja
from produto_loja import Produto
from pessoa_loja import Pessoa
class App:
    def __init__(self):
        self.loja = Loja()
    
    def menu(self):
        
        opcao = 0
        print("1. Cadastrar produto\n")
        print("2. Ver lista de produtos\n")
        print("3. Ver detalhes de produto\n")
        print("4. Atualizar desconto de produto\n")
        print("5. Registrar aquisição de produto\n")
        print("6. Remover produto\n")
        print("7. Iniciar compra\n")
        print("8. Cancelar compra\n")
        print("9. Finalizar compra\n")
        print("10. Adicionar item na compra\n")
        print("11. Visualizar compra\n")
        print("12. Remover item da compra\n")
        print("13. Atualizar quantidade de item na compra\n")
        print("14. Relatório - Número de produtos\n")
        print("15. Relatório - Número de vendas\n")
        print("16. Relatório - Valor total vendido\n")
        print("17. Relatório - Valor médio das compras\n")
        print("18. Relatório - Número de usuários\n")
        print("19. Relatório - Usuário que mais fez compras\n")
        print("20. Relatório - 5 produtos mais caros\n")
        print("21. Relatório - 5 produtos mais vendidos\n")
        print("22. Relatório – Montante por pessoa\n")
        opcao  = input("Opção: ")
        
        if opcao == '1':
            nome = input("nome: ")
            codigo = input("codigo: ")
            preco = input("preco: ")
            categoria = input("categoria: ")
            produto = Produto(nome, codigo, preco, categoria)
            self.loja.inserir_produtos(produto)
            
        elif opcao == '2':
            indice =0
            for i in self.loja.produtos:
                print(f"codigo: {i.codigo},nome: {i.nome},preco: {i.Preco()},indice: {indice}")
                indice +=1
                
        elif opcao == '3':
            codigo = input("codigo: ")
            for i in  self.loja.produtos:
                if i.codigo == codigo:
                    print(f"{i.nome},{i.codigo},{i.preco},{i.quant_estoque},{i.desconto_percentual},{i.categoria},{i.Preco()}\n")
            pass
        elif opcao == '4':
            codigo = input("codigo: ")
            desconto = float(input("desconto: "))
            if desconto > 1.0 or desconto < 0.0:
                print("erro no desconto, digite um valor >=0 ou <=1\n")
                desconto = float(input("desconto: "))
            for i in  self.loja.produtos:
                if i.codigo == codigo:
                    i.desconto_percentual = desconto
            pass
        
        elif opcao == '5':
            codigo = input("codigo: ")
            quant = input("quantidade comprada: ")
            for i in  self.loja.produtos:
                if i.codigo == codigo:
                   i.quant_estoque = quant
                   return 1
            pass
        
        elif opcao == '6':
            codigo = input("codigo: ")
            for i in  self.loja.produtos:
                if i.codigo == codigo:
                   self.loja.produtos.remove(i)
                   return 1
            pass
        elif opcao == '7':
            nome =input("nome: ")
            email=input("email: ")
            cpf=input("cpf: ")
            cliente = Pessoa(nome, email,cpf)
            self.loja.Iniciar_compra(cliente)
            pass
        elif opcao == '8':
            
            self.loja.Cancelar_compra()
            return 1
        elif opcao == '9':
            self.loja.Finalizar_compra()
            self.loja.Salvar()
            pass
        elif opcao == '10':
            codigo = input("codigo: ")
            quant = input("quantidade: ")
            for i in  self.loja.produtos:
                if i.codigo == codigo: 
                  self.loja.compra_aberta.Adicionar_produto(i,quant)
            pass
        elif opcao == '11':
            if self.loja.compra_aberta != None:
             self.loja.compra_aberta.Visualizar_compra()
            else:
                print("Sem compras")
            pass
        elif opcao == '12':
            if self.loja.compra_aberta != None:
                indice = int(input("indice item: "))
                self.loja.compra_aberta.Remover_produto(indice)
            else:
                print("Sem compras")
            pass
        elif opcao == '13':
            indice = int(input("indice item: "))
            novaQauntidade = int(input("quantidade: "))
            self.loja.compra_aberta.Atualizar_quantidade(indice, novaQauntidade)
            pass
        elif opcao == '14':
            print(f"{self.loja.Número_de_produtos()}")
            pass
        elif opcao == '15':
            print(f"{self.loja.Número_de_vendas()}")
            pass
        elif opcao == '16':
            print(f"{self.loja.Valor_total_vendido()}")
            pass
        elif opcao == '17':
            print(f"{self.loja.Valor_médio_das_compras()}")
            pass
        elif opcao == '18':
            print(f"{self.loja.Número_de_usuários()}")
            pass
        elif opcao == '19':
            pessoa = self.loja.Usuário_que_mais_fez_compras()
            print(f"{pessoa.nome},{pessoa.email},{pessoa.cpf}")
            pass
        elif opcao == '20':
            produtos=self.loja.produtos_mais_caros()
            for p in produtos:
                print(f"{p.nome},{p.codigo},{p.preco},{p.categoria}")
            pass
        elif opcao == '21':
            self.loja.produtos_mais_vendidos()
            pass
        elif opcao == '22':
            self.loja.Compras_por_pessoa()
            pass
        else:
            print("Opcão invalid.")    
        
    
    def executar(self):
        while 1:
         self.menu()
         self.loja.Salvar()
         
        