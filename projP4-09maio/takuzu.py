# takuzu.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2


import sys

from numpy import size


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
    def __init__(self,positions,size):
        self.positions=positions
        self.size=size

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        # TODO
        return self.positions[row][col]

    def set_number(self,row,col,number):
        self.positions[row][col]=number

    def get_columns(self):
        columns=[]
        for col in range(self.size):
            column=[]
            for row in range(self.size):
                column.append(self.positions[row][col])
            columns.append(column)
        return columns
    
    def adjacent_vertical_up(self,row,col):
        if row==1:
            return (None,self.get_number(row-1,col))
        elif row>1:
            return (self.get_number(row-2,col),self.get_number(row-1,col))
        else:
            return (None,None)
    
    def adjacent_vertical_down(self,row,col):
        size=self.size
        if row==size-2:
            return (self.get_number(row+1,col),None)
        elif row<size-2:
            return(self.get_number(row+1,col),self.get_number(row+2,col))
        else:
            return (None,None)
    
        

    def adjacent_vertical_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        # TODO
        size=self.size
        if(row==0):
            return (self.get_number(row+1,col),None)
        elif(row==size-1):
            return (None,self.get_number(row-1,col))
        else:
            return (self.get_number(row+1,col),self.get_number(row-1,col))


    def adjacent_horizontal_left(self,row,col):
        if col==1:
            return (None,self.get_number(row,col-1))
        elif col>1:
            return (self.get_number(row,col-2),self.get_number(row,col-1))
        else:
            return (None,None)
        
    def adjacent_horizontal_right(self,row,col):
        size=self.size
        if col==size-2:
            return (self.get_number(row,col+1),None)
        elif col<size-2:
            return (self.get_number(row,col+1),self.get_number(row,col+2))
        else:
            return (None,None)



    def adjacent_horizontal_numbers(self, row: int, col: int) -> (int, int):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO
        size=len(self.positions)
        if(col==0):
            return (None,self.get_number(row,col+1))
        elif(col==size-1):
            return (self.get_number(row,col-1),None)
        else:
            return (self.get_number(row,col-1),self.get_number(row,col+1))
    
    def copy(self):
        positions_copy=[]
        for row in self.positions:
            copy_row=[]
            for col in row:
                copy_row.append(col) 
            positions_copy.append(copy_row)
        return Board(positions_copy,self.size)

    def all_lines_different(self):
        for i in range(0,self.size):
            if(self.positions[i] in self.positions[i+1:]):
                return False
        return True

    def all_columns_different(self):
        columns=self.get_columns()
        for i in range(0,self.size):
            if(columns[i] in columns[i+1:]):
                return False
        return True

    def has_more_than_two_equal_adjacent(self):
        for row in range(self.size):
            for col in range(self.size):
                number=self.get_number(row,col)
                adj_ver=self.adjacent_vertical_numbers(row,col)
                adj_hor=self.adjacent_horizontal_numbers(row,col)
                if((number==adj_ver[0] and number==adj_ver[1]) or (number==adj_hor[0] and number==adj_hor[1]) or number==2):
                    return True
        return False
    
    def has_equal_number_elements_lines(self):
        for row in self.positions:
            if(abs(row.count(0)-row.count(1))>1):
                return False
        return True

    def has_equal_number_elements_columns(self):
        columns=self.get_columns()
        for column in columns:
            if(abs(column.count(0)-column.count(1))>1):
                return False
        return True

    def get_size(self):
        return self.size
    

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
        size=int(sys.stdin.readline())
        for i in range(size):
            line_str=sys.stdin.readline()[:-1].split('\t')
            line=[int(i) for i in line_str]
            positions.append(line)
        return Board(positions,size)

    # TODO: outros metodos da classe

    def __str__(self) -> str:
        board_str=''
        for line in self.positions:
            line_str=[str(i) for i in line]
            board_str+='\t'.join(line_str)+'\n'
        return board_str


class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        self.initial=TakuzuState(board)

    def actions(self, state: TakuzuState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        actions=[]
        size=state.board.get_size()
        for row in range(size):
            for col in range(size):
                number=state.board.get_number(row,col)
                if number==2:
                    adj_ver=state.board.adjacent_vertical_numbers(row,col)
                    adj_hor=state.board.adjacent_horizontal_numbers(row,col)
                    adj_ver_u=state.board.adjacent_vertical_up(row,col)
                    adj_ver_d=state.board.adjacent_vertical_down(row,col)
                    adj_hor_l=state.board.adjacent_horizontal_left(row,col)
                    adj_hor_r=state.board.adjacent_horizontal_right(row,col)
                    if adj_ver[0]==adj_ver[1]==0 or adj_hor[0]==adj_hor[1]==0 or adj_ver_u[0]==adj_ver_u[1]==0 or adj_ver_d[0]==adj_ver_d[1]==0 or adj_hor_l[0]==adj_hor_l[1]==0 or adj_hor_r[0]==adj_hor_r[1]==0:
                        actions.append((row,col,1))
                    elif adj_ver[0]==adj_ver[1]==1 or adj_hor[0]==adj_hor[1]==1 or adj_ver_u[0]==adj_ver_u[1]==1 or adj_ver_d[0]==adj_ver_d[1]==1 or adj_hor_l[0]==adj_hor_l[1]==1 or adj_hor_r[0]==adj_hor_r[1]==1:
                        actions.append((row,col,0))
                    else:
                        actions.append((row,col,0))
                        actions.append((row,col,1))
                    break
            if(len(actions)!=0):
                break
                            
        return actions

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        board_copy=state.board.copy()
        board_copy.set_number(action[0],action[1],action[2])
        return TakuzuState(board_copy)


    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas com uma sequência de números adjacentes."""
        # TODO
        if(not state.board.has_more_than_two_equal_adjacent() and 
        state.board.all_lines_different() and 
        state.board.all_columns_different() and
        state.board.has_equal_number_elements_lines() and
        state.board.has_equal_number_elements_columns()):
            return True
        return False

                

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
    board = Board.parse_instance_from_stdin()
    # Criar uma instância de Takuzu:
    problem = Takuzu(board)
    
    # Obter o nó solução usando a procura em profundidade:
    goal_node = depth_first_tree_search(problem)
    # Verificar se foi atingida a solução
    print("Is goal?", problem.goal_test(goal_node.state))
    print("Solution:\n", goal_node.state.board, sep="")