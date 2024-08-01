# Island Perimeter

This project contains a Python function that calculates the perimeter of an island described in a grid.

## Function: island_perimeter

The `island_perimeter` function takes a grid as input and returns the perimeter of the island described in the grid.

### Parameters:
- `grid`: A list of list of integers where:
  - 0 represents water
  - 1 represents land

### Rules:
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

### Usage:

```python
from island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12