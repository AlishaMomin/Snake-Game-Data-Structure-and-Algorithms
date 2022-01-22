# Snake-Game-Data-Structure-and-Algorithms
## Project name:
Snake game 
## Group members: 
1. Alisha Momin
2. Zain-ul-haq
3. Mustafa Usman 
## Power point presentation link: 
https://prezi.com/view/zr5Auapxi3x45ssx1RqP/ 
## Project Idea:
The idea of Snakes' same is very basic. The snake eats large flashing dots called "energizers" in an area. The length of the snake increases proportionally with the energizers eaten by the snake. All the snake has to do is to avoid hitting the boundaries in the area and avoid hitting its own body.
## Libraries: 
Pygame, randrange, sys, deepcopy, time, os.environ, math
Randrange: It generate random numbers from a specified range and also allowing rooms for steps to be included
Sys: The sys module provides information about constants, functions and methods of the Python interpreter.
Deepcopy: In this, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
Os.environ: In Python, it is a mapping object that represents the user’s environmental variables. It returns a dictionary having user’s environmental variable as key and their values as value.
## Challenges faced: 
In starting, we were unable to figure out how snake will find the shortest path using BFS algorithm in 612 x 612 display. Then we created a grid of 17 rows and 17 columns which helped us a lot and make things easier to find the shortest path using this grid. Using this grid, the length of the apple is 1 box of that grid and the length of the snake is increased by 1 box every time it eat an apple. The grid formation makes things easier to apply BFS algorithm on it. 
## Project outcome:
Snake game figures out how to locate a short and straight-forward arrangement to find the food. We would be using graph algorithm for finding foods from the shortest path (i.e. BFS). First we compare the BFS and DFS efficiency from which we get to know that BFS beats DFS by a shorter path. BFS finds the most limited length arrangement, however forfeits space as it grows each nodes in the search space. Secondly we have created a manual snake game which ask user to play the game through which we figured out the warning alerts every time it is near the border. This is implemented using Flag and other DSA algorithm, which will be discussed below. 
## Project goal and time complexity: 
Our goal for the project was to compare the time complexity between user player and automatic snake game. Over here we figured out that automatic game has less time complexity as compare to user player because in automatic snake game, we used BFS algorithm which find the shortest path for snake to reach his food while in user player snake game, the time complexity depends on user input. We figured out that in automatic snake game is more efficient as compare to user player and  the time complexity of automatic snake game is O(V+E) where V is vertices and E is edges. 
## Project description: 
Firstly we have asked user to give the input. Whether he/she wanted to play the snake game by itself or wants to watch snake to eat the food automatically. 
1.	If the user has given the input == userplayer:
The user will give the direction to snake. If snake hits its body or the border of the display, the game will be over. Else user continue to play the game which means it will eat the food. Once snake has eat the food then the length of snake will be increased by 1 as well as its score. Over here we have also alerted the user if he is near the border. It will show the WARNING sign as well the time till when the user is at warning area.
2.	If the user has given the input == Automatic: 
In this game, the snake will be find the shortest path using BFS algorithm to find the shortest distance the head of the snake and the food and we will name it path1. If this path1 is available then we have created a virtual snake which is identical to the real snake and this will follow the path1. After that, once the virtual snake has reached the apple then we will check the path between the tail and the head of snake is available or not and let’s name it path2. If the path2 is available then we will give instruction to the real snake to follow the footsteps of path1. 
If the path1 or path2 or both are not available then we will give direction to the real snake to follow the tail of the snake.
## Algorithm for userplayer: 
1.	Initialization: (setting up the basic framework, defining variables and functions.)
    1.	Importing python libraries i.e. pygame, time, random, sys
    2.	Initializing clock : “pygame.time.Clock()
    3.	Defining the RGB codes and storing them in variables
    4.	Initializing screen dimension of our game i.e. “(600,400)”
    5.	Setting up the font style and size, fonts used : “bahnschrift” and “comicsansms”
    6.	Defining the main function : “def gameLoop():”
    7.	Setting up x-pos and y-pos of our snake “x-pos= (600 / 2), y-pos= (400 / 2)”
    8.	Setting up delta x and delta y == 0
    9.	Initial snake length = 1
    10.	Random x & y pos for apple generation: “round(random.randrange(initial x or y, final x or y) / 10.0) * 10.0”
    11.	Flags for end_game and warning == False
2.	Main Loop:
    1.	While game_end is not == False, causing the loop to run until collisions
        Any heading proceeding this would be nested in this main loop.
        I.	Mapping of keys as Input:
        * For event in pygame.event.get (): -- to initiate the loop for any event during game
        * If event.key == pygame.K_specified_key:
        * In case on ‘q’ pygame would be forced to quit the game,    * pygame.quit ()
        *In case of ‘c’ recursive function would be called upon to restart the game.
        * In case of any arrow key change_in_xpos and change_in_ypos would be given value either (10,-10, 0) to infer change in direction.
        II.	Collisions:
        To account for collisions flags has been used
        For border collision:
        If number 1 >= 600 or <0 similarly if number2 >= 400 or <0: “end_game = True”
                    For self-collision:
        Snake_list contains the changes in xpos and ypos as snake eats apple, head denotes the very first tuple pos of snake
                      For i in snake¬¬_list [:-1]:
                        If i == head:
                          End_game == True
                    Warning generator:
        If snake in a certain region of the screen i.e. 10 units smaller or greater than the initial and final xpos and ypos a flag would be switched True
    2.	Output:
        1.	“pygame.display.set_mode((600, 400)).fill(black)” – producing background
        2.	Using the random x and y from apple_genertaion to produce rect on screen
        3.	Iterating over Snake_list to produce snake using the similar pygame.draw.rect  command
        4.	In case of end_game == False, produces score (number of apples eaten) and amount of time spent in warning area.
    3.	Clock manuplation:
    Finally it’s time for clock to be manipulated to control speed.
## Algorithm for automatic: 
#### Class square:
This function is responsible for the change in the direction of snake a directory with a tuple of pos indicate change in direction in case of striking a direction key i.e. (1,0)(0,1)(-1,0)(0,-1) Upon each strike the program would draw a rectangle in the similar direction. To keep the snake moving: Pos of snake keeps getting updated by adding the dir_snake which basically is the next immediate state of snake in terms of dir, it grow literally by a unit of one. In case of change in dir dir_snake would change respectively according to the above stated program.
Collision:
A very basic flag/checker system is put up, which determines if the pos of snake in in the playable region else a false statement is returned which would end the game

#### Class Snake: 
This class is responsible for the generation of food, snake, finding the shortest path to the tail, head, and apple. In this class we have also used BFS algorithm to find the shortest path between food and the head of the snake. 
def draw(self):
	Basically, this function initially draw the apple and snake 
	1. step1: give the color code to apple and head of the snake. 
	
	2. step2: for every i in self.squares [1:] it will draw the apple and snake.
Def set_direction (self, direction):
	Basically, this function will check the directions and will return the coordinates according to the given position. 
	1. step1: it will check the position.
	
	2. step2: it will return the direction at a given coordinates.
Def handle_events (self):
	This function handles 2 events that is quit game and keyboard 
	1. step1: if the type of the event is QUIT then the pygame will be end and the display will be closed. 
	2. step2: else it will take the keyboard input. If the keyboard input is equal to the given position then it will return the position which will help snake to move according to the position direction.
Def add_square (self):
	This function append the snake tail by 1 every time it’s eat an apple.
Def reset (self):
	This function will restart the game 
Def hitting_self (self):
	1. step1: this function will check if the snake head hits any part of its body then game will be end.
	2. step2: else the game is continued to be played. 
Def generate_apple (self):
	For the first time we have created the apple in draw (self) but now after first time, we will be creating random apples at random places so for this we have created this function to generate apple randomly.
	1. step1: we will be generating apples in the range of 17 which is our row and column. 
	2. step2: it will check if the first apple is eaten by snake then it will create the next apple by following the step1 and so on.
Def eating_apple (self):
	This function will basically do 2 things. First when snake eat the food it will generate new apple. Secondly it will increase the score by 1 
	1. step1: it will check if the snake head is equal to apple then it will generate a new apple by calling the above generate_apple function.
	2. step2: once it has generated a new apple then it will increase the score by 1.
Def go_to (self, position):
	This function is basically set the direction of head to the position of target. We have used BFS algorithm which we have done in labs. Lastly we have few more functions which is given below.
Def get_available_neighbors (self, pos):
	This function uses get_neighbours to attain all possible neighbours, then check whether those locations are free "if self.is_position_free(i): if the condition comes out to be true, a list containing tuple location of all available neighbours gets updated.
Def longest_path_to_tail (self):
	This functions checks the path from head of the snake to the apple being generated, maximum distance for the ease of coding is hard coded and set to -9999, finding the possible paths, a variable named path gets updated on each iteration over the neighbours and gets returned at the end.
Def any_safe_move (self):
	Basically there's a limit to the snake size in relation to its movement and dimension of screen, maximum size of snake in which a path could be find in 285, in case of length of snake being equal to the limit a path is laid out towards the tail of the snake in order to restart the game.
#### MAIN GAME:
This Takes two function which will call the above classes and plays the whole game.
Def screen_fill (surface):
	This function is filling the color to the display. 
Def play_game ():
	This function is the main function because the whole game is run by using this function. This function is doing the multiple tasks. it is checking the game is to be quit or to be played both at the same time.
	1. step1: we have initialized the pygame by using pygame.init and then caption our display screen which is DSA Final project Snake Game.
	2. step2: the game is running at the speed of 50 as we have used the pygame.time.Clock ().tick function.
	3. step3: first it will check if the gameLoop is true (which means if the snake has not collided with its body or wall then gameLoop==true) then it will call the above classes and function to run the game. And every time it will update the screen after we have called the above class. This will show the new movement of snake. 
	4. step4: if the gameLoop==false then will stop the game and our pygame display will be closed.
	
	

