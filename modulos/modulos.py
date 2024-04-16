#se le dice modulo porque se pueden llamar otros desde el mismo archivo
#3tippos modulos de python(escritos en c), modulos de terceros(de otras personas) y modulos propios.

#llamar a otra funcion

import saludar #se importa con el nombre del archivo sin la extencion

saludo = saludar.saludar("franco") #la funcion cambia a metodo y se llama asi

print(saludo)

import saludar as Variable #nos permite asignar nombres a los modulos para no tener interfefiencia

from saludar import saludar #sirve para importar funciones espesificas de modulos tambien con coma se importan mas modulos

from saludar import saludar as cambiarNombre #sirve para cambiar el nombre de lo que se importa

#para ver los elementos se puede usar {print(dir(funcion))}