"""Módulo para evaluar el inventario y calcular las cantidades a reabastecer."""

# Matriz con al menos 5 artículos:
# [Código del artículo, Nombre del artículo, Stock actual, Stock mínimo requerido]
INVENTARIO = [
    ["ART-001", "Resistencia 220 ohmios", 15, 50],
    ["ART-002", "Capacitor cerámico 100nF", 120, 80],
    ["ART-003", "Sensor ultrasónico HC-SR04", 10, 10],
    ["ART-004", "Cable jumper macho-macho", 25, 40],
    ["ART-005", "Protoboard 830 puntos", 18, 12],
    ["ART-006", "Diodo LED rojo 5mm", 30, 100],
]


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """Calcula la cantidad exacta que debe solicitarse para reabastecer un artículo.

    Args:
        stock_actual (int): Unidades disponibles actualmente en inventario.
        stock_minimo (int): Unidades mínimas requeridas.

    Returns:
        int: Cantidad a pedir (0 si el stock actual es mayor o igual al mínimo).
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def generar_lista_reabastecimiento(matriz_inventario):
    """Recorre la matriz de inventario y construye el listado de pedido por artículo.

    Args:
        matriz_inventario (list[list]): Filas con código, nombre, stock actual y mínimo.

    Returns:
        list[tuple[str, int]]: Lista de tuplas con (nombre_articulo, cantidad_a_pedir).
    """
    lista_pedidos = []

    for articulo in matriz_inventario:
        _codigo, nombre_articulo, stock_actual, stock_minimo = articulo
        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        lista_pedidos.append((nombre_articulo, cantidad_pedir))

    return lista_pedidos


def mostrar_reporte_inventario():
    """Ejecuta el cálculo y muestra en pantalla el nombre y cantidad a solicitar."""
    pedidos = generar_lista_reabastecimiento(INVENTARIO)

    print("=== REPORTE DE REABASTECIMIENTO DE INVENTARIO ===")
    for nombre_articulo, cantidad_pedir in pedidos:
        print(f"- {nombre_articulo}: {cantidad_pedir} unidades")


if __name__ == "__main__":
    mostrar_reporte_inventario()
    input("\nPresiona ENTER para salir...")