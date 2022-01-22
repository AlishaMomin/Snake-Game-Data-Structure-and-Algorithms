# #ALISHA="
from os import environ
import pygame
import sys
from copy import deepcopy
from random import randrange

SURFACE_CLR= (15, 15, 15) #display color 
GRID = [[val, ele] for val in range(17) for ele in range(17)]
def push(lst,item):
    lst.append(item)
def get_neighbors(position):
    A,B=position[0],position[1]
    neigh, stacks= [[A+1,B],[A-1,B],[A,B+1],[A,B-1]] , []
    for i in neigh:
        if i in GRID: push(stacks,i)
    return (stacks)
def distance(A1, A2):
    a1, a2,b1, b2 = A1[0], A2[0],A1[1], A2[1]
    adding1= abs(a2 - a1)
    adding2=abs(b2 - b1)
    return(adding1+adding2)
ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
# "
# --------------------------------------------------------



class Square:
    def __init__(self, pos, surface, is_apple=False):
        self.pos,self.surface,self.is_apple,self.is_tail,self.dir = pos,surface,is_apple,False,[-1, 0] 
        if self.is_apple:
            self.dir = [0, 0]

    def draw(self, clr=(50, 255, 50)):
        x, y = self.pos[0], self.pos[1]
        if self.dir == [-1, 0]:
            if self.is_tail:pygame.draw.rect(self.surface,(50, 255, 50), (x*36+2 , y*36+2, 36-2*2, 36-2*2))
            pygame.draw.rect(self.surface,(50, 255, 50),(x*36+2 , y*36+2 , 36, 36-2*2))

        if self.dir == [1, 0]:
            if self.is_tail:pygame.draw.rect(self.surface,(50, 255, 50),(x*36+2, y*36+2, 36-2*2, 36-2*2))
            pygame.draw.rect(self.surface,(50, 255, 50),(x*36-2, y*36+2, 36, 36-2*2))

        if self.dir == [0, 1]:
            if self.is_tail:pygame.draw.rect(self.surface, (50, 255, 50), (x*36+2, y*36+2, 36-2*2, 36-2*2))
            pygame.draw.rect(self.surface, (50, 255, 50),(x*36+2, y*36-2, 36-2*2, 36))
        if self.dir == [0, -1]:
            if self.is_tail:pygame.draw.rect(self.surface, (50, 255, 50), (x*36+2, y*36+2, 36-2*2, 36-2*2))
            pygame.draw.rect(self.surface, (50, 255, 50),(x*36+2, y*36+2, 36-2*2, 36))
        if self.is_apple:
            pygame.draw.rect(self.surface, clr, (x*36+2,y*36+2, 36-2*2, 36-2*2))

    def move(self, direction):
        self.dir = direction
        self.pos[0] , self.pos[1] = self.pos[0]+self.dir[0] , self.pos[1]+self.dir[1]

    def hitting_wall(self):
        A=(self.pos[0] <= -1)
        B=(self.pos[0] >= 17)
        C=(self.pos[1] <= -1)
        D=(self.pos[1] >= 17)
        if A or B or C or D:
            return True
        return False

# ---------------------------------------------------------------------------------------
class Snake:
    def __init__(self, surface):
        self.surface,self.is_dead  = surface,False
        self.squares_start_pos = [[17 // 2 + i, 17 // 2] for i in range(3)]
        self.turns,self.dir,self.score,self.moves_without_eating = {},[-1, 0],0,0
        self.apple,self.squares = Square([randrange(17), randrange(17)],self.surface, is_apple=True), []
        for val in self.squares_start_pos:
            push(self.squares,(Square(val, self.surface)))
            

        self.head,self.tail,self.tail.is_tail   = self.squares[0],self.squares[-1],True
        self.path,self.is_virtual_snake,self.total_moves,self.won_game = [],False,0,False
        
# ALISHA="
    def draw(self):
        self.apple.draw((255, 255, 0)) #yellow 
        self.head.draw((0, 150, 0)) #green
        for sqr in self.squares[1:]: 
            if self.is_virtual_snake:   #self.is_virtual_snake=false
                sqr.draw((255, 0, 0))
            sqr.draw()

    def set_direction(self, direction):
        A=self.head.pos[0], self.head.pos[1]
        if direction == 'left':
            if self.dir != [1, 0]:
                self.dir = [-1, 0]
                self.turns[A] = self.dir
        if direction == "right":
            if self.dir != [-1, 0]:
                self.dir = [1, 0]
                self.turns[A] = self.dir
        if direction == "up":
            if self.dir != [0, 1]:
                self.dir = [0, -1]
                self.turns[A] = self.dir
        if direction == "down":
            if self.dir != [0, -1]:
                self.dir = [0, 1]
                self.turns[A] = self.dir

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for _ in pygame.key.get_pressed():
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.set_direction('left')
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.set_direction('right')
                if pygame.key.get_pressed()[pygame.K_UP]:
                    self.set_direction('up')
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.set_direction('down')
# "
    def move(self):
        B=self.squares
        for j, sqr in enumerate(B):
            p = (sqr.pos[0], sqr.pos[1])
            if p in self.turns:
                turn = self.turns[p]
                A=[turn[0], turn[1]]
                sqr.move(A)
                if j == len(B)-1:self.turns.pop(p)
            else:sqr.move(sqr.dir)
        self.moves_without_eating = self.moves_without_eating+ 1
# -----------------------------------------------------------------------------------
    def add_square(self):
        self.squares[-1].is_tail = False
        tail = self.squares[-1] 
        direction = tail.dir
        A=self.surface
        F=self.squares
        B=tail.pos[0]
        C=tail.pos[1]
        Z,Y,X,W=[1, 0],[-1, 0],[0, 1],[0, -1]
        if direction == Z:
            push(F,(Square([B-1, C], A)))
        if direction == Y:
            push(F,(Square([B+1, C], A)))
        if direction == X:
            push(F,(Square([B, C-1], A)))
        if direction == W:
            push(F,(Square([B, C+1], A)))
        H=self.squares[-1]
        H.dir , H.is_tail = direction,True  #it will create a tail after adding every new squares (grid)
# Alisha="
    def reset(self):
        self.__init__(self.surface)

    def hitting_self(self):
        A=self.squares[1:]
        for sqr in A:
            Z=self.head.pos
            Y=sqr.pos
            if  Z== Y:return True

    def generate_apple(self):
        A=self.surface
        B=[randrange(17), randrange(17)]
        self.apple = Square(B,A, is_apple=True)
        C=self.is_position_free(self.apple.pos)
        if not C: 
            D=self.generate_apple()
            return D

    def eating_apple(self):
        A=self.head.pos
        B=self.apple.pos 
        if  A== B:
            if not False :
                self.generate_apple()
                self.moves_without_eating , self.score = 0,self.score+1
                return True
    def go_to(self, position):  # this function is basically Set the direction of head to the position of target
        A=self.head.pos[0]
        B=self.head.pos[1]
        C=position[0]
        D=position[1]
        if  A- 1 == C:self.set_direction('left')
        if A + 1 == C:self.set_direction('right')
        if B - 1 == D:self.set_direction('up')
        if B + 1 == D:self.set_direction('down')
# "
    def is_position_free(self, position):
        A=position[0] >= 17
        B=position[0] < 0 
        C=position[1] >= 17
        D=position[1] < 0
        Z=self.squares
        if A or B or C or D: return False
        for i in Z:
            Y=i.pos
            X=position
            if Y == X:return False
        return True
# ----------------------------------------------------------------------------------------------------------
    def bfs(self, s, e):
        q = [s]
        visited,visited[s] = {tuple(i): False for i in [[val, ele] for val in range(17) for ele in range(17)]},True
        prev = {tuple(i): None for i in [[val, ele] for val in range(17) for ele in range(17)]}
        while q:  
            node = q.pop(0)
            A = ADJACENCY_DICT[node]
            for i in A:
                if self.is_position_free(i):
                    if not visited[tuple(i)]:
                        push(q,tuple(i))
                        visited[tuple(i)], prev[tuple(i)] = True,node
        path , p_node= [] , e
        while not False:
            Z=prev[p_node]
            if Z==None: return []
            p_node = Z
            if s ==Z:
                push(path,e)
                return path
            path.insert(0, Z)

        return [] 
    def create_virtual_snake(self): #create the snake copy (from direction,size,position,moves)
        v_snake = Snake(self.surface)
        A=len(self.squares) - len(v_snake.squares)
        for i in range(A):
            v_snake.add_square()
        Z=enumerate(v_snake.squares)
        for i, sqr in Z:
            sqr.pos,sqr.dir = deepcopy(self.squares[i].pos),deepcopy(self.squares[i].dir)
        v_snake.dir,v_snake.turns,v_snake.apple.pos = deepcopy(self.dir),deepcopy(self.turns),deepcopy(self.apple.pos)
        v_snake.apple.is_apple , v_snake.is_virtual_snake= True , True

        return v_snake

    def get_path_to_tail(self): #using bfs function we are finding the path to the tail
        A=self.squares
        tail_pos = deepcopy(A[-1].pos)
        A.pop(-1)
        path = self.bfs(tuple(self.head.pos), tuple(tail_pos))
        self.add_square()
        return path

    def get_available_neighbors(self, pos): 
        valid_neighbors , neighbors = [],get_neighbors(tuple(pos))
        for i in neighbors:
            if self.is_position_free(i):
                if not self.apple.pos == i:
                    push(valid_neighbors,(tuple(i)))
        return valid_neighbors

    def longest_path_to_tail(self):
        neighbors , path= self.get_available_neighbors(self.head.pos) ,[]
        if neighbors:
            dis = -9999
            for n in neighbors:
                B=self.squares
                if distance(n, B[-1].pos) >  -9999:
                    self.create_virtual_snake().go_to(n)
                    self.create_virtual_snake().move()
                    if self.create_virtual_snake().eating_apple():
                        self.create_virtual_snake().add_square()
                    if self.create_virtual_snake().get_path_to_tail():
                        push(path,n)
                        dis = distance(n, B[-1].pos)
            if path:
                A=[path[-1]]
                return A

    def any_safe_move(self):
        path =[]
        if self.get_available_neighbors(self.head.pos):
            push(path,(self.get_available_neighbors(self.head.pos)[randrange(len(self.get_available_neighbors(self.head.pos)))]))
            for move in path:
                self.create_virtual_snake().go_to(move)
                self.create_virtual_snake().move()
            if self.create_virtual_snake().get_path_to_tail():
                return path
            else:
                return self.get_path_to_tail()

    def set_path(self):
        A=285
        if self.score == A:
            if self.apple.pos in get_neighbors(self.head.pos): 
                print('Snake will win in a while')
                return [tuple(self.apple.pos)]
        path_1 = self.create_virtual_snake().bfs(tuple(self.create_virtual_snake().head.pos), tuple(self.create_virtual_snake().apple.pos))
        path_2 = []
        if path_1:
            for pos in path_1:
                self.create_virtual_snake().go_to(pos)
                self.create_virtual_snake().move()
            self.create_virtual_snake().add_square() 
            path_2 = self.create_virtual_snake().get_path_to_tail()
        if path_2: return path_1
        if self.longest_path_to_tail():
            if self.score % 2 == 0:
                if self.moves_without_eating < 4913:
                    return self.longest_path_to_tail()
        if self.any_safe_move():
            return self.any_safe_move()
        if self.get_path_to_tail():
            return self.get_path_to_tail()
        print('Path is not available which indicates the danger!')

    def update(self):
        self.handle_events()
        if self.set_path():
            self.go_to(self.set_path()[0])
        self.draw()
        self.move()
        if self.score == 286:
            self.won_game = True
            print("The game is won by snake after {} moves".format(self.total_moves))
            pygame.time.wait(15000)
            return 1
        self.total_moves = self.total_moves+1
        if self.hitting_self() or self.head.hitting_wall():
            print("The game is over because Snake is dead. Please trying again")
            self.is_dead = True
            self.reset()
        if self.moves_without_eating == 9826:
            self.is_dead = True
            print("snake is stuck. please help him by restarting the game!")
            self.reset()
        if self.eating_apple():
            self.add_square()
# ------------------------------------------------------------------------------ #ALISHA:
def screen_fill(surface):
    surface.fill(SURFACE_CLR)
def play_game():
    pygame.init() 
    pygame.display.set_caption("DSA Final project Snake Game")
    clock,snake,gameloop = pygame.time.Clock(), Snake(pygame.display.set_mode((700, 700))),True
    while gameloop:
        screen_fill(pygame.display.set_mode((700, 700)))
        snake.update()
        clock.tick(50)
        pygame.display.update()
play_game()