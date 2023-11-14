'''
Escreva um programa que leia um valor em metros
e o exiba convertido em centimetros e milimetros
'''
metro = float(input('Digite qtd metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 1000
cm = metro * 10000
mm = metro * 100000


print(f'{metro}m corresponde: \n{km}km, \n{hm}hm, \n{dam}dam, \n{dm},dm, \n{cm}cm e \n{mm}mm.')
