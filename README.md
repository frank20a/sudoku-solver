# Sudoku Solver
As simple as the title suggests! Currently can solve ~up to **Hard** puzzles~ any puzzle from [sudoku.com](https://sudoku.com/)

## Watch it go
![Program solving a puzzle](https://i.ibb.co/N3B3gFV/Untitled-1.gif)

## Known Bugs
- ~Currently I have implemented *rule propagation* and *singleton value* methods. This can only solve so far. The algorithm CAN and WILL get stuck some times!~
- Solving **Expert** puzzles uses a Uniform Cost Search implementation to scrub impossible values. This method might find a better state or a complete solution but the program will not consider it. It will recalculate the solution to show it in the GUI
- The Arc Consequence method uses UCS and therefore is slow and calculates too deep. Implementing a localized search CAN solve every puzzle and WILL be faster!
- No loading different puzzles
