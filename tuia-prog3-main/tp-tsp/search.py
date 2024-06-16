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
    """Algoritmo de ascension de colinas con reinicio aleatorio.

    Cuando se llega a un optimo local se reinicia aleatoriamente.
    """


    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas de reseteo aleatorio.

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

        mejor_estado_encontrado = None
        mejor_valor_encontrado = None

        for i in range(7):

            while True:

                # Determinar las acciones que se pueden aplicar
                # y las diferencias en valor objetivo que resultan
                diff = problem.val_diff(actual)

                # Buscar las acciones que generan el mayor incremento de valor obj
                max_acts = [act for act, val in diff.items() if val ==
                            max(diff.values())]

                # Elegir una accion aleatoria
                act = choice(max_acts)


                # Reiniciar si estamos en un optimo local
                # (diferencia de valor objetivo no positiva)
                if diff[act] <= 0:

                    if mejor_valor_encontrado == None or value > mejor_valor_encontrado:
                        mejor_valor_encontrado = value
                        mejor_estado_encontrado = actual

                    self.tour = mejor_estado_encontrado
                    self.value = mejor_valor_encontrado
                    end = time()
                    self.time = end-start
                    break

                # Sino, nos movemos al sucesor
                else:

                    actual = problem.result(actual, act)
                    value = value + diff[act]
                    self.niters += 1
            actual = problem.random_reset()
            value = problem.obj_val(actual)


class Tabu(LocalSearch):
    """Algoritmo de búsqueda tabú."""

    def solve(self, problem: OptProblem):
        
        # Inicio del reloj
        start = time()

        # Estado inicial
        actual = problem.init
        mejor = actual
        mejor_valor = problem.obj_val(actual)

        # Tabú como un conjunto de estados
        tabu = []
        tabu_max_size = 5

        # Número máximo de iteraciones
        max_iteraciones = 18
        max_iteraciones_malas = max_iteraciones // 2

        iteraciones = 0
        iteraciones_malas = 0

        while iteraciones < max_iteraciones:
            iteraciones += 1
            self.niters += 1

            # Determinar sucesores no tabúes
            sucesores_no_tabu = []
            for a in problem.actions(actual):
                sucesor = problem.result(actual, a)
                if sucesor not in tabu:
                    sucesores_no_tabu.append(sucesor)

            valores_objetivos = []
            for s in sucesores_no_tabu:
                valores_objetivos.append(problem.obj_val(s))


            # Encontrar el mejor sucesor no tabú
            mejor_sucesor = sucesores_no_tabu[valores_objetivos.index(max(valores_objetivos))]
            mejor_valor_sucesor = max(valores_objetivos)

            # Actualizar la mejor solución global
            if mejor_valor_sucesor > mejor_valor:
                mejor = mejor_sucesor
                mejor_valor = mejor_valor_sucesor
                iteraciones_malas = 0
            else:
                iteraciones_malas +=1
                if iteraciones_malas >= max_iteraciones_malas:
                    break

            # Actualizar la lista tabú
            tabu.append(mejor_sucesor)
            if len(tabu) >= tabu_max_size:
                tabu.pop(0)

            # Actualizar el estado actual para el siguiente ciclo
            actual = mejor_sucesor

    # Almacenar la mejor solución encontrada y su valor
        self.tour = mejor
        self.value = mejor_valor

        # Finalizar el temporizador
        end = time()
        self.time = end - start