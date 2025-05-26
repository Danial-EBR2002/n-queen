
import pygame
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except:
    pass
WHITE = (255, 255, 255)
GRAY = (125, 135, 150)
DARK_GRAY = (100, 110, 120)

WIDTH = 600
HEIGHT = 600

def draw_board(screen, n, queens, queen_img):
    cell_size = WIDTH // n
    for row in range(n):
        for col in range(n):
            color = GRAY if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))

    # Draw queens using image
    queen_scaled = pygame.transform.smoothscale(queen_img, (cell_size, cell_size))
    for row in range(n):
        col = queens[row]
        x = col * cell_size
        y = row * cell_size
        screen.blit(queen_scaled, (x, y))

def main(n, queens):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"{n}-Queens Visualization")

    try:
        queen_img = pygame.image.load("LightQueen.webp").convert_alpha()
    except Exception as e:
        print("Error loading queen image:", e)
        pygame.quit()
        sys.exit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(DARK_GRAY)
        draw_board(screen, n, queens, queen_img)
        pygame.display.flip()
        


if __name__ == "__main__":

    sample_solution = [0,0,0,0,0,0,0,0]
    main(8, sample_solution)
