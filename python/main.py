import pygame

WIDTH = 600
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cat_player = pygame.image.load("../gfx/cat_player.png")
cat_player_scaled = pygame.transform.scale(cat_player, (70, 70))

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")
    
    screen.blit(cat_player_scaled, (20, 20))
    pygame.display.flip()

pygame.quit()