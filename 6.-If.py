edad = int(input("anota tu edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "la infancia es increible..."
elif 10 <= edad < 20:
    mensaje = "muchos cambios, mucho estudio..."
elif 20 <= edad < 30:
    mensaje = "amor y mucho trabajo..."
else:
    mensaje = "edad no encontrada, estas cañon"
print(f"tienes {edad} años de edad y ", mensaje)
