from .portafolio import Portafolio

class ReportadorFinanciero:
    def imprimir_resumen(self, portafolio: Portafolio) -> None:
        print("\n" + "═" * 50)
        print(f"{'📊 RESUMEN DE INVERSIONES':^50}")
        print("═" * 50)
        
        total_pnl = 0.0
        
        for pos in portafolio.posiciones:
            # Simulación: El mercado sube un 5% sobre el precio de entrada
            precio_simulado = pos.precio_entrada * 1.05
            pnl = pos.calcular_ganancia_no_realizada(precio_simulado)
            total_pnl += pnl
            
            print(f"Ticker: {pos.instrumento.ticker:<6} | Cant: {pos.cantidad:<6} | PnL: ${pnl:>8.2f}")
            
        print("-" * 50)
        print(f"Ganancia/Pérdida Total Estimada: ${total_pnl:>10.2f}")
        print("═" * 50 + "\n")