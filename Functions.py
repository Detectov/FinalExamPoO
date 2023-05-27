from Classes import *

misProductos = []
def crear_prodbase(nombre:str, tiene_iva:bool):
    return Producto_Base(nombre, tiene_iva)

def crear_batch(id:int, lab:str, costo:float, precio:float, cantidad:int) -> Batch:
    product_id: int = int(input("Ingrese el ID del producto: "))
    for product in misProductos:
        if product.Id == product_id:
            lab = input("Ingrese el nombre del laboratorio: ")
            costo = float(input("Ingrese el costo del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            Producto.batches.append(Batch(id, lab, costo, precio, cantidad))
            print("Batch guardado")
            return Batch(id, lab, costo, precio, cantidad)
        else:
            print("Producto no encontrado") 
   
    

def crear_producto(id:int, batches:list[Batch], nombre:str, tiene_iva:bool) -> Producto:
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    tiene_iva = bool(input("Tiene IVA? (True/False): "))
    misProductos.append(Producto(id, batches, nombre, tiene_iva))
    return Producto(id, batches, nombre, tiene_iva)

def imprimir_producto():
    for producto in misProductos:
        print(f"Nombre: {producto.nombre}")
        print(f"ID: {producto.id}")
        print(f"Tiene IVA: {producto.tiene_iva}")
        print(f"Batches: {producto.batches}")
        print()

def guardar_en_archivo():
    with open("productos.txt", "w") as f:
        for producto in misProductos:
            f.write('{},{},{},{},\n'.format(producto.id, producto.nombre, producto.tiene_iva, producto.batches))
            

def menu():
    while True:
        opcion = int(input("Ingrese una opción\n1. Crear un batch\n2. Crear un producto\n3. Imprimir productos\n4. Salir\n"))
        match opcion:
            case 1:
                crear_batch(id: int, lab: str, costo: float, precio: float, cantidad: int)
            case 2:
                crear_producto(id: int, batches: list[Batch], nombre: str, tiene_iva: bool)
            case 3:
                imprimir_producto()
            case 4:
                print("Saliendo...")
                exit()
            case _:
                print("Opción inválida")
                



    









