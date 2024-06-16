from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        
        # Inicializar un nodo con la posición inicial
        node = Node("", state=grid.start, cost=0, parent=None, action=None)
        
        # Inicializar el diccionario de alcanzados para rastrear los estados visitados
        reached = {}
        reached[node.state] = True

        # Si el nodo inicial es el estado objetivo, retornar la solución inmediatamente
        if node.state == grid.end:
            return Solution(node, reached)

        # Inicializar la frontera como una pila
        frontier = StackFrontier()
        frontier.add(node)

        while not frontier.is_empty():
            # Extraer el nodo más reciente de la frontera
            node = frontier.remove()
            
            # Obtener los sucesores del estado actual
            successors = grid.get_neighbours(node.state)
            
            # Evaluar cada sucesor
            for i in successors:
                new_state = successors[i]
                
                # Si el sucesor no ha sido alcanzado, procesarlo
                if new_state not in reached:
                    # Crear un nuevo nodo para el sucesor
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state), parent=node, action=i)
                    
                    # Marcar el sucesor como alcanzado
                    reached[new_state] = True
                    
                    # Si el sucesor es el estado objetivo, retornar la solución
                    if new_state == grid.end:
                        return Solution(new_node, reached)
                    
                    # Agregar el nuevo nodo a la frontera
                    frontier.add(new_node)
        
        # Si la frontera se vacía sin encontrar una solución, retornar NoSolution
        return NoSolution(reached)
