from .repuesto import Repuesto

class Inventario:
    def __init__(self):
        self.repuestos = []

    def agregar_repuesto(self, repuesto: Repuesto):
        self.repuestos.append(repuesto)

    def buscar_repuesto(self, nombre: str):
        return [r for r in self.repuestos if nombre.lower() in r.nombre.lower()]

    def listar_por_categoria(self, categoria: str):
        return [r for r in self.repuestos if r.categoria.lower() == categoria.lower()]

    def stock_bajo(self, minimo: int = 5):
        return [r for r in self.repuestos if r.stock <= minimo]

    def __repr__(self):
        return f"<Inventario con {len(self.repuestos)} repuestos>"
