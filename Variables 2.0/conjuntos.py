#creando un conjunto con set


conjunto = set(["dato1", "dato2"])

#metiendo un conjunto dentro de otro

conjunto1 = frozenset(["wenas", "que", "tal"])
conjunto2 = {conjunto1, "tasdasal"}

print(conjunto)
print(conjunto2)

#teoria de conjuntos

#datos
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#es subconjunto de

resultado = conjunto4.issubset(conjunto3)

#otra forma de hacerlo es resultado = conjunto4 <= conjunto3

#es superconjunto de

resultado2 = conjunto3.issuperset(conjunto4)

#otra forma de hacerlo es resultado = conjunto4 > conjunto3

print(resultado)
print(resultado2)


#verificar si tienen un numero en comun

resultado3 = conjunto4.isdisjoint(conjunto3)

print(resultado3)



