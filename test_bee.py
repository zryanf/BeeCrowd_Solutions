#beecrowd 1040
n1,n2,n3,n4 = map(float,input().split())

def media(n1,n2,n3,n4):
    mediar = (n1*2+n2*3+n3*4+n4*1)/10
    return mediar

def somar():
    medias = media(n1,n2,n3,n4)
    nota = float(input())
    soma= (medias + nota)/2
    return soma

def passar():
    if (media >= 5.0 and media <= 6.9)
        return ("Aluno em exame.")

if __name__ == '__main__':
    print("Media: ",media(n1,n2,n3,n4))
    if media(n1,n2,n3,n4) >=7:
        print("Aluno aprovado.")
    elif media(n1,n2,n3,n4) < 5.0:
        print("Aluno reprovado.")
    if (media >= 5.0 and media <= 6.9):
        
media = (n1*2+n2*3+n3*4+n4*1)/10
if (media >= 7.0):
    print("Aluno aprovado.")
elif (media < 5.0):
    print("Aluno reprovado.")
if (media >= 5.0 and media <= 6.9):
    nota = float(input())
    print("Aluno em exame.")
    print("Nota do exame: ",nota)
    soma= float((media + nota)/2)
elif(soma>=5.0):
        print("Aluno aprovado.")
        print("Media final: ", soma)
elif(soma<=4.9):
        print("Aluno reprovado.")
        print("Media final: ", soma)
