"""
Lista de compras em python
"""

lista_compras = [''] #Cria uma lista
lista_compras.pop() #Apaga o índice zerado

while True: #Executa um looping
    print('Selecione uma opção ') #Print de início de programa
    select = input('[i]nserir [a]pagar [l]istar: ') #Opções para selecionar

    if select == 'i': #Se digitado i (inserir valor)
        lista_compras.append(input('Valor: ')) #Digitar o valor

    elif select == 'a': #Se digitado a (apagar valor)
        try: #Tenta
            apagar = int(input('Escolha o índice para apagar: ')) #Digitar valor
            del lista_compras[apagar] #Apaga o índice 
        except IndexError: #Exceto se tiver erro de index
            print('Este índice não existe') #Print para informar o erro
    
    elif select == 'l': #Se digitado l (listar valor)
        if lista_compras == []: #Se a lista de compras estiver vazia, retorna que está vazia
            print('Nada para listar.') #Print informando lista vazia
        else:
            for indice in enumerate(lista_compras): #Retorna a lista de compra
                print(indice) #Print informando a lista

    else:
        print('Não entendi, pode repetir pf') #Se digitado algo fora do i, a, l