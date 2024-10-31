import pygame

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Skull")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

while(True):

    screen.fill((50, 50, 50))  # Background color

    # Draw skull head (upper part)
    pygame.draw.circle(screen, white, (100, 280), 70)  # Upper skull circle
    
    # Draw skull jaw (lower part)
    pygame.draw.ellipse(screen, white, (300, 300, 100, 150))  # Lower jaw oval

    # Draw eyes (large black circles)
    pygame.draw.circle(screen, black, (170, 160), 25)

    pygame.draw.circle(screen, white, (200, 150), 25)

  

    # Draw nose (upside-down triangle)
    pygame.draw.polygon(screen, black, [(100,20), (390,80), (210, 210)])

    #teeth!
    for i in range(20):
        for j in range(14):
            pygame.draw.rect(screen, black, (20+j*10, 240+i*10, 5, 8))

    
    # Update display
    pygame.display.flip()


pygame.quit()


