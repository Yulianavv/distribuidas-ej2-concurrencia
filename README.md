# Ejercicio 2: Ejecución con Concurrencia

## Descripción del Caso
Simulación del funcionamiento simultáneo de múltiples electrodomésticos en el hogar:
- **Lavadora de ropa**: 4.00 segundos
- **Robot aspirador**: 3.00 segundos
- **Microondas**: 2.00 segundos

En un modelo secuencial, el tiempo total sería la suma de todas las tareas (9.00 segundos). Mediante la ejecución concurrente con un pool de hilos (`concurrent.futures.ThreadPoolExecutor`), todas las tareas inician y operan simultáneamente, completándose en un tiempo equivalente al electrodoméstico más lento (~4.00 segundos).

## Requisitos
- Docker y Docker Compose instalados.
- (Opcional para ejecución directa en local): Python 3.8 o superior.

## Comandos de Ejecución

### Con Docker Compose (Recomendado)
Levantar y ejecutar el servicio:
```bash
docker compose up
```

Detener y eliminar los contenedores:
```bash
docker compose down
```

### Ejecución Local Directa
```bash
python 02_concurrente.py
```

## Salida Esperada en Consola
```text
==================================================
 EJERCICIO 2: ELECTRODOMÉSTICOS DEL HOGAR (CONCURRENTE)
==================================================
Total de electrodomésticos: 3
Tiempo estimado secuencial (suma de tareas): 9.00 segundos

[INICIO] Ciclo de lavadora de ropa ha iniciado su operación (duración estimada: 4.00s)...
[INICIO] Robot aspirador limpiando la sala ha iniciado su operación (duración estimada: 3.00s)...
[INICIO] Microondas calentando comida ha iniciado su operación (duración estimada: 2.00s)...
[FIN]    Microondas calentando comida ha finalizado su ciclo con éxito.
[FIN]    Robot aspirador limpiando la sala ha finalizado su ciclo con éxito.
[FIN]    Ciclo de lavadora de ropa ha finalizado su ciclo con éxito.

==================================================
Tiempo total de ejecución concurrente: 4.01 segundos
Ahorro de tiempo obtenido: 4.99 segundos
==================================================
```
