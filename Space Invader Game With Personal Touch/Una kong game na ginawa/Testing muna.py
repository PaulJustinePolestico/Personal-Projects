import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 40)

# Button Colors
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
BLACK = (0, 0, 0)

# Button Class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 20, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Define Buttons
start_button = Button(300, 200, 200, 50, "Start Game")
settings_button = Button(300, 300, 200, 50, "Settings")
quit_button = Button(300, 400, 200, 50, "Quit")

# Menu Loop
menu_running = True
while menu_running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_clicked(event.pos):
                print("Start Game!")  # Replace with game launch logic
            if settings_button.is_clicked(event.pos):
                print("Settings!")  # Replace with settings logic
            if quit_button.is_clicked(event.pos):
                menu_running = False

    start_button.draw()
    settings_button.draw()
    quit_button.draw()

    pygame.display.update()

pygame.quit()