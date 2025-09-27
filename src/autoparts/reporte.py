class Reporte:
    @staticmethod
    def resumen_inventario(inventario):
        return [f"{r.nombre}: {r.stock} unidades" for r in inventario.repuestos]

    @staticmethod
    def resumen_ventas(ventas):
        return [f"Venta {v.id} - Cliente {v.cliente} - Total: {v.calcular_total()}" for v in ventas]
