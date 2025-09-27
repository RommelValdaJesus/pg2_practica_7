class Repuesto:
    def __init__(self, id_repuesto: int, nombre: str, categoria: str, precio: float, stock: int, proveedor=None):
        self.id = id_repuesto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def actualizar_stock(self, cantidad: int):
        self.stock += cantidad

    def cambiar_precio(self, nuevo_precio: float):
        self.precio = nuevo_precio

    def __repr__(self):
        return f"<Repuesto {self.nombre} ({self.stock} unidades)>"
