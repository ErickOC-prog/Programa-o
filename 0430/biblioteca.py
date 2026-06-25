r=0
r2=0
r3=0
r4=0
l=[  
 {"codigo": 1, "titulo": "Harry Piter","autor": "joel", "ano": 2030, "disponivel": "Disponivel" },
 {"codigo": 2, "titulo": "Senho dos anel","autor": "arthu", "ano": 1945, "disponivel": "Indisponivel" },
 {"codigo": 3, "titulo": "Onde piece","autor": "oda", "ano": 1880, "disponivel": "Disponivel" }
]
while True:
    r=int(input("Lista de comandos\n 1-Ver livros \n 2-Alugar um livro\n 3-devolver um livro\n"))
    if r==1:
        for c in l:
         print(c["codigo"],c["titulo"],c["autor"],c["ano"],c["disponivel"])
    elif r==2:
       for c in l:
         print(c["codigo"],c["titulo"],c["autor"],c["ano"],c["disponivel"])
    r2=int(input("\n Qual livro gostaria de alugar?\n(1,2,3)\n"))
    for z in l:
      if z ["disponivel"]=="Disponivel":
         
