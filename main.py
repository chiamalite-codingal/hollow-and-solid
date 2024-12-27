import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill(((238,130,238)))
#colors
YELLOW = (225,165,0)
PURPLE = (106,90,205)
pygame.draw.circle(screen, YELLOW, (300,300), 50)
pygame.draw.circle(screen, PURPLE, (200,200), 70, 20)
pygame.display.update()
done = True
while done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  done = False
pygame.quit()