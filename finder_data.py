import json

datos = {
    'nombre': input('Ingrese su nombre'),
   'apellido': input('Ingrese su apellido'),
   'lugar_hallazgo':input ('Ingrese aqui el lugar del hallazgo'),
'fecha_hallazgo': input ('Ingrese aqui la fecha del hallazgo'),
'Ingrese_mascota': input ('Ingrese la mascota encontrada')
}


with open('./finder_data.json') as file:
   json.dump(datos, file, indent=4)
   file.close()