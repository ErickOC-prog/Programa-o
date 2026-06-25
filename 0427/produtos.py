r=0
r2=0
i=0
l=[
 {"nome":"pessego","preço": 3, "quantia":0},
 {"nome":"batata","preço": 6,  "quantia":0},
 {"nome":"feijao","preço": 2, "quantia":0},
 {"nome":"farofa","preço": 10,  "quantia":0},
]
while True:
 r=int(input("Digite o numero referente a cada produto que queria adicionar a lista\n1-pessego(3R$)\n2-batata(6,00R$)\n3-feijao(2,00R$)\n4-farofa(10,00R$)\nDigite 0 para finalizar\n"))
 if r==0:
  break
 r2=int(input("Quatos desse produto voce gostaria de adicionar a lista?\n"))
 if r in [1,2,3,4]:
  print(f"{r2} unidades do produto {r} foram adiocinadas a lista!")
 i=r-1
 l[i]["quantia"] += r2

for item in l:
    if item["quantia"] > 0:
        print(f"{item['nome']}: {item['quantia']} unidades.\n O valor total é {item["quantia"]}*{item["preço"]} R$")
      
   
