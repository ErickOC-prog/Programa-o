def calcular(a,b,op):
    if op == "soma":
        t=a+b
        return t

    elif op=="subtração":
        t=a-b
        return t
    
    elif op=="multiplicação":
        t=a*b
        return t
    
    elif op=="divisão":
        t=a/b
        return t
    
print("----MENU----")
a=float(input("Me diga o numero A: "))
b=float(input("Me diga o numero B: "))
r1=int(input("Escolha uma opção:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n"))
if r1==1:
    op="soma"
elif r1==2:
    op="subtração"
elif r1==3:
    op="multiplicação"
elif r1==4:
    op="divisão"

resultado=calcular(a,b,op)
print(f"O resultado da {op} é {resultado}")