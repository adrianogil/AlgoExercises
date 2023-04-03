#include <stdio.h>
#include <stdlib.h>


void calculateNewMatrixState(int **matrix, int **matrixNewState, int sizeX, int sizeY)
{
    int liveNeighbors = 0;
    int cellValue = 0;
    int xk, yk, xn, yn;
    int neighborValue, lastCellValue;

    for (int y = 0; y < sizeY; y++)
    {
        for (int x = 0; x < sizeX; x++)
        {
            
            liveNeighbors = 0;
            cellValue = 0;
            lastCellValue = matrix[y][x];
            for (int k = 0; k < 9; k++)
            {
                xk = (k % 3) - 1;
                yk = (k / 3) - 1;

                xn = x + xk;
                yn = y + yk;

                if ((xk != 0 || yk != 0) && xn >= 0 && xn < sizeX && yn >= 0 && yn < sizeY) {
                    neighborValue = matrix[yn][xn];
                    if (neighborValue == 1)
                        liveNeighbors += 1;
                }
            }

            // Propagation rule
            // 
            // - White cells (DEAD_CELL) turn green (LIVE_CELL) if they have a number of green adjacent cells greater than 1 and less
            // than 5. Otherwise, they remain white (DEAD_CELL).
            // - Green cells (LIVE_CELL) remain green if they have a number of green adjacent cells greater than 3 and
            // less than 6. Otherwise, they become white (DEAD_CELL).

            if (lastCellValue == 0 && (liveNeighbors == 2 || liveNeighbors == 3 || liveNeighbors == 4))
            {
                cellValue = 1;
            }
            else if (lastCellValue == 1 && (liveNeighbors == 4 || liveNeighbors == 4)){

                cellValue = 1;
            }
            matrixNewState[y][x] = cellValue;
        }
    }
}


int main(int argc, char *argv[]) {
    FILE *fp;
    char ch;

    int sizeX = atoi(argv[2]);
    int sizeY = atoi(argv[3]);

    fp = fopen(argv[1], "r");

    int **matrix = (int **)malloc(sizeY * sizeof(int *));
    int **matrixNewState = (int **)malloc(sizeY * sizeof(int *));
    for (int i = 0; i < sizeY; i++) {
        matrix[i] = (int *)malloc(sizeX * sizeof(int));
        matrixNewState[i] = (int *)malloc(sizeX * sizeof(int));
    } 

    int index = 0;
    int x,y;
    while ((ch = fgetc(fp)) != EOF) {
        if (ch == '0' || ch == '1' || ch == '3' || ch == '4')
        {
            y = index / sizeX;
            x = index % sizeX;

            int cellValue = -1;
            if (ch == '0')
            {
                cellValue = 0;
            } else if (ch == '1')
            {
                cellValue = 1;
            } else if (ch == '3')
            {
                cellValue = 3;
            } else if (ch == '4')
            {
                cellValue = 4;
            }

            matrix[y][x] = cellValue;
            index++;
        }
    }
    fclose(fp);

    printf("%d", matrix[200][300]);
    printf("%d\n", matrix[1200][230]);

    calculateNewMatrixState(matrix, matrixNewState, sizeX, sizeY);

    printf("%d", matrixNewState[200][300]);
    printf("%d\n", matrixNewState[1200][230]);
    
    free(matrix);
    free(matrixNewState);

    return 0;
}