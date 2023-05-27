from dataclasses import dataclass
@dataclass
class Producto_Base:
    nombre: str
    tiene_iva: bool

@dataclass
class Batch:
    Id: int
    lab: str
    costo: float
    precio: float
    cantidad: int

@dataclass
class Producto(Producto_Base):
    id: int
    batches: list[Batch]

    nombre: str
    tiene_iva: bool

    def detalle_producto(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Tiene IVA: {self.tiene_iva}")
        print(f"Batches: {self.batches}")