# coding=utf8
import numpy as np  # nÃ©cessaire pour avoir le calcul numÃ©rique

# mÃ©thode du simplexe pour rÃ©soudre
# max c.x sous contraintes
# Ax=b
# x >= 0
# permut(0..m-1) : variables dans la base initiale
# permut(m..n-1) : variables hors base initiale
# ne fonctionne que si la base initiale est admissible
# et les composantes de b >=0
# renvoie la solution et le gain maximal


def simplexe(A, b, c, permut):
    # m: nombre de variables dans la base
    # n: nombres d'inconnues du pb d'optimisation linÃ©aire
    m, n = A.shape
    if m >= n or c.shape[0] != n or b.shape[0] != m:
        return 'dimensions incompatibles'

    if min(b) < 0:
        return 'le vecteur b doit Ãªtre >=0'

    while True:  # Ã©mulation du do-while en python...
        # matrice des colonnes permutÃ©es
        Ap = np.column_stack((A[:, permut[i]] for i in range(n)))
        # coefficients du gain permutÃ©s
        cp = np.array([c[permut[i]] for i in range(n)])

        # vÃ©rification que le problÃ¨me n'est pas dÃ©gÃ©nÃ©rÃ©
        # en python ":m" dÃ©signe le range "0,1,...,m-1",
        # "m:" le range "m,m+1,...,n-1" et ":" le range "0,1,...,n-1"
        if np.linalg.det(Ap[:, :m]) == 0:
            return 'matrice non inversible'

        # expression des variables de base en
        # fonctions des variables hors base
        # x_b = Chb x_hb + bbase
        invAp = np.linalg.inv(Ap[:, :m])
        Chb = np.dot(invAp, Ap[:, m:])
        bbase = np.dot(invAp, b)

        # coefficients du gain dans les variables hors base
        cbase = -np.dot(cp[:m], Chb)+cp[m:]
        cmax = max(cbase)
        # si tout les coeffs sont  <0 on ne peut plus amÃ©liorer
        if cmax <= 0:
            break    # sortie du do-while
        # sinon choix de la variable optimale pour le gain
        # cette variable rentrera dans la base
        ihb = np.argmax(cbase)+m
        # choix de la variable qui s'annule en premier
        # quand la variable optimale augmente
        # cette variable sortira de la base
        xrmax = np.array([bbase[i]/Chb[i][ihb-m] for i in range(m)])
        vmax = max(xrmax)
        # on met les valeurs nÃ©gatives Ã  une valeur grande
        for i in range(m):
            if xrmax[i] <= 0:
                xrmax[i] = vmax+1

        # recherche de l'indice de "premiÃ¨re sortie"
        ib = np.argmin(xrmax)
        print('out=', permut[ib], '   in=', permut[ihb])

        # actualisation de la permutation
        permut[ib], permut[ihb] = permut[ihb], permut[ib]  # swap en python
        # fin du do while

    # fin de l'algorithme
    # on complÃ¨te le vecteur des variables
    # dans la base par des zÃ©ros
    xp = np.hstack((bbase, np.zeros(n-m)))
    # prise en compte de la permutation
    x = np.empty(n)
    for i in range(n):
        x[permut[i]] = xp[i]
    # renvoie la solution et le gain
    return x, np.dot(c, x)
# fin de la fonction simplexe


# test du programme prÃ©cÃ©dent sur l'exemple du cours
# matrice des contraintes Ax=b
A = np.array([[1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 1, 0], [3, 6, 2, 0, 0, 0, 1]])
# second membre des contraintes Ax=b
b = np.array([1000, 500, 1500, 6750])
# coefficients de la fonction Ã  maximiser
c = np.array([4, 12, 3, 0, 0, 0, 0])
# base initiale
# permutation contenant les m variables dans la base (x>=0) puis
# les variables hors base (n-m variables nulles)
permut = np.array([6, 5, 4, 3, 2, 1, 0])
print(simplexe(A, b, c, permut))
