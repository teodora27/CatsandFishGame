import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(0,0),Vector2(1,0),Vector2(2,0)]
        self.direction = Vector2(0,1)
        self.new_block = False
        self.cat = pygame.image.load('C:\web\python idk\CATS GAME/pisica3.png').convert_alpha()

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos =  block.y * cell_size
            block_rect = pygame.Rect(x_pos,y_pos, cell_size,cell_size)
            #pygame.draw.rect(screen,(65,168,58),block_rect)
            screen.blit(self.cat,block_rect)

            
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body=body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body=body_copy[:]

    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        screen.blit(fish,fruit_rect)
        #pygame.draw.rect(screen,(236,43,43),fruit_rect)
    
    def randomise(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)

class BROTHER:
    def __init__(self):
        self.body = [Vector2(cell_number-1,cell_number-1),Vector2(cell_number-1,cell_number-2),Vector2(cell_number-1,cell_number-3)]
        self.direction = Vector2(0,-1)
        self.new_block1 = False
        self.cat = pygame.image.load('C:\web\python idk\CATS GAME/pisica4.png').convert_alpha()

    def draw_brother(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos =  block.y * cell_size
            block_rect = pygame.Rect(x_pos,y_pos, cell_size,cell_size)
            #pygame.draw.rect(screen,(0,0,0),block_rect)
            screen.blit(self.cat,block_rect)

    def move_brother(self):
        if self.new_block1 == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body=body_copy[:]
            self.new_block1 = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body=body_copy[:]

    def add_block(self):
        self.new_block1 = True

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.brother = BROTHER()

    def update(self):
        self.snake.move_snake()
        self.eating()
        self.fail()
        self.brother.move_brother()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.brother.draw_brother()
        self.draw_score()

    def eating(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
            self.brother.add_block()
        if self.fruit.pos == self.brother.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
            self.brother.add_block()

    def fail(self):
        if not 0<= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0<= self.snake.body[0].y < cell_number:
            self.game_over()
        if self.snake.body[0].x == cell_number/2+1:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
             self.game_over()
        for block in self.brother.body[0:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_rect = score_surface.get_rect(center=(25,25))
        screen.blit(score_surface,score_rect)


pygame.init()
cell_size = 30
cell_number = 20
screen =pygame.display.set_mode((20 * 30 ,20 * 30))
clock = pygame.time.Clock()
fish = pygame.image.load('C:\web\python idk\CATS GAME/6.png').convert_alpha()
game_font = pygame.font.Font(None,25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
           main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                if main_game.snake.direction.y!=1:
                 main_game.snake.direction = Vector2(0, -1)
                 main_game.brother.direction =Vector2(0, 1)
            if event.key ==pygame.K_DOWN:
                if main_game.snake.direction.y!=-1:
                 main_game.snake.direction = Vector2(0, 1)
                 main_game.brother.direction =Vector2(0, -1)
            if event.key ==pygame.K_RIGHT:
                if main_game.snake.direction.x!=-1:
                 main_game.snake.direction = Vector2(1, 0)
                 main_game.brother.direction =Vector2(-1, 0)
            if event.key ==pygame.K_LEFT:
                if main_game.snake.direction.x!=1:
                 main_game.snake.direction = Vector2(-1, 0)
                 main_game.brother.direction =Vector2(1, 0)

    screen.fill((40,152,190))
    main_game.draw_elements()
    pygame.draw.rect(screen,(0,0,0),(10*cell_size,0,5,2000))
    pygame.display.update()
    clock.tick(60)