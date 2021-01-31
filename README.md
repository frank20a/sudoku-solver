# Sudoku Solver
As simple as the title suggests! Currently can solve ~up to **Hard** puzzles~ any puzzle from [sudoku.com](https://sudoku.com/)

## Watch it go
![Program solving a puzzle](https://i.ibb.co/N3B3gFV/Untitled-1.gif)

## Usage
Upon startup the program opens an Open File dialog to choose a game file. Game files contain a sudoku puzzle. Every one of the nine rows contains nine numbers from 0 to 9. 0 means that the cell is empty and 1-9 are the provided solved cells. There are example puzzles in the `games` folder. When you open the file, the program loads it and you can use it from the **"Solve"** and **"Step"** buttons. **"Step"** makes a single move twards solution and **"Solve"** recursively steps until solution.

    Example input file:
      0 0 0 0 0 0 0 0 1
      9 0 5 3 0 0 6 0 0
      0 0 3 1 0 0 0 4 0
      0 0 2 0 8 0 0 0 0
      0 0 0 0 0 0 1 0 6
      7 0 0 0 0 0 5 8 0
      0 0 0 0 0 3 0 0 0
      8 7 0 0 2 6 0 0 4
      0 4 0 0 0 0 7 0 0
 
## Known Bugs
- ~Currently I have implemented *rule propagation* and *singleton value* methods. This can only solve so far. The algorithm CAN and WILL get stuck some times!~
- Solving **Expert** puzzles uses a Uniform Cost Search implementation to scrub impossible values. This method might find a better state or a complete solution but the program will not consider it. It will recalculate the solution to show it in the GUI
- The Arc Consequence method uses UCS and therefore is slow and calculates too deep. Implementing a localized search CAN solve every puzzle and WILL be faster!
- No loading different puzzles
- Console doesn't show "Solved" when finished
