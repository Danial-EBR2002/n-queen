# N-Queens Visualizer

This project is an interactive visualizer for the classic N-Queens problem, letting the user choose between two solving algorithms:

- Backtracking – fast, exact, guaranteed solution.
- Genetic Algorithm – evolutionary, heuristic, and faster for larger boards.

The final solution is shown on a graphical chessboard using Pygame.

---

## Features

- Interactive algorithm selection at startup.
- Elegant and dynamic Pygame-based GUI.
- Adjustable board size (default: 8×8).
- Image-based queen rendering (LightQueen.webp required).

---

## Algorithm Options

### 1. Backtracking

A depth-first recursive approach that exhaustively explores all valid placements until a solution is found.

### 2. Genetic Algorithm

A population-based heuristic method that evolves placements across generations using selection, crossover, and adaptive mutation.

---

## Screenshot

Make sure to have a file named LightQueen.webp (a queen chess piece image) in the same folder.

You can optionally add a screenshot.png to preview the UI here.

---

## How to Run

### Requirements

```bash
pip install pygame
```

### Run the GUI

```bash
python n-queens_gui.py
```

Then select:
```
1 → Backtracking
2 → Genetic Algorithm
```

---

## Project Structure

```
n-queens/
├── n-queen_backtracking.py       # Backtracking solver
├── n-queen_genetic.py            # Genetic Algorithm solver
├── n-queens_gui.py               # GUI + logic integration
├── LightQueen.webp               # Image of the queen (required)
└── README.md                     # You are here
```

---

## Language Style

This project uses a neutral, clean English style aimed at clarity, similar to translated academic technical reports.

---

## License

MIT License – free to use and modify.