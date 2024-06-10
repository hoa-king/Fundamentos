productos = {"shampoo": 1200, 
    "jabón": 1000,
    "pasta de dientes": 1000, 
    "confort": 2000, 
    "clorox": 900
}
canasta = []
while True:
        print("\n1. Agregar productos")
        print("2. Ver canasta")
        print("3. Ver total")
        print("4. Salir")
    
        try:
             opcion = int(input("Seleccione una opción: "))

             if opcion == 1:
                   print("\n.... Agregar productos....")
                   for i, producto in enumerate(productos, start= 1):
                         print(f" {i}.{producto}- ${productos[producto]}")
                         prod_sel = int(input("Ingrese el numero del producto que desea agregar: "))
                         canasta = list(productos.keys())[prod_sel-1]
                         
                

    
        except ValueError:
             print("Operación no válida")

