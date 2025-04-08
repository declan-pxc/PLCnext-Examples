# General Tutorial coding with PLCnext
This tutorial is going to go through 
- how code can be structured utilitising FBs and other methods to 'clean up' the code.
- Improvements of the HMI and development of symbols.
- How HMI and Structures can be interlinked

> You will need [PLCnext Base library](https://www.plcnextstore.com/world/app/391) v1.6.4

# Initial code
In [this commit](https://github.com/declan-pxc/PLCnext-Examples/commit/d3cdd63a0ec3cf2b27403793162e856901082170) the inital code that we will be working on can be found.

Currently the code for Arcade2 has two games in the project: Minesweeper (MSW) and Sudoku (SUD). If you look at NewProgram, you will see that both games are in the same program. The HMI has both games on different screens.

# MSW
Currently there is a flag indicated by `F` and bomb `B`. We will look at creating symbols to improve the look of this.
## HMI

### Flag
A new symbol was created and I used a Polycurve path to create the flag shape. It required 4 points in a rectangle and each point selected to be a corner. 
Then the colour background can be changed and sized accordingly

![image](https://github.com/user-attachments/assets/57f7e618-edbb-468b-80f8-04a4d9484868)

### Bomb
Similarly, a symbol was created for the bomb. Using a circle with gradient to make it appear more 3D and multiple Polylines to make the 'spikes'

![image](https://github.com/user-attachments/assets/ffa6be51-d2f7-4184-a5d9-1d9de980dc6d)


### Cell
The flag and bomb symbols `MSW_FLAG_ICO` and `MSW_BOMB_ICO` where given their respective symbols with the rectangle and dynamics `MSW_CELL_FLAG` and `MSW_CELL_BOMB`

## MSW Diffilculties
For the traditional game, there are three levels
| Difficulty | Rows | Columns | Mines |
|------------|------|---------|-------|
| Easy       | 9    | 9       | 10    |
| Medium     | 16   | 16      | 40    |
| Hard       | 16   | 30      | 99    |

To create the additional levels, the current code, it is dynamic with the its initialisation. A difficulty variable was added to dynamically change the max row, column and number of mines.

On the HMI, a Text List is used to select the different difficulties similar to SUD, but the values have been modified. It is connected to a HMI tag `iDifficulty`.
![image](https://github.com/user-attachments/assets/bee07e95-af2f-4d13-8a84-37786a5ecf8d)

| Text | Start Val  | End Val | Write Val |
|------------|------|--------|------|
| Easy       | 1    | 1      | 1    |
| Medium     | 2    | 2      | 2    |
| Hard       | 3    | 3      | 3    |

## MSW Initialisation
```
CASE iDifficulty OF
    1 : (* Easy *)
        rowMax := 9;
        colMax := 9;
        bomNum := 10;
    2 : (* Medium *)
        rowMax := 16;
        colMax := 16;
        bomNum := 40;
    3 : (* Hard *)
        rowMax := 16;
        colMax := 30;
        bomNum := 99;
    ELSE 
        (* Statements *)
END_CASE
```

This allows for the initialisation of mines to be dynamic 
```
PBCL_SysRandom_11(); // Uses the PLCnextBase library to generate sudo-random numbers
PBCL_SysRandom_12();
randrow := TO_INT(PBCL_SysRandom_11.lrRandom * (rowMax - 1) + 1);
randcol := TO_INT(PBCL_SysRandom_12.lrRandom * (colMax - 1) + 1);
IF NOT udtMSW[randrow][randcol].xBomb THEN
    udtMSW[randrow][randcol].xBomb := TRUE;    
    countB := countB + 1;
END_IF
IF countB = bomNum THEN
    State := 2;
END_IF
```
Based on the mines, we loop through and count the number of mines connected to each square (that is not a mine).
```
FOR i := 1 TO rowMax DO
    FOR j := 1 TO colMax DO
        
        // Init the location of the cells
        udtMSW[i][j].iRow := i;
        udtMSW[i][j].iCol := j;
        
        // Find the bomb cells and increase the good cells by one.
        rowMinOK := i - 1 > 0;
        rowMaxOK := i + 1 < rowMax + 1;
        colMinOK := j - 1 > 0;
        colMaxOK := j + 1 < colMax + 1;
        
        IF udtMSW[i][j].xBomb THEN
            IF rowMinOK AND colMinOK THEN
                IF NOT udtMSW[i-1][j-1].xBomb THEN
                    udtMSW[i-1][j-1].iBomb := udtMSW[i-1][j-1].iBomb + 1;
                END_IF
            END_IF
            IF rowMinOK THEN
                IF NOT udtMSW[i-1][j].xBomb THEN
                    udtMSW[i-1][j].iBomb := udtMSW[i-1][j].iBomb + 1;
                END_IF
            END_IF
            IF rowMinOK AND colMaxOK THEN   
                IF NOT udtMSW[i-1][j+1].xBomb THEN
                    udtMSW[i-1][j+1].iBomb := udtMSW[i-1][j+1].iBomb + 1;
                END_IF
            END_IF
            IF colMinOK THEN
                IF NOT udtMSW[i][j-1].xBomb THEN
                    udtMSW[i][j-1].iBomb := udtMSW[i][j-1].iBomb + 1;
                END_IF
            END_IF
            IF colMaxOK THEN
                IF NOT udtMSW[i][j+1].xBomb THEN
                    udtMSW[i][j+1].iBomb := udtMSW[i][j+1].iBomb + 1;
                END_IF
            END_IF
            IF rowMaxOK AND colMinOK THEN
                IF NOT udtMSW[i+1][j-1].xBomb THEN
                    udtMSW[i+1][j-1].iBomb := udtMSW[i+1][j-1].iBomb + 1;
                END_IF
            END_IF
            IF rowMaxOK THEN
                IF NOT udtMSW[i+1][j].xBomb THEN
                    udtMSW[i+1][j].iBomb := udtMSW[i+1][j].iBomb + 1;
                END_IF
            END_IF
            IF rowMaxOK AND colMaxOK THEN
                IF NOT udtMSW[i+1][j+1].xBomb THEN
                    udtMSW[i+1][j+1].iBomb := udtMSW[i+1][j+1].iBomb + 1;
                END_IF
            END_IF
        END_IF
        
    END_FOR
END_FOR
```
Each cell is then given the string to display on the cell. This is so that cells with 0, will show a blank square.
