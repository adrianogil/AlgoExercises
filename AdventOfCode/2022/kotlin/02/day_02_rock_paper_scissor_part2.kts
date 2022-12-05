import java.io.File

fun getRockPaperScissorWinner(move1: Char, move2: Char) : Int {

    var move1Value = (move1.toInt()) - ('A'.toInt()) + 1;
    var move2Value = (move2.toInt()) - ('X'.toInt()) + 1;

    val losePoints = 0;
    val drawPoints = 3;
    val winPoints = 6;

    val shouldlose = 1;
    val shouldDraw = 2;
    val shouldWin = 3;

    val rock = 1;
    val paper = 2;
    val scissor = 3;

    // Draw
    if (move2Value == shouldDraw) return move1Value + drawPoints;
    
    if (move1Value == rock)
    {
        if (move2Value == shouldWin) return paper + winPoints;
        // scissor - lose
        return scissor + losePoints;
    }

    if (move1Value == paper)
    {
        if (move2Value == shouldWin) return scissor + winPoints;
        // rock - lose
        return rock + losePoints;
    }

    if (move1Value == scissor)
    {
        if (move2Value == shouldWin) return rock + winPoints;
        // paper - lose
        return paper + losePoints;
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

