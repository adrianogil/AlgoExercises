import java.io.File

// Get the input file
val inputFilePath = if (args.contains("-i")) args[1 + args.indexOf("-i")] else "input.txt"

var lineCount = 0
var currentElftCaloriesBeingCarried = 0;
var maxCalorieBeingCarried = 0;

File(inputFilePath).forEachLine { 

    if (it.isNullOrEmpty())
    {
        if (currentElftCaloriesBeingCarried > maxCalorieBeingCarried)
        {
            maxCalorieBeingCarried = currentElftCaloriesBeingCarried;
        }

        currentElftCaloriesBeingCarried = 0;
    }
    else {
        currentElftCaloriesBeingCarried += Integer.parseInt(it);
    }

        // println(it) 
    lineCount++
}

println("The maximum calories being carried by an Elf is " + maxCalorieBeingCarried)

