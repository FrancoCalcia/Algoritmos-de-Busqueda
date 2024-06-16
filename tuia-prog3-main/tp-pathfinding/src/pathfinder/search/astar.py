from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class AStarSearch:
    @staticmethod
    def heuristic(state, goal):
        """Calcula la distancia Manhattan entre el estado actual y el objetivo.
        
        Args:
            state (tuple): Coordenadas del estado actual.
            goal (tuple): Coordenadas del estado objetivo.
        
        Returns:
            int: Distancia Manhattan entre el estado actual y el objetivo.
        """
        x1, y1 = state
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def search(grid: Grid) -> Solution:
       
        # Inicializar un nodo con la posición inicial
        node = Node("", state=grid.start, cost=0, parent=None, action=None)
        
        # Inicializar la frontera como una cola de prioridad y agregar el nodo inicial con su costo + heurística
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost + AStarSearch.heuristic(node.state, grid.end))

        # Diccionario para rastrear los costos mínimos para alcanzar cada estado
        reached = {node.state: node.cost}
       
        while not frontier.is_empty():
            # Extraer el nodo con el costo + heurística más bajo de la frontera
            node = frontier.pop()
            
            # Si el nodo actual es el estado objetivo, retornar la solución
            if node.state == grid.end:
                return Solution(node, reached)
           
            # Obtener los sucesores del estado actual
            successors = grid.get_neighbours(node.state)
            
            # Evaluar cada sucesor
            for i, new_state in successors.items():
                # Calcular el nuevo costo para llegar al sucesor
                new_cost = node.cost + grid.get_cost(new_state)
                
                # Si el sucesor no ha sido alcanzado o se encuentra un camino más barato, procesar el sucesor
                if new_state not in reached or new_cost < reached[new_state]:
                    # Crear un nuevo nodo para el sucesor
                    new_node = Node("", new_state, new_cost, parent=node, action=i)
                    
                    # Actualizar el costo mínimo para alcanzar este nuevo estado
                    reached[new_state] = new_cost
                    
                    # Agregar el nuevo nodo a la frontera con su costo + heurística
                    frontier.add(new_node, new_cost + AStarSearch.heuristic(new_state, grid.end))
        
        # Si la frontera se vacía sin encontrar una solución, retornar NoSolution
        return NoSolution(reached)
