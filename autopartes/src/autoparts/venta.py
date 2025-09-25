from datetime import datetime

class Venta:
    def __init__(self, id_venta: int, fecha: str, cliente: str):
        self.id = id_venta
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        self.cliente = cliente
        self.items = []  # (repuesto, cantidad)

    def agregar_item(self, repuesto, cantidad: int):
        if repuesto.stock >= cantidad:
            repuesto.actualizar_stock(-cantidad)
            self.items.append((repuesto, cantidad))
        else:
            raise ValueError(f"No hay suficiente stock de {repuesto.nombre}")

    def calcular_total(self):
        return sum(repuesto.precio * cantidad for repuesto, cantidad in self.items)

    def __repr__(self):
        return f"<Venta {self.id} - Cliente: {self.cliente} - Total: {self.calcular_total()}>"
