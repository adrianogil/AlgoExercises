#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define DEBUG 0

typedef struct PathNodeStruct {
    int x, y;
    struct PathNodeStruct *lastNode;
} PathNode;

PathNode * push(int x, int y, PathNode *lastNode) {
    PathNode *newNode = (PathNode *) malloc(sizeof(PathNode));
    newNode->x = x;
    newNode->y = y;
    newNode->lastNode = lastNode;
    
    return newNode;
}

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

            if (lastCellValue != 0 && lastCellValue != 1) {
                matrixNewState[y][x] = lastCellValue;      
                continue;
            }

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

    printf("   - New matrix state calculated!\n");
}


PathNode * getNextPos(PathNode *currentPos, char nextDirection, int sizeX, int sizeY, int **matrixNewState, PathNode **nextPosToBeEval, int numberNextPosToBeEval)
{
    int nx, ny;

    switch (nextDirection) {
        case 'U':
            nx = currentPos->x + 0;
            ny = currentPos->y - 1;
            break;
        case 'D':
            nx = currentPos->x + 0;
            ny = currentPos->y + 1;
            break;
        case 'L':
            nx = currentPos->x - 1;
            ny = currentPos->y + 0;
            break;
        case 'R':
            nx = currentPos->x + 1;
            ny = currentPos->y + 0;
            break;
        default:
            return NULL;
    }

    if (nx < 0 || nx >= sizeX) return NULL;
    if (ny < 0 || ny >= sizeY) return NULL;
    if (matrixNewState[ny][nx] == 1) return NULL;

    // Remove repeated
    for (int p = 0; p < numberNextPosToBeEval; p++)
    {
        if (nx == nextPosToBeEval[p]->x && ny == nextPosToBeEval[p]->y)
        {
            return NULL;
        }
    }

    int maxRepeatedInPath = 5;
    int totalRepeatedInPath = 0;
    int pathDepthExplored = 0;
    PathNode *node = currentPos;
    while (node != NULL && pathDepthExplored < 2 * maxRepeatedInPath) {
        if (nx == node->x && ny == node->x) {
            totalRepeatedInPath++;
            if (totalRepeatedInPath > maxRepeatedInPath) return NULL;
        }
        node = node->lastNode;
        pathDepthExplored++;
    }

    return push(nx, ny, currentPos);
}


int main(int argc, char *argv[]) {
    FILE *fp;
    char ch;

    int sizeX = atoi(argv[2]);
    int sizeY = atoi(argv[3]);

    fp = fopen(argv[1], "r");


    int **matrixTemp;
    int **matrix = (int **)malloc(sizeY * sizeof(int *));
    int **matrixNewState = (int **)malloc(sizeY * sizeof(int *));
    for (int i = 0; i < sizeY; i++) {
        matrix[i] = (int *)malloc(sizeX * sizeof(int));
        matrixNewState[i] = (int *)malloc(sizeX * sizeof(int));
    } 

    PathNode* initialPos;
    PathNode* finalPos;

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
                initialPos = push(x, y, NULL);
            } else if (ch == '4')
            {
                cellValue = 4;
                finalPos = push(x, y, NULL);
            }

            matrix[y][x] = cellValue;
            index++;
        }
    }
    fclose(fp);

    printf("%d", matrix[200][300]);
    printf("%d\n", matrix[1200][230]);

    int maxPosToBeEval = 300000;
    PathNode **currentPosToBeEval = (PathNode**) malloc(maxPosToBeEval * sizeof(PathNode*));
    PathNode **nextPosToBeEval = (PathNode**) malloc(maxPosToBeEval * sizeof(PathNode*));
    PathNode **tempPosToBeEval;
    int numberPosToBeEval = 0;
    int numberNextPosToBeEval = 0;

    currentPosToBeEval[numberPosToBeEval] = initialPos;
    numberPosToBeEval++;

    char directions[4] = {'U', 'D', 'L', 'R'};
    char nextDirection;

    PathNode *currentPos;
    PathNode *nextPos;

    PathNode *bestPath;

    int maxT = 10000000;
    bool pathUsed = false;
    bool foundPath = false;

    float bestDist = 1000000.0f;
    float dist;

    for (int t = 0; t < maxT && !foundPath; t++)
    {
        printf("> t %d\n", t);
        printf("   - Evaluating %d positions\n", numberPosToBeEval);
        calculateNewMatrixState(matrix, matrixNewState, sizeX, sizeY);

        numberNextPosToBeEval = 0;
        bestDist = 1000000000000000.0f;

        for (int p = 0; p < numberPosToBeEval && !foundPath; p++)
        {
            currentPos = currentPosToBeEval[p];
            if (DEBUG)
            {
                printf("-- (%d, %d)\n", currentPos->x, currentPos->y);
            }
            pathUsed = false;
            for (int d = 0; d < 4 && !foundPath; d++)
            {
                nextDirection = directions[d];
                PathNode *nextPos = getNextPos(currentPos, nextDirection, sizeX, sizeY, matrixNewState, nextPosToBeEval, numberNextPosToBeEval);
                if (nextPos != NULL)
                {
                    dist = ((nextPos->x - finalPos->x) * (nextPos->x - finalPos->x)) + ((nextPos->y - finalPos->y) * (nextPos->y - finalPos->y));
                    if (dist < bestDist) {
                        bestDist = dist;
                    }

                    if (nextPos->x == finalPos->x && nextPos->y == finalPos->y)
                    {
                        bestPath = nextPos;
                        foundPath = true;
                        break;
                    }

                    nextPosToBeEval[numberNextPosToBeEval] = nextPos;
                    numberNextPosToBeEval++;
                    pathUsed = true;
                }
            }
            // Free unused path nodes
            if (!pathUsed) {
                free(currentPos);
            }
        }

        printf("   - Best dist: %.3f\n", bestDist);

        // Swap - position evaluation
        numberPosToBeEval = numberNextPosToBeEval;
        tempPosToBeEval = currentPosToBeEval;
        currentPosToBeEval = nextPosToBeEval;
        nextPosToBeEval = tempPosToBeEval;

        // Swap - matrix states
        matrixTemp = matrix;
        matrix = matrixNewState;
        matrixNewState = matrixTemp;
    }
    

    printf("%d", matrixNewState[200][300]);
    printf("%d\n", matrixNewState[1200][230]);
    
    free(matrix);
    free(matrixNewState);

    free(initialPos);
    free(finalPos);

    free(currentPosToBeEval);

    return 0;
}