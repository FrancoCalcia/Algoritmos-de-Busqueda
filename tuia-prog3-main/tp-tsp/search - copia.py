"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem
from random import choice
from time import time
import random



class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def __init__(self):
        """
        Construye una instancia de la clase.
        """
        super().__init__()
        self.maximo = None

    def random_reset(self, problem: OptProblem, p_reset = .15):
        # Reinicio aleatorio con probabilidad p_reset
        if random.random() < p_reset:
            actual = problem.init
            value = problem.obj_val(problem.init)
            return (actual, value)
        return None


    def solve(self, problem: OptProblem):
        """
        Resuelve un problema de optimización con ascenso de colinas y reinicio aleatorio.
        Argumentos:
        problem (OptProblem): Un problema de optimización.
        """

        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:
            # Determinar las acciones que se pueden aplicar y las diferencias en valor objetivo
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_val = max(diff.values())
            max_acts = [act for act, val in diff.items() if val == max_val]

            # Elegir una acción aleatoria
            act = choice(max_acts)

            # Incrementar el contador de iteraciones en cada iteración del bucle
            self.niters += 1

            # Si se alcanza un óptimo local (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:
                self.tour = actual
                self.value = value
                end = time()
                self.time = end - start

                # Realizar reinicio aleatorio con cierta probabilidad
                probabilidad = self.random_reset(problem)
                if probabilidad:
                    actual, value = probabilidad
                else:
                    return

            # Sino, nos movemos al sucesor
            else:
                actual = problem.result(actual, act)
                value = value + diff[act]


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        mejor = actual
        value = problem.obj_val(problem.init)
        tabu = []

        while True:
            
            for a in problem.actions(actual):
                sucesores = problem.result(actual,a)
                for sucesor in sucesores:
                    if sucesor is not tabu:
                        no_tabues = sucesor
            
            diff = problem.val_diff(no_tabues)
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            #diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
           # max_acts = [act for act, val in diff.items() if val ==
              #          max(diff.values())]

            # Elegir una accion aleatoria
            #act = choice(max_acts)

            if problem.obj_val(mejor) < problem.obj_val(diff):
                mejor = diff
            
            tabu=mejor
            actual = diff
            return mejor
            # Retornar si estamos en un optimo local
            # (diferencia de valor objetivo no positiva)
            #if diff[act] <= 0:

             #   self.tour = actual
              #  self.value = value
               # end = time()
                #self.time = end-start
                #return

            # Sino, nos movemos al sucesor
            #else:

#                actual = problem.result(actual, act)
 #               value = value + diff[act]
  #              self.niters += 1
