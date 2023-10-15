nomeHeroi = input("Informe o nome do seu Herói:")
xp = int(input("Quantos XP's seu herói tem?"))

print ("Bem vindo Heroi " + nomeHeroi)


 

if(xp >=0 ) and (xp <= 1000) :
    print("Você é um Herói nivel Ferro!")

elif(xp >1000) and ( xp <= 2000):
    print("Você é um Herói nivel Bronze!")

elif(xp >2000) and ( xp <= 5000):
    print("Você é um Herói nivel Prata!")

elif(xp >6000) and ( xp <= 7000):
    print("Você é um Herói nivel Ouro!")

elif(xp >7000) and ( xp <= 8000):
    print("Você é um Herói nivel Platina!")

elif(xp >8000) and ( xp <= 9000):
    print("Você é um Herói nivel Ascendente!")

elif(xp >9000) and ( xp <= 10000):
    print("Você é um Herói nivel Imortal!")            

else:
    (xp >10000)
    print("Você é um Herói nivel Radiante!")

try:
    xp >= 0   

except:
    print("Você informou um valor invalido!")



