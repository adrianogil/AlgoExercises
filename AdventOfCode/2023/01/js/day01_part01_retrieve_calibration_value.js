const fs = require('fs');
const process = require('process');

// Set the target file; use "../input.txt" by default or take from command line argument
let targetFile = process.argv.length < 3 ? "../input.txt" : process.argv[2];

function readFile(callback) {
    fs.readFile(targetFile, 'utf8', callback);
}

function processFile(err, data) {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    let lines = data.split('\n');
    let sumAllCalibrationValues = 0;

    for (let line of lines) {
        // Find the first and last digit in the line
        let firstDigit = null;
        let lastDigit = null;
        for (let s of line) {
            if (!isNaN(parseInt(s))) {
                lastDigit = parseInt(s);
                if (firstDigit === null) {
                    firstDigit = lastDigit;
                }
            }
        }

        if (firstDigit !== null) {
            sumAllCalibrationValues += firstDigit * 10 + lastDigit;
        }
    }

    console.log("Sum of all calibration values is", sumAllCalibrationValues);
}

readFile(processFile);
