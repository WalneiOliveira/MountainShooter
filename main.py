import pygame

# starting Pygame
pygame.init()

# setting window size
print('setup start')
screen = pygame.display.set_mode(size=(600, 480))
# setting screen background color (RGB: white blue)
screen.fill((135, 206, 235))
pygame.display.flip()
pygame.display.set_caption("Montain Shooter Game")
print('setup end')

print('loop start')
# main loop
running = True
while running:
    # checking all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# ending Pygame
print('quiting...')
pygame.quit()
