from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        # Crear el nodo inicial con el estado inicial de la grilla, costo 0, sin padre ni acción
        node = Node("", state=grid.start, cost=0, parent=None, action=None)
        
        # Inicializar la frontera como una cola de prioridad y agregar el nodo inicial con su costo
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)     
        
        # Diccionario para rastrear los costos mínimos para alcanzar cada estado
        reached = {node.state: node.cost}
       
        while not frontier.is_empty():
            # Extraer el nodo con el costo más bajo de la frontera
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
                    
                    # Agregar el nuevo nodo a la frontera con su costo
                    frontier.add(new_node, new_cost)
        
        # Si la frontera se vacía sin encontrar una solución, retornar NoSolution
        return NoSolution(reached)
