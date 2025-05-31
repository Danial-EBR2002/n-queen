import pygame
import sys
import os

# Import solver modules
from n_queen_backtracking import solve_n_queens
from n_queen_genetic import solve_n_queens_genetic

# Set path to current directory (for image loading)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except:
    pass

# Colors
WHITE = (255, 255, 255)
GRAY = (125, 135, 150)
DARK_GRAY = (100, 110, 120)

# Screen dimensions
WIDTH = 600
HEIGHT = 600

def draw_board(screen, n, queens, queen_img):
    cell_size = WIDTH // n
    for row in range(n):
        for col in range(n):
            color = GRAY if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))

    # Resize and draw queen image
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
    print("Select Algorithm to Solve N-Queens:")
    print("1. Backtracking")
    print("2. Genetic Algorithm")
    choice = input("Enter 1 or 2: ")

    try:
        n = int(input("Enter the value of n (e.g., 8): "))
    except:
        print("Invalid input for n.")
        sys.exit()

    if choice == "1":
        sol = solve_n_queens(n)
    elif choice == "2":
        sol = solve_n_queens_genetic(n)
    else:
        print("Invalid choice.")
        sys.exit()

    if sol:
        main(n, sol)
    else:
        print("No solution found.")
