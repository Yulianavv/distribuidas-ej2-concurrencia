import concurrent.futures
import time


def ejecutar_electrodomestico(nombre: str, duracion: float):
    """Simula el funcionamiento de un electrodoméstico durante un tiempo determinado."""
    print(f"[INICIO] {nombre} ha iniciado su operación (duración estimada: {duracion:.2f}s)...")
    time.sleep(duracion)
    print(f"[FIN]    {nombre} ha finalizado su ciclo con éxito.")
    return nombre


def main():
    electrodomesticos = [
        ("Ciclo de lavadora de ropa", 4.0),
        ("Robot aspirador limpiando la sala", 3.0),
        ("Microondas calentando comida", 2.0),
    ]

    tiempo_secuencial = sum(duracion for _, duracion in electrodomesticos)

    print("==================================================")
    print(" EJERCICIO 2: ELECTRODOMÉSTICOS DEL HOGAR (CONCURRENTE)")
    print("==================================================")
    print(f"Total de electrodomésticos: {len(electrodomesticos)}")
    print(f"Tiempo estimado secuencial (suma de tareas): {tiempo_secuencial:.2f} segundos\n")

    inicio = time.perf_counter()

    # Ejecución concurrente mediante pool de hilos
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(electrodomesticos)) as executor:
        futuros = [
            executor.submit(ejecutar_electrodomestico, nombre, duracion)
            for nombre, duracion in electrodomesticos
        ]
        # Esperar la finalización de todas las tareas a medida que culminan
        for futuro in concurrent.futures.as_completed(futuros):
            futuro.result()

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print("\n==================================================")
    print(f"Tiempo total de ejecución concurrente: {tiempo_total:.2f} segundos")
    print(f"Ahorro de tiempo obtenido: {tiempo_secuencial - tiempo_total:.2f} segundos")
    print("==================================================")


if __name__ == "__main__":
    main()
