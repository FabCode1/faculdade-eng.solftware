def menu():
    print("1- Incluir contato e telefone")
    print("2- Alterar um telefone de um contato")
    print("3- Excluir um telefone de um contato")
    print("4-Consultar os telefones de um contato")
    print("5- Listar todos os contatos e seus respectivos telefones ")
    print('6 – FIM')


def alterar_telefone(Agenda):
    contato = input("Nome do contato:") 
    if contato in Agenda:
        for i in range(len(Agenda)):
            if Agenda[i]== contato:
                Indice_contato = i
                Indice_telefone = i+1
                telefones = Agenda[Indice_telefone]
                
                i2=1
                for numero in  range (len(telefones)):
                    print(f'{i2}:{telefones[numero]}')
                    i2+=1
                print("Qual Telefone que deseja alterar?")
                opc=int(input("opção:"))    
                novo_numero = input("Novo numero:")
                telefones[opc -1]= novo_numero
    else:
        return 0
    return Agenda


def excluir_telefone(Agenda):
    contato = input("Nome do contato:") 
    if contato in Agenda:
        for i in range(len(Agenda)):
            if Agenda[i]== contato:
                Indice_contato = i
                Indice_telefone = i+1
                telefones = Agenda[Indice_telefone]
                
                i2=1
                for numero in  range (len(telefones)):
                    print(f'{i2}:{telefones[numero]}')
                    i2+=1
                print("Qual Telefone que deseja Exluir?")
                opc=int(input("opção:"))    
                del telefones[opc -1]
    else:
        return 0
    return Agenda 
        

    
def adicionar_contato(Agenda):
    flag = True
    i = 1
    while flag:
        contato = input(f"Nome do contato {i}: ")
        if contato == '':
            flag = False
        else:
            if contato in Agenda:
                print("O contato já existe!")
                i -= 1
            else:
                numeros = []
                flag2 = True
                i2 = 1

                while flag2:
                    numero = input(f"Número de telefone {i2}: ")
                    if numero == '':
                        flag2 = False
                    else:
                        numeros.append(numero)
                    i2 += 1
                Agenda.append(contato)
                Agenda.append(numeros)

        i += 1


def consultar_telefone(Agenda):
    contato = input("Nome do contato:") 
    if contato in Agenda:
        for i in range(len(Agenda)):
            if Agenda[i]== contato:
                Indice_contato = i
                Indice_telefone = i+1
                telefones = Agenda[Indice_telefone]
                print(f"\nTelefones de {contato}")
                i2=1
                for numero in  range (len(telefones)):
                    print(f'Telefone {i2}:{telefones[numero]}')
                    i2+=1             
                
    else:
        return 0
    return Agenda 
                    
                    
                

def mostrar_contatos(Agenda):
    for i in range(0, len(Agenda), 2):
        nome = Agenda[i]
        telefones = Agenda[i + 1]
        i2=1
        print(f"{nome}:")
        for numero in telefones:
            print(f"{i2}-{numero}")
            i2+=1
        


#Programa principal ===========================================================

        
Agenda=['Contato 1', ['99876-5645','98798-3244'], 'Contato 2',['99786-5531'], 'Contato N',
        ['99654-1123', '99874-5532 ', '99874-8879' ]]

if Agenda == []:
    print("Agenda vazia!\n")
else:
    print(f"\nAgenda:{Agenda}\n")



programa= True
while programa:
    opc = int(input('\nOpção:'))
    menu()
    if opc == 1:
        adicionar_contato(Agenda)
    elif opc == 2:
        Nova_Agenda = alterar_telefone(Agenda)
        if Nova_Agenda == 0:
            print("Contato não encontrado")
        else:
            print(f"\n{Nova_Agenda}")
            print("Contato modificado com sucesso!")
    elif opc == 3:
        Nova_Agenda = excluir_telefone(Agenda)
        if Nova_Agenda == 0:
            print("Contato não encontrado")
        else:
            print(f"\n{Nova_Agenda}")
            print("Contato excluido com sucesso!")
    elif opc == 4:
        Mostrar = consultar_telefone(Agenda)
        if Mostrar == 0:
            print("Contato não encontrado")
    elif opc == 5:
        Todos_contatos =mostrar_contatos(Agenda)
    elif opc == 6:
        programa= False 
        



















    
