BM1 = float(input"Digite a nota do primeiro bimestre:"))
BM2 = float(input"Digite a nota do segundo bimestre:"))
BM3 = float(input"Digite a nota do terceiro bimestre:"))
BM4 = float(input"Digite a nota do quarto bimestre:"))
media = float (BM1 + BM2 + BM3 + BM4)/4
print ("nota final do aluno",media)
if media >7:
   print ("aprovado")
elif media >=9:
   print ("aprovado com louvor!")
elif media <7:
   print ("reprovado")

