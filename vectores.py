from sys import stdin
import oper as a

def sumaVectores(lista1,lista2):
    suma=[]
    for i in range(len(lista1)):
        resp=a.sumar(lista1[i],lista2[i])
        suma.append(resp)
    print(suma)


def main():
    tamaño=int(stdin.readline().strip())
    lista1=[]
    lista2=[]
    for i in range(tamaño):
        exp1=[int(x) for x in stdin.readline().split()]
        lista1.append(exp1)
    for i in range(tamaño):
        exp2=[int(x) for x in stdin.readline().split()]
        lista2.append(exp2)
    print(sumaVectores(lista1,lista2))
main()
