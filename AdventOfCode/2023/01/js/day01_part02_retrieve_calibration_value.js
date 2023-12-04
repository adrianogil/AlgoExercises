const fs = require('fs');
const process = require('process');

const testFile = 
`two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`;

let lines;

if (process.argv.includes('--test')) {
    lines = testFile.split('\n');
} else {
    const targetFile = process.argv.length < 3 ? "../input.txt" : process.argv[2];
    try {
        const fileContent = fs.readFileSync(targetFile, 'utf8');
        lines = fileContent.split('\n');
    } catch (err) {
        console.error("Error reading the file:", err);
        return;
    }
}

let sumAllCalibrationValues = 0;

const validDigitsStr = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
];

function checkDigit(i, line) {
    for (let j = 0; j < validDigitsStr.length; j++) {
        const s = validDigitsStr[j];
        if (line.substring(i, i + s.length) === s) {
            return j + 1;
        }
    }
}

for (let line of lines) {
    let firstDigit = null;
    let lastDigit = null;

    for (let i = 0; i < line.length; i++) {
        const s = line[i];
        if (!isNaN(parseInt(s))) {
            if (firstDigit === null) {
                firstDigit = parseInt(s);
            }
            lastDigit = parseInt(s);
        } else {
            const value = checkDigit(i, line);
            if (value) {
                if (firstDigit === null) {
                    firstDigit = value;
                }
                lastDigit = value;
            }
        }
    }

    if (firstDigit !== null) {
        sumAllCalibrationValues += firstDigit * 10 + lastDigit;
    }
}

console.log("Sum of all calibration values is", sumAllCalibrationValues);
