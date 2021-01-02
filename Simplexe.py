import numpy as np
import math
PL = input("Entrer les coefficients de votre PL :")
PL = PL.split()
longeur = len(PL)

for i in range(longeur):
    PL[i] = int(PL[i])

longeur_rows = input("Saisir le nombre  de variable 'ei' : ")
longeur_rows = int(longeur_rows)
matrice = []

print("saisir votre matrice : ")
for i in range(longeur_rows):
    matr = input().split()
    for j in range(len(matr)):
        matr[j] = float(matr[j])
    matrice.append(matr)

matrice = np.array(matrice)

coeff_v_b = []
for i in range(longeur_rows):
    PL.append(0)
    coeff_v_b.append(0)

# initialiser le premier tableau
Cj = np.array(PL)
coeff_v_b = np.array(coeff_v_b)

Zj = []
for i in range(len(matrice[1])):
    Zj.append(0)

Zj = np.array(Zj)

result = Cj - Zj[:-1]


while (len((np.where(result > 0))[0]) > 0):

    for i in range(len(matrice[1])):
        Zj[i] = 0

# chercher la position de la variable entrante
    x = np.where(result == max(result))
    x = x[0][0]

# chercher les variables sortantes
    Vs = matrice[:, -1] / matrice[:, x]
    Vs[Vs < 0] = math.nan
    for i in range(len(Vs)):
        if (Vs[i] < 0):
            Vs[i] = Vs[i] * (-1) / 0

# Chercher la position de la variable sortante
    y = np.where(Vs == min(Vs))
    y = y[0][0]

    print("les variabels sortantes : ", Vs)
    print("position de la variable entrante : ", x)
    print("position de la variable sortante : ", y)
    print("pivot : ", matrice[y, x])

# changer la variable sortante par la variable entrante

    coeff_v_b[y] = Cj[x]

# Changer la matrice et etablir la méthode de pivot de  Gauss
    matrice[y] = matrice[y] / matrice[y][x]

    # if (y == 1):
    #     matrice[0] = matrice[0] - matrice[0][x] * matrice[y]
    #     if (matrice[0, -1] < 0):
    #         matrice[0] = matrice[0] * (-1)

    for i in range(len(coeff_v_b)):
        if (i != y):
            matrice[i] = matrice[i] - matrice[i][x] * matrice[y]
            if (matrice[i, -1] < 0):
                matrice[i] = matrice[i] * (-1)

    # for i in range(len(coeff_v_b)-y-1):
    #     j = y+i+1
    #     matrice[j] = matrice[j] - matrice[j][x] * matrice[y]
    #     if (matrice[j, -1] < 0):
    #         matrice[j] = matrice[j] * (-1)


# Changer Zj

    for i in range(len(Cj)+1):
        for j in range(len(coeff_v_b)):
            Zj[i] = Zj[i] + matrice[j][i] * coeff_v_b[j]

    print("Cj : ", Cj)
    print("matrice : \n", matrice)
    print("coeff est : ", coeff_v_b)
    print("Zj : ", Zj)
    result = Cj - Zj[:-1]
    print("resultat : ", result)
    print()


# Afficher la solution optimale

print("la solution optimale est : ")
for i in range(longeur):
    xi = np.where(coeff_v_b == Cj[i])
    xi = xi[0][0]
    print("la solution x", i+1, "= ", matrice[xi][-1])

print("Z =", Zj[-1])
