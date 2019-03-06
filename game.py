import pygame, sys

pygame.init()

screen = pygame.display.set_mode((720, 480))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.width = 10
        self.height = 10
        self.rect = pygame.Rect((0,0),(self.width, self.height))
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.velocity = [0, 0]
        self.speed  = 2 
        self.dx = []
        self.dy = []
        self.screen_width = 720
        self.screen_height = 480

    def update(self):
        # update the X axis
        try:
            self.rect.x += self.dx[0]
            self.rect.x = self.wall_collision_x()    
        except IndexError:
            self.rect.x += 0
        
        # update the y axis
        try:
            self.rect.y += self.dy[0]
            self.rect.y = self.wall_collision_y()
        except IndexError:
            self.rect.y += 0

    def wall_collision_x(self):
        if self.rect.x < 1:
            return 1
        elif self.rect.x + self.width > self.screen_width + 1:
            return self.screen_width - 1 - self.width
        else:
            return self.rect.x
    def wall_collision_y(self):
        if self.rect.y < 1:
            return 1
        elif self.rect.y + self.height > self.screen_height + 1:
            return self.screen_height - 1 - self.height
        else:
            return self.rect.y

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.dx.insert(0, -player.speed)
            elif event.key == pygame.K_RIGHT:
                player.dx.insert(0, player.speed)
            elif event.key == pygame.K_UP:
                player.dy.insert(0, -player.speed)
            elif event.key == pygame.K_DOWN:
                player.dy.insert(0, player.speed)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.dx.remove(-player.speed)
            elif event.key == pygame.K_RIGHT:
                player.dx.remove(player.speed)
            elif event.key == pygame.K_UP:
                player.dy.remove(-player.speed)
            elif event.key == pygame.K_DOWN:
                player.dy.remove(player.speed)
    
    player.update()
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    pygame.display.update()
