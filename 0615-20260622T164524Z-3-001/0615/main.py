from estoque import add,att,calc

l=[]

while True:
    r1=int(input("Escolha uma opção:\n1-Adicionar produto\n2-Atualizar estoque\n3-Calcular valor total em estoque\n4-Finalizar\nOpção:"))
    if (r1==4):
        break
    elif (r1==1):
        i1=int(input("ID:"))
        i2=input("Nome:")
        i3=int(input("Quantidade:"))
        i4=float(input("Preço:"))
        add(l,i1,i2,i3,i4)

    elif (r1==2):
        i1=int(input("ID:"))
        for c in l:
            if (c["id"])==i1:
                print(f"A quantidade atual é de {c["quantidade"]} unidades")
        i2=int(input("Nova quantidade:"))
        att(l,i1,i2)
    
    elif (r1==3):
        calc(l)

print("PROGRAMA FINALIZADO.....")