class Proveedor:
    def __init__(self, id_proveedor: int, nombre: str, telefono: str, email: str):
        self.id = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.productos = []

    def agregar_producto(self, repuesto):
        self.productos.append(repuesto)

    def listar_productos(self):
        return [p.nombre for p in self.productos]

    def __repr__(self):
        return f"<Proveedor {self.nombre}>"
