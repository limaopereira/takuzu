# takuzu.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

import sys
import numpy


from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class TakuzuState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = TakuzuState.state_id
        TakuzuState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:

    """Representação interna de um tabuleiro de Takuzu."""
    def __init__(self,positions):
        self.positions=positions

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        # TODO
        return self.positions[row][col]

    def adjacent_vertical_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        # TODO
        size=len(self.positions);
        if(row==0):
            return (self.get_number(row+1,col),None)
        elif(row==size-1):
            return (None,self.get_number(row-1,col))
        else:
            return (self.get_number(row+1,col),self.get_number(row-1,col))


    def adjacent_horizontal_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO
        size=len(self.positions);
        if(col==0):
            return (None,self.get_number(row,col+1))
        elif(col==size-1):
            return (self.get_number(row,col-1),None)
        else:
            return (self.get_number(row,col-1),self.get_number(row,col+1))

    @staticmethod
    def parse_instance_from_stdin():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 takuzu.py < input_T01

            > from sys import stdin
            > stdin.readline()
        """
        positions=[]
        size=sys.stdin.readline()
        for i in range(int(size)):
            line_str=sys.stdin.readline().split('\t')
            line=[int(i) for i in line_str]
            positions.append(line)
        print(positions)
        return Board(positions)

    # TODO: outros metodos da classe


class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        pass

    def actions(self, state: TakuzuState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas com uma sequência de números adjacentes."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    board=Board.parse_instance_from_stdin()
    print("Initial:\n",board, sep="")
    
    print(board.adjacent_vertical_numbers(3,3))
    print(board.adjacent_horizontal_numbers(3,3))

    print(board.adjacent_vertical_numbers(1,1))
    print(board.adjacent_horizontal_numbers(1,1))