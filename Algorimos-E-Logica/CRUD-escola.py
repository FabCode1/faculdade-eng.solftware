def menu():
    print('1-Cadastrar turma')
    print('2- Cadastrar aluno')
    print('3-remover aluno')
    print('4- Alunos com maior media')
    print('5-Fim')


#escola[[turma[[aluno[notas]]]
#escola[i][j][0]

def descobre_indice(Disciplinas, nome_diciplina):
    encontrada = False
    indice = -1
    for i in range(len(Disciplinas)):
        if nome_diciplina == Disciplinas[i]:
            indice = i
            encontrada= True
    if encontrada:
        return indice
    else:
        
        
        print('A matéria não foi encontrada!')
    

    
def Cadastrar_turma(Disciplinas, Escola, nome_diciplina):
    Disciplinas.append(nome_diciplina)
    Escola.append([])
    cadastrar_aluno(Escola, Disciplinas, nome_diciplina)
    return Escola
    


def cadastrar_aluno(Escola, Disciplinas, nome_diciplina):
    indice = descobre_indice(Disciplinas, nome_diciplina)
    
    lista_aluno=[]
    nome_aluno= input(f'Escreva o nome do aluno para adicionar a {nome_diciplina}')
    encontrado = False
    for aluno in range (len(Escola[indice])):
        if nome_aluno == (Escola[indice][aluno][0]):
                          
                          encontrado=True

    if encontrado:
        idade_aluno= int(input('idade do aluno'))
        flag=True
        notas =[]
        while flag:
            notas_do_aluno = float(input('Nota do aluno(-1 para parar):'))
            if notas_do_aluno == -1:
                flag = False
            else:
                notas.append(notas_do_aluno)
        lista_aluno.append(nome_aluno)
        lista_aluno.append(idade_aluno)
        lista_aluno.append(notas)

        Escola[indice].append(lista_aluno)
        return Escola
    else:
        return 0

    

def remover_aluno(Disciplinas, Escola, Nome_do_aluno, nome_diciplina ):
    indice_diciplina = descobre_indice(Disciplinas, nome_diciplina)
    indice_aluno= -1
    encontrado=False
    for aluno in range (len(Escola[indice_diciplina])):
        if Nome_do_aluno == Escola[indice_diciplina][aluno][0]:
                          indice_aluno=aluno
                          encontrado = True
    if encontrado:
        del Escola[indice_diciplina][indice_aluno]
        return Escola
    else:
        return 0


def media(Escola,Disciplinas):
    maior = float('-inf')
    Alunos_maior_media = []
    for turma  in range(len(Escola)):
         for aluno in Escola[turma]:
             media = sum(aluno[2])/len(aluno[2])
             if media > maior:
                 maior = media
                 Alunos_maior_media = [{
                    "nome": aluno[0],
                    "idade": aluno[1],
                    "disciplina": Disciplinas[turma],
                    "notas": aluno[2],
                    "media": media
                }]

                 #era possivel tb usar lista (minha ideia incial)
                 #Alunos_maior_media = [[Disciplinas[turma], aluno[0], aluno[1], notas, media_aluno]]
             elif media == maior:
                 
                 Alunos_maior_media.append({
                    "nome": aluno[0],
                    "idade": aluno[1],
                    "disciplinas": Disciplinas[turma],
                    "notas": aluno[2],
                    "media": media})
                 

    return Alunos_maior_media




#Programa principal=====================================================================


Disciplinas=['Algoritmos e Programação', 'Segurança']

Escola=[
[ ['André Coelho', 19, [7.5, 9.2, 8.9, 6.0]],
  ['Rebeca Farias', 20, [9.5, 7.8]] ],

[ ['    Tiago Silva', 19, [4.5, 6.1, 7.4]],
  ['Bárbara Andrade', 18, [5.0, 8.2, 7.6]] ]
]



flag = True 
while flag:
    opc = int(input("Opção:"))
    menu()
    if opc == 1:
        print('===Nova turma!===')
        nome_diciplina= input('Nome da nova diciplina:')
        descobre_indice(Disciplinas, nome_diciplina)
        Cadastrar_turma(Disciplinas, Escola, nome_diciplina)
    elif opc ==2:
        print('===Novo aluno!===')
        nome_diciplina= input('Nome da diciplina:')
        descobre_indice(Disciplinas, nome_diciplina)
        Novo =cadastrar_aluno(Escola, Disciplinas, nome_diciplina)
        if Novo == 0:
            print("aluno não encontrado")
        else:
            print('Aluno cadastrado com sucesso')
    elif opc ==3:
        print('=====Remova diciplina=====')
        Disciplinas=['Algoritmos e Programação', 'Segurança']
        nome_diciplina= input('Nome da diciplina:')

        indice = descobre_indice(Disciplinas, nome_diciplina)
        if indice >= 0:
            Nome_do_aluno= input('Nome do aluno que deseja remover:')
            remover_aluno(Disciplinas, Escola, Nome_do_aluno, nome_diciplina)

    elif opc == 4:
        dados = media(Escola,Disciplinas)
        print('\n')
        for info in dados:
            for chave, dado in info.items():
                print(f'{chave}:{dado}')
    elif opc == 5:
        print(Disciplinas)
        print(Escola)
        flag=False
    else:
        print('opção invalida')




