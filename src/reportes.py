from .portafolio import Portafolio

class ReportadorFinanciero:
    """Clase especializada solo en salida de datos (SRP)"""
    
    def imprimir_resumen(self, portafolio: Portafolio) -> None:
        print("\n" + "═" * 45)
        print(" 📈 REPORTE DE ESTADO - SMART PORTFOLIO")
        print(" " + "═" * 45)
        
        total_invertido = 0.0
        
        # Encabezado de tabla simple
        print(f"{'TICKER':<10} | {'CANT':<8} | {'VALOR ACTUAL':<15}")
        print("-" * 45)

        for pos in portafolio.posiciones:
            # Simulamos que el precio subió un 5% para el reporte
            precio_mercado = pos.precio_entrada * 1.05 
            valor_posicion = pos.calcular_valor_actual(precio_mercado)
            total_invertido += valor_posicion
            
            print(f"{pos.instrumento.ticker:<10} | {pos.cantidad:<8.2f} | ${valor_posicion:>12,.2f}")

        print("-" * 45)
        print(f"{'TOTAL DEL PORTAFOLIO:':<21} ${total_invertido:>12,.2f}")
        print("═" * 45 + "\n")