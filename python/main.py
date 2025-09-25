import pygame

WIDTH = 600
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cat_player = pygame.image.load("../gfx/cat_player.png")
cat_player_scaled = pygame.transform.scale(cat_player, (70, 70))

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    screen.fill("white")
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_pos.x > -3:
            player_pos.x -= 5
    if keys[pygame.K_RIGHT]:
        # cat_player_right = pygame.transform.flip(cat_player_scaled, True, False)
        if player_pos.x < WIDTH - 65:
            player_pos.x += 5
    
    screen.blit(cat_player_scaled, (player_pos.x, player_pos.y))
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()