# Crear un diccionario
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado a la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para "telefono"
informacion_personal["telefono"] = "0991234567"

# Verificar si la clave "telefono" existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"  # Esto no se ejecutará porque ya existe

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)

