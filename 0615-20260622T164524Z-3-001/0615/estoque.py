
def add(l,id,nome,quantidade,preco):
    adicionar={"id":id,"nome":nome,"quantidade":quantidade,"preco":preco}
    l.append(adicionar)

def att(l,id,nova_quantidade):
    for c in l:
        if c["id"]==id:
            print(f"A quantidade atual é {c["quantidade"]}unidades")
            c["quantidade"]=nova_quantidade

def calc(l):
    total=0
    for c in l:
        total+=c["quantidade"]*c["preco"]
    print(f"O total de valor em mercadorias é {total}reais")  