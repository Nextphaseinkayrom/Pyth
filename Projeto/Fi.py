tarefas = []
while True:
 print("""
Olá oque você deseja
 1 - Criar tarefa
  2 - Vizualizar tarefas criadas
   3 - Modificar alguma tarefa 
    4 - Excluir alguma tarefa\n
     Qualquer numero - Sair""")

 pergunta_menu = int(input('. . .?'))

 if pergunta_menu == 1:
    print('Qual tarefa você deseja criar?')
    perg = input('. . .?')
    if perg:
        tarefas.append(perg)
        print('Tarefa adicionada com sucesso')
        continue

 elif pergunta_menu == 2:
     print(f'As tarefas no momentos são {tarefas}\n')

 elif pergunta_menu == 3:
     if tarefas:
         print(f'Tarefas no momento {tarefas}')
     else:
         print('Nada de tárefas até agora')
         continue

     pergunta_mod = input('. . .?')
     if pergunta_mod in tarefas:
         print('Tarefa encontrada')
         indice = tarefas.index(pergunta_mod)
         pergunta_mod2 = input('Digite oque deseja por no lugar')
         tarefas[indice] = pergunta_mod2
         print(f'Deu certo sua nova tarefa é {pergunta_mod2}')
     else:
         print('Tarefa Não encontrada')
         continue

 elif pergunta_menu == 4:
     print(tarefas)
     pergunta_rem = input('Qual item deseja remover')
     if pergunta_rem in tarefas:
        print('Tarefa encontrada\nRemovendo-a')
     tarefas.remove(pergunta_rem)
     print(f'Tárefa removida agora restou\n{tarefas}')


 else:
     print('Finalizando sistema . . .')
     break


