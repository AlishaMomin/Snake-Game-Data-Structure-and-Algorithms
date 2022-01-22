import pygame,time,random,sys
pygame.init()
pygame.time.Clock()
pygame.display.set_caption('DSA Project Snake Game')

white, yellow, black = (255, 255, 255), (255, 255, 102), (0, 0, 0),
red, green, blue = (213, 50, 80), (0, 255, 0), (50, 153, 213)

screen_set = pygame.display.set_mode((600, 400))
Font, Score = pygame.font.SysFont(
    "bahnschrift", 25), pygame.font.SysFont("comicsansms", 35)
# 

def gameLoop():
    end_game =  False
    number1, number2, change_in_n1, change_in_n2, snake_length = (600 / 2), (400 / 2), 0, 0, 1
    warn_num=0
    list_of_snake = []
    appleA = round(random.randrange(0, 590) / 10.0) * 10.0
    appleB = round(random.randrange(0, 390) / 10.0) * 10.0
    flag=False
   
    while not False:
        
        while end_game == True:
            screen_set.fill(black)
            screen_set.blit(Font.render("You Lost! Press C to Play Again or Q to Quit", True, red), [
                     600/6, 400/3])
            screen_set.blit(Score.render("Your Score: " +str(snake_length-1)+"; Warning Seconds: "+str(warn_num)+"s", True, red), [0, 0])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_in_n1, change_in_n2 = -10, 0
                elif event.key == pygame.K_RIGHT:
                    change_in_n1, change_in_n2 = 10, 0
                elif event.key == pygame.K_UP:
                    change_in_n2, change_in_n1 = -10, 0
                elif event.key == pygame.K_DOWN:
                    change_in_n2, change_in_n1 = 10, 0
            if number1 >= 590 or number1 < 10 or number2 >= 390 or number2 < 10:
                flag = True
            else:
                flag = False
            

        #########
        checker = number1 >= 600 or number1 < 0 or number2 >= 400 or number2 < 0
        if checker:
            end_game = True
        number1 = number1 + change_in_n1
        number2 = number2 + change_in_n2
        pygame.display.set_mode((600, 400)).fill(black)
        pygame.draw.rect(pygame.display.set_mode(
            (600, 400)), red, [appleA, appleB, 10, 10])
        head = []
        head.append(number1), head.append(number2), list_of_snake.append(head)
        check = len(list_of_snake) > snake_length
        if check:
            del list_of_snake[0]
        for ele in list_of_snake[:-1]:
            if ele == head:
                end_game = True
        for val in list_of_snake:
            pygame.draw.rect(screen_set, white, [val[0], val[1], 10, 10])

        screen_set.blit(Score.render("Your Score: " +
                                   str(snake_length-1), True, yellow), [0, 0])
        if flag==True and end_game == False:
                screen_set.blit(Font.render("Warning", True, red), [
                     600/2, 400/2])
                warn_num+=1

                
                pygame.display.update()
                
        pygame.display.update()

        if number1 == appleA and number2 == appleB:
            appleA, appleB = round(random.randrange(0, 590) / 10.0) * 10.0, round(random.randrange(
                0, 390) / 10.0) * 10.0
            snake_length += 1

        pygame.time.Clock().tick(10)

    pygame.quit()
    quit()


gameLoop()
