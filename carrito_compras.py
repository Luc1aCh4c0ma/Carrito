import os
import funciones
from colorama import init, Fore, Back, Style

init()

def mostrar_menu_principal():
    print(Fore.YELLOW+Style.BRIGHT+"=== BIENVENIDO ===")
    print("1. Ver Productos")
    print("2. Breve Descripción de los Productos")
    print("3. Buscar Productos por CODIGO")
    print("4. Realizar Compra")
    print("5. Mi Carrito")
    print("6. Salir"+Fore.RESET+Style.RESET_ALL)
    print (Style.BRIGHT+"°"*40+Style.RESET_ALL)

def mostrar_submenu1():
    os.system ("cls")
    print(Fore.BLUE+Style.BRIGHT+"=== REALIZAR COMPRA ===")
    print (Back.WHITE+"si desea eliminar/editar productos ingrese a la opcion 'mi carrito' (5) del menú principal "+Back.RESET)
    print("1. Agregar Productos")
    print("2. Ver Compra")
    print("3. Finalizar Compra ")
    print("4. Volver al menú principal"+Fore.RESET+Style.RESET_ALL)
    print (Style.BRIGHT+"°"*40+Style.RESET_ALL)

def mostrar_submenu2():
    os.system ("cls")
    print(Fore.BLUE+Style.BRIGHT+"=== MI CARRITO ===")
    print("1. Modificar Cantidad")
    print("2. Eliminar Productos")
    print("3. Volver al menú principal"+Fore.RESET+Style.RESET_ALL)
    print (Style.BRIGHT+"°"*40+Style.RESET_ALL)


# Función principal que maneja la lógica del menú
def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == "4":
            mostrar_submenu1()
            opcion_submenu1 = input("Selecciona una opción: ")

            if opcion_submenu1 == "1":
                print(Fore.MAGENTA+Style.BRIGHT+"== AGREGAR PRODUCTOS =="+Fore.RESET+Style.RESET_ALL)
                funciones.producto_codigo ()
                codigo = input ("ingrese codigo del producto: ")
                if codigo == "2001":
                   print ("LAPTOP")
                   funciones.agregar_laptop()
                   funciones.otro_producto()
                elif codigo == "2002":
                   print ("TELEFONO")
                   funciones.agregar_telefono()
                   funciones.otro_producto()
                elif codigo == "2003":
                   print ("SMARTWATCH")
                   funciones.agregar_smartwatch()
                   funciones.otro_producto()
                elif codigo == "2004":
                   print ("TABLETS")
                   funciones.agregar_tablets()
                   funciones.otro_producto()
                elif codigo == "2005":
                   print ("AURICULARES")
                   funciones.agregar_auriculares()
                   funciones.otro_producto()
                else: print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] codigo inexistente, pruebe de nuevo o consulte la lista de productos"+Fore.RESET+Style.RESET_ALL+Back.RESET)

            elif opcion_submenu1 == "2":
                # Lógica para la opción 2 del submenú 1
                print(Fore.MAGENTA+Style.BRIGHT+"== VER COMPRA =="+Fore.RESET+Style.RESET_ALL)
                if len(funciones.carrito) == 0:
                    print("el carrito no tiene productos")
                else:
                    print (funciones.carrito)
            elif opcion_submenu1== "3":
                print (Fore.MAGENTA+Style.BRIGHT+"== FINALIZAR COMPRA =="+Fore.RESET+Style.RESET_ALL)
                if len(funciones.carrito) == 0:
                    print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"el carrito no tiene productos"+Fore.RESET+Style.RESET_ALL+Back.RESET)
                else:
                    choice=input("Desea finalizar compra? SI=1 / NO=0:  ")
                    if choice == "1":
                       funciones.ticket ()
                       print("")
                       print(Fore.BLUE+Style.BRIGHT+Back.WHITE+"Gracias por comprar en nuestra Tienda :)"+Fore.RESET+Style.RESET_ALL+Back.RESET)
                       exit ()
                    elif choice == "0":
                       print (Fore.GREEN+Style.BRIGHT+"volvera al menu principal"+Fore.RESET+Style.RESET_ALL)
                    else: 
                       print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso invalido, pofavor ingrese vallor indicado"+Fore.RESET+Style.RESET_ALL+Back.RESET)
      
            elif opcion_submenu1 == "4":
                print()
                print (Style.BRIGHT+"°"*40+Style.RESET_ALL)
                continue
            else: 
                print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso no valido "+Fore.RESET+Style.RESET_ALL+Back.RESET)
        elif opcion == "5":
            mostrar_submenu2()
            opcion_submenu2 = input("Selecciona una opción: ")

            if opcion_submenu2 == "1":
                print(Fore.MAGENTA+Style.BRIGHT+"== MODIFICAR CANTIDAD =="+Fore.RESET+Style.RESET_ALL)
                if len(funciones.carrito) == 0:
                    print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"el carrito no tiene productos"+Fore.RESET+Style.RESET_ALL+Back.RESET)
                else:
                    funciones.modificar2()
            elif opcion_submenu2 == "2":
                print(Fore.MAGENTA+Style.BRIGHT+"== ELIMINAR PRODUCTOS =="+Fore.RESET+Style.RESET_ALL)
                if len(funciones.carrito) == 0:
                    print(Fore.BLACK+Style.BRIGHT+Back.YELLOW+"el carrito no tiene productos"+Fore.RESET+Style.RESET_ALL+Back.RESET)
                else:
                    funciones.eliminar ()
            elif opcion_submenu2 == "3":
                print()
                print (Style.BRIGHT+"°"*40+Style.RESET_ALL)
                continue
            else:
                print(Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso no valido "+Fore.RESET+Style.RESET_ALL+Back.RESET)

        elif opcion == "1":
            print("")
            funciones.mostrar()
        elif opcion == "2":
            print (Fore.MAGENTA+Style.BRIGHT+"=== INFORMACION BREVE DE PRODUCTOS ==="+Fore.RESET+Style.RESET_ALL)
            funciones.breve_informacion ()
        
        elif opcion == "3":
            print (Fore.MAGENTA+Style.BRIGHT+"=== BUSCAR PRODUCTOS POR -CODIGO- ==="+Fore.RESET+Style.RESET_ALL)
            codigo = input ("ingrese codigo del producto: ")
            if codigo == "2001":
               funciones.prod_laptop()
            elif codigo == "2002":
                funciones.prod_telefono()
            elif codigo == "2003":
                funciones.prod_smart()
            elif codigo == "2004":
                funciones.prod_tablet()
            elif codigo == "2005":
                funciones.prod_auri()
            else: print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] codigo inexistente, pruebe de nuevo o consulte la lista de productos"+Fore.RESET+Style.RESET_ALL+Back.RESET)
            main ()    

        elif opcion == "6":
            print("")
            print(Fore.BLUE+Style.BRIGHT+Back.WHITE+"¡Hasta luego!"+Fore.RESET+Style.RESET_ALL+Back.RESET)
            break

        else:
            print (Fore.RED+Style.BRIGHT+Back.WHITE+"[!] ingreso no valido, porfavor intente de nuevo con un numero del 1 al 6"+Fore.RESET+Style.RESET_ALL+Back.RESET) 
        print ("\n")
# Llamar a la función principal para comenzar el programa
main()