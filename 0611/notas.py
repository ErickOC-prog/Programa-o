def media(q):
    t=0
    m=0
    for i in range (q):
        o=float(input(f"Qual a nota do aluno n{i+1}:"))
        t=o+t
    m=t/q
    print(f"A media final é {m}")

q=int(input("Quantos alunos tem na turma:"))