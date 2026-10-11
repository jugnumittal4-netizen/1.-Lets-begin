import pygame
pygame.init()
width, height = 800, 600
display=pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
bg_image=pygame.transform.scale(pygame.image.load("bgnew.jpg"), (width, height))
penguin = pygame.transform.scale(pygame.image.load("penguin.png"), (200, 200))
pernguin_rect = penguin.get_rect(center=(width//2, height//2))
text = pygame.font.Font(None, 36).render("Hello, Pygame!", True, (0, 0, 0))
text_rect = text.get_rect(center=(width//2, 50))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        display.blit(bg_image, (0, 0))
        display.blit(penguin, pernguin_rect)
        display.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()
