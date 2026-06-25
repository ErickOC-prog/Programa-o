l=[]
while True:
    r1=int(input("Escolha uma opção:\n1-Adicionar compromisso\n2-Ver compromissos\n3-Filtrar\n4-Sair\nOpção:"))
    if r1==4:
        break
    elif r1==1:
        i1=input("Qual a data do livro(DD/MM/AAAA):\n")
        i2=input("Horario(HH:MM)\n")
        i3=input('Descrição para o compromisso:\n')
        i4=input("Local:\n")
        add={"data":i1, "horario":i2, "descrição":i3, "local":i4}
        l.append(add)

    elif r1==2:
        for c in l:
            print(f"Data:{c["data"]}\nHora:{c["horario"]}\nDescrição:{c["descrição"]}\nLocal:{c["local"]}")
    
    elif r1==3:
        q1=input("Qual o local que gostaria de procurar:")
        for c in l:
            if c["local"]==q1:
                print(f"Data:{c["data"]}\nHora:{c["horario"]}\nDescrição:{c["descrição"]}\nLocal:{c["local"]}")
    
    else:
        print("Opção incorreta")