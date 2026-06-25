l=[
    {"nome": "Jerry", "votos":0},
    {"nome": "Bruno", "votos":0},
    {"nome": "Ryan", "votos":0},
    {"nome": "Pedro", "votos":0}
]

while True:
    r1=int(input("Escolha uma opção:\n1-votar\n2-Obter vencedor\n3-Gerar relatorio\nOpção:"))
    
    if(r1==1):
        r2=input("Candidato:")
        