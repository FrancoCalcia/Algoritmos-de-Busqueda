# Algoritmos de Búsqueda en Espacios de Estados

El objetivo principal de este proyecto es implementar y comparar diferentes algoritmos de búsqueda en espacios de estados, aplicados al problema de escape de un laberinto. 

Vas a poder visualizar y jugar con los distintos algoritmos gracias a la libreria PyGame como se muestra a continuación:

![image](https://github.com/FrancoCalcia/Algoritmos-de-Busqueda/assets/136127479/acb6395c-5d75-426c-9fa5-170ff052c675)

## Descripción del Proyecto
### Primer parte:
Se implementaron los siguientes algoritmos de búsqueda:

- **Búsqueda en Anchura (BFS)**
- **Búsqueda en Profundidad (DFS)**
- **Búsqueda de Costo Uniforme (UCS)**
- **Búsqueda Avara Primero el Mejor (GBFS)**
- **Búsqueda A***

Todos estos algoritmos se implementaron en su versión de grafo, manteniendo en memoria los estados ya alcanzados para evitar caminos redundantes.

### Segunda parte:
Se implementó:
- **HillClimbing**
- **HillClimbingReset**
- **Busqueda Tabú**
  
Te invito a que pruebes todos los algoritmos creados.

## Ejecución del Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/FrancoCalcia/Algoritmos-de-Busqueda
   
2. Navega hacia la carpeta .\tp-pathfinding\ y ejecuta el siguiente comando:
   ```bash
   pip install -r requirements.txt
   
3. Ejecutar el programa:
   ```bash
   python3 run.pyw
   
4. Repetir paso '2' pero para la carpeta .\tp-tsp\

5. Ejecutar el programa:
  ```bash
   python3 main.py instances/ar24.tsp
   #'ar24.tsp' es uno de los tantos mapas que puedes ir probando. Te invito a que ejecutes los demas y veas la diferencia entre ellos
  ```
## Requerimientos
* Python 3.10 o superior (https://www.python.org/downloads/).
* Pygame.

