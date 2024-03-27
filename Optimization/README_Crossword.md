# Crossword Puzzle Generator

This project aims to create a program for generating crossword puzzles. The program takes a predefined structure of the puzzle grid and a list of words as input, and it fills the grid with words in such a way that they intersect correctly, resulting in a fully functional crossword puzzle. The implementation includes constraint satisfaction problem (CSP) techniques to ensure that the generated puzzle adheres to the specified constraints and is solvable.

## Features

- **Crossword Puzzle Generation**: Generates crossword puzzles based on the provided structure and word list.
- **Constraint Satisfaction Problem (CSP)**: Utilizes CSP techniques to ensure that the generated puzzle meets the specified constraints.
- **Python Implementation**: Implemented in Python, making it accessible and easy to understand.
- **Backtracking Algorithm**: Employs a backtracking algorithm to efficiently search for solutions.
- **Command-line Interface**: Provides a command-line interface for running the crossword puzzle generator.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

```bash
git clone https://github.com/AlxBlzrv/CS50-AI.git
```

2. Navigate to the project directory:

```bash
cd Optimization
```

3. Run the main script to generate a crossword puzzle:

```bash
python generate.py structure.txt words.txt
```

Replace `structure.txt` with the file containing the crossword structure and `words.txt` with the file containing the list of words.

## Contributions

Contributions to this project are welcomed! If you have ideas for improvements or enhancements, feel free to open an issue or submit a pull request.

## License

This project is an educational endeavor and is not licensed. Feel free to clone, modify, and share it for educational purposes.

---
