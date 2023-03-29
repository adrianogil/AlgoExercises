const stateSizeX = 8;
const stateSizeY = 7;

function domToArray() {
    const cells = document.getElementsByTagName('cell');
    const result = [];

    for (let i = 0; i < cells.length; i++) {
        const cell = cells[i];

        if (cell.classList.contains('dead')) {
            result.push(0);
        } else {
            result.push(1);
        }
    }

    return result;
}

const mazeStates = []
const deadPatterns = []

function updateStateFromGame(){
    const currentState = domToArray();
    console.log(currentState);
    mazeStates.push(currentState);
}

function checkPatterns(targetStateToCheck) {

    const targetState = mazeStates[targetStateToCheck];
    const nextState = mazeStates[targetStateToCheck+1];

    for (let i = 0; i < nextState.length; i++) {
        if (i != 0 && i != (nextState.length - 1) && nextState[i] == 0) {
            // Check neighbors
            
            var xs = i % 8;
            var ys = Math.floor(i / 8);

            var currentPattern = [];

            for (let k = 0; k <= 8; k++) {
                var xk = (k % 3) - 1;
                var yk = Math.floor(k / 3) - 1;

                var xn = xs + xk;
                var yn = ys + yk;

                if (xn >= 0 && xn < stateSizeX && yn >= 0 && yn < stateSizeY) {
                    var itarget = yn * 8 + xn;
                    currentPattern.push(targetState[itarget]);
                } else {
                    currentPattern.push(1);
                }
            }
            deadPatterns.push(currentPattern);
        }
    }
}

function printState(state) {
    let rows = stateSizeY;
    let cols = stateSizeX;

    for (let i = 0; i < rows; i++) {
      let row = '';
      for (let j = 0; j < cols; j++) {
        let index = i * cols + j;
        row += state[index] + ' ';
      }
      row += ' - ' + i;
      console.log(row);
    }
}

function tryToPredictNextMazeState(from) {
    const lastState = mazeStates[from];
    const possibleNextState = [];

    for (let i = 0; i < lastState.length; i++) {
        var nextCellState = 1;

        if (i != 0 && i != (lastState.length - 1) && lastState[i] == 0) {
            // Check neighbors
            
            var xs = i % 8;
            var ys = Math.floor(i / 8);            

            for (let p = 0; p < deadPatterns.length; p++) {
                var pattern = deadPatterns[p];
                if (nextCellState != 0) {
                    var foundError = 0;
                    for (let k = 0; k <= 8; k++) {
                        if (foundError == 0) {
                            var xk = (k % 3) - 1;
                            var yk = Math.floor(k / 3) - 1;

                            var xn = xs + xk;
                            var yn = ys + yk;

                            if (xk != 0 && yk != 0 && xn >= 0 && xn < stateSizeX && yn >= 0 && yn < stateSizeY) {
                                var itarget = yn * 8 + xn;
                                if (lastState[itarget] == pattern[k]) {
                                    nextCellState = 0;
                                } else {
                                    nextCellState = 1;
                                    foundError = 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        possibleNextState.push(nextCellState);
    }

    console.log(possibleNextState);

    printState(possibleNextState);
}

