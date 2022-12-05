import java.io.File

fun getRockPaperScissorWinner(move1: Char, move2: Char) : Int {

    var move1Value = (move1.toInt()) - ('A'.toInt()) + 1;
    var move2Value = (move2.toInt()) - ('X'.toInt()) + 1;

    val losePoints = 0;
    val drawPoints = 3;
    val winPoints = 6;

    val rock = 1;
    val paper = 2;
    val scissor = 3;

    if (move1Value == move2Value) return move2Value + drawPoints;
    
    if (move1Value == rock)
    {
        if (move2Value == paper) return move2Value + winPoints;
        // scissor
        return move2Value + losePoints;
    }

    if (move1Value == paper)
    {
        if (move2Value == rock) return move2Value + losePoints;
        // scissor
        return move2Value + winPoints;
    }

    if (move1Value == scissor)
    {
        if (move2Value == rock) return move2Value + winPoints;
        // paper
        return move2Value + losePoints;
    }

    return 0
}
// Get the input file
val inputFilePath = if (args.contains("-i")) args[1 + args.indexOf("-i")] else "input.txt"

var lineCount = 0
var currentScore = 0;
var move1 = "A";
var move2 = "X";

File(inputFilePath).forEachLine { 

        var moves = it.split(" ")
        move1 = moves[0]
        move2 = moves[1]

        currentScore += getRockPaperScissorWinner(move1[0], move2[0]);
        // println(it) 
    lineCount++
}

println("The final score is " + currentScore)

