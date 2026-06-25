l=[
    {'titulo':'arroz','autor':'edjandir','data':'20/05/26'},
]

while True:
    r1=input('Titulo:')
    r2=input('Autor:')
    r3=input('data(DD/MM/AA)')
    add=({'titulo':r1,'autor':r2,'data':r3},)
    l.append(add)
    for c in l:
        print(c['titulo'],c['autor'],c['data'])