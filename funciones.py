import os
from colorama import init , Fore, Style, Back
init ()

laptop = {Style.BRIGHT+"codigo"+Style.RESET_ALL: 2001,
        Style.BRIGHT+"marca"+Style.RESET_ALL: "Lenovo / ThinkPad",
        Style.BRIGHT+"precio"+Style.RESET_ALL: 360000,
        Style.BRIGHT+"stock"+Style.RESET_ALL: 16,
        Style.BRIGHT+"color"+Style.RESET_ALL : "gris", 
        Style.BRIGHT+"descripcion"+Style.RESET_ALL: " \n Pantalla: De 14”, UHD+ (3840x2400), IPS, 500 nits \n Procesador: Intel® Core™ i5-1145G7 \n Memoria RAM: 32 GB LPDDR4x-4266 \n Memoria de almacenamiento: SSD de 1 TB \n Gráficos: Intel® Iris® Xe \n Sistema operativo: Windows 10 Home 64"

}

telefono = {Style.BRIGHT+"codigo"+Style.RESET_ALL: 2002,
        Style.BRIGHT+"marca"+Style.RESET_ALL: "Apple / iPhone 12",
        Style.BRIGHT+"precio"+Style.RESET_ALL: 150000,
        Style.BRIGHT+"stock"+Style.RESET_ALL: 42,
        Style.BRIGHT+"color"+Style.RESET_ALL: "negro",
        Style.BRIGHT+"descripcion"+Style.RESET_ALL:"\n Pantalla: De 6,1” (1170x2532) \n Procesador: Apple A14 Bionic hexa - core \n Memoria RAM: 32 GB LPDDR4x-4266 \n Memoria de almacenamiento: SSD de 256 GB \n Gráficos: super retina XDR OLED, 460 pi HDR10 \n Sistema operativo: iOS 14 Apple quad core"
}

smartwatch = {Style.BRIGHT+"codigo"+Style.RESET_ALL: 2003,
        Style.BRIGHT+"marca"+Style.RESET_ALL: "Samsung / Galaxy 3",
        Style.BRIGHT+"precio"+Style.RESET_ALL: 20000,
        Style.BRIGHT+"stock"+Style.RESET_ALL: 78,
        Style.BRIGHT+"color"+Style.RESET_ALL: "blanco",
        Style.BRIGHT+"descripcion"+Style.RESET_ALL: "\n Pantalla: Super AMOLED 1,4pix con resolución 360 x 360p \n Procesador: Dual Core 1.15 GHz WATCH 3 SM R840 \n Memoria RAM: 1 GB \n Memoria de almacenamiento: SSD de 8 GB \n Gráficos: Intel UHD \n Sistema operativo: Tizen"

}

tablets = {Style.BRIGHT+"codigo"+Style.RESET_ALL: 2004,
        Style.BRIGHT+"marca"+Style.RESET_ALL: "Microsoft / Surface 7",
        Style.BRIGHT+"precio"+Style.RESET_ALL: 90000,
        Style.BRIGHT+"stock"+Style.RESET_ALL: 22,
        Style.BRIGHT+"color"+Style.RESET_ALL: "gris",
        Style.BRIGHT+"descripcion"+Style.RESET_ALL: "\n Pantalla: PixelSense táctil de 12.3 con resolución 2736 x 1824p \n Procesador: Intel Core i3-1005G1 Dual-Core 1.20 GHz \n Memoria RAM: 4 GB LPDDR4x \n Memoria de almacenamiento: SSD de 128 GB \n Gráficos: Intel UHD \n Sistema operativo: Windows 10 Home"

}

auriculares = {Style.BRIGHT+"codigo"+Style.RESET_ALL: 2005,
    Style.BRIGHT+"marca"+Style.RESET_ALL: "Sony / WH-1000XM4",
    Style.BRIGHT+"precio"+Style.RESET_ALL: 350,
    Style.BRIGHT+"stock"+Style.RESET_ALL: 184,
    Style.BRIGHT+"color"+Style.RESET_ALL: "blanco",
    Style.BRIGHT+"descripcion"+Style.RESET_ALL: "\n Conexion: Bluetooth 5 / 10m, Alexa, Google Assistant, Siri\n Sonido: 4 Hz - 40 kHz / 105 dB / 40mm / over-ear"

}
carrito = []

def imprimir_diccionario (diccionario):
    for clave, valor in diccionario.items():
        print(clave, ":", valor)
        

def mostrar ():
    os.system ("cls")
    print (Fore.MAGENTA+Style.BRIGHT+"=== PRODUCTOS ==="+Fore.RESET+Style.RESET_ALL)
    print("")
    print(Fore.CYAN+Style.BRIGHT+"LAPTOP:"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (laptop)
    print("")
    print (Style.BRIGHT+"*"*40+Style.RESET_ALL)
    print(Fore.CYAN+Style.BRIGHT+"TELEFONO:"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (telefono)
    print("")
    print (Style.BRIGHT+"*"*40+Style.RESET_ALL)
    print(Fore.CYAN+Style.BRIGHT+"AURICULARES:"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (auriculares)
    print("")
    print (Style.BRIGHT+"*"*40+Style.RESET_ALL)
    print(Fore.CYAN+Style.BRIGHT+"SMARTWATCH"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (smartwatch)
    print("")
    print (Style.BRIGHT+"*"*40+Style.RESET_ALL)
    print(Fore.CYAN+Style.BRIGHT+"TABLET"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (tablets)
    print("")
    print (Style.BRIGHT+"*"*40+Style.RESET_ALL)


def breve_informacion ():
    os.system ("cls")
    atributos_mostrados = [Style.BRIGHT+"codigo"+Style.RESET_ALL, Style.BRIGHT+ "marca"+Style.RESET_ALL, Style.BRIGHT+"stock"+Style.RESET_ALL]
    print(Fore.CYAN+Style.BRIGHT+"LAPTOP:"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in laptop.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print ("\n")
    print(Fore.CYAN+Style.BRIGHT+"TELEFONO:"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in telefono.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print("\n")
    print(Fore.CYAN+Style.BRIGHT+"AURICULARES:"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in auriculares.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print ("\n")
    print(Fore.CYAN+Style.BRIGHT+"SMARTWATCH"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in smartwatch.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print ("\n")
    print(Fore.CYAN+Style.BRIGHT+"TABLET:"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in tablets.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)


def producto_codigo():
    os.system ("cls")
    print(Fore.MAGENTA+Style.BRIGHT+"== AGREGAR PRODUCTOS =="+Fore.RESET+Style.RESET_ALL)
    atributos_mostrados = [Style.BRIGHT+"codigo"+Style.RESET_ALL, Style.BRIGHT]
    print ("\n")
    print(Fore.CYAN+Style.BRIGHT+"LAPTOP:"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in laptop.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print ("\n")
    print(Fore.CYAN+Style.BRIGHT+"TELEFONO: "+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in telefono.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print("\n")
    print(Fore.CYAN+Style.BRIGHT+"AURICULARES:"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in auriculares.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print ("\n")
    print(Fore.CYAN+Style.BRIGHT+"SAMRTWATCH"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in smartwatch.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)
    print ("\n")
    print(Fore.CYAN+Style.BRIGHT+"TABLET:"+Fore.RESET+Style.RESET_ALL)
    for atributo, valor in tablets.items():
        if atributo in atributos_mostrados:
           print(atributo.capitalize() + ":", valor)

def prod_laptop ():
   os.system ("cls")
   print (Fore.CYAN+Style.BRIGHT+"LAPTOP "+Fore.RESET+Style.RESET_ALL)
   imprimir_diccionario (laptop)

def prod_telefono ():
    os.system ("cls")
    print(Fore.CYAN+Style.BRIGHT+"TELEFONO"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (telefono)

def prod_auri ():
    os.system ("cls")
    print(Fore.CYAN+Style.BRIGHT+"AURICULARES"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (auriculares)


def prod_smart ():
    os.system ("cls")
    print(Fore.CYAN+Style.BRIGHT+"SMARTWATCH"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (smartwatch)

def prod_tablet ():
    os.system ("cls")
    print(Fore.CYAN+Style.BRIGHT+"TABLET"+Fore.RESET+Style.RESET_ALL)
    imprimir_diccionario (tablets)

    
def agregar_laptop ():
    os.system ("cls")
    print (laptop[Style.BRIGHT+"marca"+Style.RESET_ALL])
    print ("Stock:", laptop [Style.BRIGHT+"stock"+Style.RESET_ALL])
    clave = Style.BRIGHT+"stock"+Style.RESET_ALL
    agregar = (input("desea agregar el producto al carrito? SI= 1 / NO = 0:  "))
    
    if agregar == "1":
       cantidad = int(input("ingrese la cantidad:  "))
       descuento = cantidad
       total = descuento * laptop[Style.BRIGHT+"precio"+Style.RESET_ALL]
       if clave in laptop:
          valor_actual = laptop[clave]
          if valor_actual > descuento:
             valor_actual -= descuento
             laptop[clave] = valor_actual
             carrito.append ([laptop [Style.BRIGHT+"marca"+Style.RESET_ALL],descuento,laptop[Style.BRIGHT+"precio"+Style.RESET_ALL],total])
             print("")
             print (Fore.GREEN+Style.BRIGHT+"agregado correctamente " + Fore.RESET+Style.RESET_ALL)
          else:
             print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] stock insuficiente"+Fore.RESET+Style.RESET_ALL+Back.RESET)
    
    elif agregar == "0":
        otro_producto()
    else: 
        print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso invalido, porfavor ingrese valor indicado"+Fore.RESET+Style.RESET_ALL+Back.RESET)

def agregar_telefono ():
    os.system ("cls")
    print (telefono[Style.BRIGHT+"marca"+Style.RESET_ALL])
    print ("Stock:", telefono [Style.BRIGHT+"stock"+Style.RESET_ALL])
    clave = Style.BRIGHT+"stock"+Style.RESET_ALL
    agregar = (input("desea agregar el producto al carrito? SI= 1 / NO = 0:  "))
    
    if agregar == "1":
       cantidad = int(input("ingrese la cantidad:  "))
       descuento = cantidad
       total = descuento*telefono[Style.BRIGHT+"precio"+Style.RESET_ALL]
       if clave in telefono:
          valor_actual = telefono[clave]
          if valor_actual > descuento:
             valor_actual -= descuento
             telefono[clave] = valor_actual
             carrito.append ([telefono [Style.BRIGHT+"marca"+Style.RESET_ALL],descuento,telefono[Style.BRIGHT+"precio"+Style.RESET_ALL],total])
             print("")
             print (Fore.GREEN+Style.BRIGHT+"agregado correctamente " + Fore.RESET+Style.RESET_ALL)
          else:
             print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] stock insuficiente"+Fore.RESET+Style.RESET_ALL+Back.RESET)
    
    elif agregar == "0":
            otro_producto()
    else: 
            print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso invalido, porfavor ingrese valor indicado"+Fore.RESET+Style.RESET_ALL+Back.RESET)


def agregar_auriculares ():
    os.system ("cls")
    print (auriculares[Style.BRIGHT+"marca"+Style.RESET_ALL])
    print ("Stock:", auriculares [Style.BRIGHT+"stock"+Style.RESET_ALL])
    clave = Style.BRIGHT+"stock"+Style.RESET_ALL
    agregar = (input("desea agregar el producto al carrito? SI= 1 / NO = 0:  "))
    
    if agregar == "1":
       cantidad = int(input("ingrese la cantidad:  "))
       descuento = cantidad
       total = descuento * auriculares[Style.BRIGHT+"precio"+Style.RESET_ALL]
       if clave in auriculares:
          valor_actual = auriculares[clave]
          if valor_actual > descuento:
             valor_actual -= descuento
             auriculares[clave] = valor_actual
             carrito.append ([auriculares [Style.BRIGHT+"marca"+Style.RESET_ALL],descuento,auriculares[Style.BRIGHT+"precio"+Style.RESET_ALL],total])
             print("")
             print (Fore.GREEN+Style.BRIGHT+"agregado correctamente " + Fore.RESET+Style.RESET_ALL)
          else:
             print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] stock insuficiente"+Fore.RESET+Style.RESET_ALL+Back.RESET)
    
    elif agregar == "0":
        otro_producto()
    else: 
        print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso invalido, porfavor ingrese valor indicado"+Fore.RESET+Style.RESET_ALL+Back.RESET)

def agregar_smartwatch ():
    os.system ("cls")
    print (smartwatch[Style.BRIGHT+"marca"+Style.RESET_ALL])
    print ("Stock:", smartwatch [Style.BRIGHT+"stock"+Style.RESET_ALL])
    clave = Style.BRIGHT+"stock"+Style.RESET_ALL
    agregar = (input("desea agregar el producto al carrito? SI= 1 / NO = 0:  "))
    
    if agregar == "1":
       cantidad = int(input("ingrese la cantidad:  "))
       descuento = cantidad
       total= descuento * smartwatch[Style.BRIGHT+"precio"+Style.RESET_ALL]
       if clave in smartwatch:
          valor_actual = smartwatch[clave]
          if valor_actual > descuento:
             valor_actual -= descuento
             smartwatch[clave] = valor_actual
             carrito.append ([smartwatch [Style.BRIGHT+"marca"+Style.RESET_ALL],descuento,smartwatch[Style.BRIGHT+"precio"+Style.RESET_ALL],total])
             print("")
             print (Fore.GREEN+Style.BRIGHT+"agregado correctamente " + Fore.RESET+Style.RESET_ALL)
          else:
             print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] stock insuficiente"+Fore.RESET+Style.RESET_ALL+Back.RESET)
    
    elif agregar == "0":
        otro_producto()
    else: 
        print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso invalido, porfavor ingrese valor indicado"+Fore.RESET+Style.RESET_ALL+Back.RESET)

def agregar_tablets ():
    os.system ("cls")
    print (tablets[Style.BRIGHT+"marca"+Style.RESET_ALL])
    print ("Stock:", tablets [Style.BRIGHT+"stock"+Style.RESET_ALL])
    clave = Style.BRIGHT+"stock"+Style.RESET_ALL
    agregar = (input("desea agregar el producto al carrito? SI= 1 / NO = 0:  "))
    
    if agregar == "1":
       cantidad = int(input("ingrese la cantidad:  "))
       descuento = cantidad
       total = descuento * tablets[Style.BRIGHT+"precio"+Style.RESET_ALL]
       if clave in tablets:
          valor_actual = tablets[clave]
          if valor_actual > descuento:
             valor_actual -= descuento
             tablets[clave] = valor_actual
             carrito.append ([tablets [Style.BRIGHT+"marca"+Style.RESET_ALL],descuento,tablets[Style.BRIGHT+"precio"+Style.RESET_ALL],total])
             print("")
             print (Fore.GREEN+Style.BRIGHT+"agregado correctamente " + Fore.RESET+Style.RESET_ALL)
          else:
             print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] stock insuficiente"+Fore.RESET+Style.RESET_ALL+Back.RESET)
    
    elif agregar == "0":
        otro_producto()
    else: 
        print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso invalido, porfavor ingrese valor indicado"+Fore.RESET+Style.RESET_ALL+Back.RESET)

def otro_producto ():
    otro= input("desea agregar otro producto?SI= 1 / NO = 0:  ")
    if otro == "1" :
        producto_codigo ()
        codigo = input ("ingrese codigo del producto: ")
        if codigo == "2001":
            print ("LAPTOP")
            agregar_laptop()
            otro_producto()
        elif codigo == "2002":
            print ("TELEFONO")
            agregar_telefono()
            otro_producto()
        elif codigo == "2003":
            print ("SMARTWATCH")
            agregar_smartwatch()
            otro_producto()
        elif codigo == "2004":
            print ("TABLET")
            agregar_tablets()
            otro_producto() 
        elif codigo == "2005":
            print ("AURICULARES")
            agregar_auriculares()
            otro_producto() 
        else: print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] codigo inexistente, pruebe de nuevo o consulte la lista de productos"+Fore.RESET+Style.RESET_ALL+Back.RESET)
    elif otro == "0":
        print (Fore.GREEN+Style.BRIGHT+"volvera al menu principal"+Fore.RESET+Style.RESET_ALL)
        
    else: print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso invalido, porfavor ingrese valor indicado"+Fore.RESET+Style.RESET_ALL+Back.RESET)
    


def ticket ():
    os.system ("cls")    
    carrito  
    print (Style.BRIGHT+Fore.GREEN+"*" * 40,  "TICKET ", "*" * 40+Fore.RESET+Style.RESET_ALL)
    print ("\n Producto \t\t\t Cantidad \t Precio Unitario \t Total")

    for producto in carrito:
        print (f"{producto[0]}\t\t {producto [1]}\t\t{producto[2]}\t\t\t{producto[3]}")

        total_ticket = sum ([producto [3]for producto in carrito])
    print ("<>"*40)
    print (Style.BRIGHT + f"\n Total a Pagar: {total_ticket}"+Style.RESET_ALL)  

def eliminar (): 
    os.system ("cls")
    carrito
    print("Lista de productos:")
    for i, producto in enumerate(carrito):
        print(f"{i + 1}. {producto[0]} - Cantidad: {producto[1]} - Precio unitario: {producto[2]} - Precio total: {producto[3]}")
        print ("")

    print ("ingrese la marca del producto que desea modifcar: \n EJEMPLO: 'Lenovo' ")
    nombre_producto = input("")
    print("")

    producto_encontrado = None
    for producto in carrito:
        if producto[0].split(" / ")[0] == nombre_producto:
           producto_encontrado = producto
           break
    
    if producto_encontrado is None:
        print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] Producto no encontrado. Por favor, ingrese un nombre de producto válido."+Fore.RESET+Style.RESET_ALL+Back.RESET)
    else: 
        compra = int(input("ingrese cantidad comprada: "))
        print("")
        if nombre_producto == "Lenovo":
            laptop[Style.BRIGHT+"stock"+Style.RESET_ALL] = laptop[Style.BRIGHT+"stock"+Style.RESET_ALL] + compra
        elif nombre_producto == "Apple":
            telefono[Style.BRIGHT+"stock"+Style.RESET_ALL] = telefono[Style.BRIGHT+"stock"+Style.RESET_ALL] + compra
        elif nombre_producto == "Samsung":
            smartwatch[Style.BRIGHT+"stock"+Style.RESET_ALL] = smartwatch[Style.BRIGHT+"stock"+Style.RESET_ALL] + compra
        elif nombre_producto == "Microsoft":
           tablets[Style.BRIGHT+"stock"+Style.RESET_ALL] = tablets[Style.BRIGHT+"stock"+Style.RESET_ALL] + compra
        elif nombre_producto == "Sony":
            auriculares[Style.BRIGHT+"stock"+Style.RESET_ALL] = auriculares[Style.BRIGHT+"stock"+Style.RESET_ALL] + compra
        carrito.remove(producto_encontrado)
        print(Fore.GREEN+Style.BRIGHT+"El producto ha sido eliminado correctamente."+Fore.RESET+Style.RESET_ALL)

    print("")
    print("Lista de productos actualizada:")
    for producto in carrito:
        print(producto)
        
def modificar2 (): 
    os.system ("cls")
    carrito
    print("Lista de productos:")
    for i, producto in enumerate(carrito):
        print(f"{i + 1}. {producto[0]} - Cantidad: {producto[1]} - Precio unitario: {producto[2]} - Precio total: {producto[3]}")
        print ("")

    print ("ingrese la marca del producto que desea modifcar: \n EJEMPLO: 'Lenovo' ")
    nombre_producto = input("")
    print("")

    producto_encontrado = None
    for producto in carrito:
        if producto[0].split(" / ")[0] == nombre_producto:
           producto_encontrado = producto
           break
    if producto_encontrado is None:
       print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] Producto no encontrado. Por favor, ingrese un nombre de producto válido."+Fore.RESET+Style.RESET_ALL+Back.RESET)
    else:
        cantidad_comprada = int(input("Ingrese la cantidad ya comprada: "))
        print ("")
        print ("Si desea descontar cantidad del producto anteponga un (-) de lo contrario anteponga un (+)")
        cantidad_modificar = int(input("Ingrese la cantidad a modificar: "))
        if nombre_producto == "Lenovo":
            if cantidad_comprada + cantidad_modificar >= 0:
                laptop[Style.BRIGHT+"stock"+Style.RESET_ALL] -= cantidad_modificar
                cantidad_comprada += cantidad_modificar
            else:
                print("La cantidad a modificar no es válida.")
        elif nombre_producto == "Apple":
            if cantidad_comprada + cantidad_modificar >= 0:
                telefono[Style.BRIGHT+"stock"+Style.RESET_ALL] -= cantidad_modificar
                cantidad_comprada += cantidad_modificar
            else:
                print("La cantidad a modificar no es válida.")
        elif nombre_producto == "Samsung":
            if cantidad_comprada + cantidad_modificar >= 0:
                smartwatch[Style.BRIGHT+"stock"+Style.RESET_ALL] -= cantidad_modificar
                cantidad_comprada += cantidad_modificar
            else:
                print("La cantidad a modificar no es válida.")
        elif nombre_producto == "Microsoft":
            if cantidad_comprada + cantidad_modificar >= 0:
                tablets[Style.BRIGHT+"stock"+Style.RESET_ALL] -= cantidad_modificar
                cantidad_comprada += cantidad_modificar
            else:
                print("La cantidad a modificar no es válida.")
        elif nombre_producto == "Sony":
            if cantidad_comprada + cantidad_modificar >= 0:
                auriculares[Style.BRIGHT+"stock"+Style.RESET_ALL] -= cantidad_modificar
                cantidad_comprada += cantidad_modificar
            else:
                print("La cantidad a modificar no es válida.")

# Imprimir el stock actualizado
            print("Stock disponible:", laptop[Style.BRIGHT+"stock"+Style.RESET_ALL])
    
        producto_encontrado[1] = cantidad_comprada
        producto_encontrado[3] = cantidad_comprada * producto_encontrado[2] 

        print (Fore.GREEN+Style.BRIGHT+"modificado correctamente " + Fore.RESET+Style.RESET_ALL)
        print ("")
        print("\nLista de productos actualizada:")
        for i, producto in enumerate(carrito):
            print(f"{i + 1}. {producto[0]} - Cantidad: {producto[1]} - Precio unitario: {producto[2]} - Precio total: {producto[3]}")