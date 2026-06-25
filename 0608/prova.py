l=[

]

while True:
    r1=int(input('Escolha uma opção;\n1-Adicionar livro\n2-Ver lista\n3-Sair\n'))
    if r1==3:
        break
    elif r1 ==1:
        i1=input('Qual o titulo do livro:').title()
        i2=input('Qual o autor do livro:').title()
        i3=int(input('Qual o ano de punlicação:'))
        i4=input('Disponivel/Indisponivel:').title()
        add={"titulo":i1, "autor":i2, "ano":i3, "status":i4}
        l.append(add)
    elif r1 ==2:
        for c in l:
            print(f'Titulo:{c["titulo"]}\nAutor:{c["autor"]}\nAno de publicação:{c["ano"]}\nStatus:{c["status"]}')
    else:
        print("opção incorreta")        