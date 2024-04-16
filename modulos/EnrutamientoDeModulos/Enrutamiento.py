#si el modulo esta en una subcarpeta se importa asi
#import carpeta.moduloAImportar

#print(carpeta.moduloAImportar.funcion(Variable))

#si el modulo esta fuera de la carpeta de este mismo archivo se usa:

import sys

print(sys.builtin_module_names) #dato: python da prioridad a los modulos propios asique tener cuidado con nombrar archivos o funciones con los mimsmos nombres
print(sys.path) #devuelve la ruta del archivo
sys.path.append("ruta del modulo") #importar modulo desde una ruta espesifica
import moduloimportado as modulo #una vez importado se puede importar al archivo python
print(modulo.si) #se llama a la funcion