import java.io.File

// Get the input file
val inputFilePath = if (args.contains("-i")) args[1 + args.indexOf("-i")] else "input.txt"

var lineCount = 0
var currentElftCaloriesBeingCarried = 0;
var maxCalorieBeingCarried = mutableListOf(0, 0, 0)

File(inputFilePath).forEachLine { 

    if (it.isNullOrEmpty())
    {
        var foundMax = false;
        var tempValue1 = 0;
        var tempValue2 = 0;
        for (i in maxCalorieBeingCarried.indices)
        {
            if (foundMax)
            {
                tempValue2 = maxCalorieBeingCarried[i];
                maxCalorieBeingCarried[i] = tempValue1;
                tempValue1 = tempValue2;
            }
            else if (currentElftCaloriesBeingCarried > maxCalorieBeingCarried[i])
            {
                tempValue1 = maxCalorieBeingCarried[i];
                maxCalorieBeingCarried[i] = currentElftCaloriesBeingCarried;
                foundMax = true;
            }
        }
        // if (currentElftCaloriesBeingCarried > maxCalorieBeingCarried)
        // {
        //     maxCalorieBeingCarried = currentElftCaloriesBeingCarried;
        // }

        currentElftCaloriesBeingCarried = 0;
    }
    else {
        currentElftCaloriesBeingCarried += Integer.parseInt(it);
    }

        // println(it) 
    lineCount++
}

println("The maximum calories being carried by the top 3 Elves is " + (maxCalorieBeingCarried[0] + maxCalorieBeingCarried[1] + maxCalorieBeingCarried[2]))
println("The maximum calories being carried by the top 1 Elf is " + maxCalorieBeingCarried[0])
println("The maximum calories being carried by the top 2 Elf is " + maxCalorieBeingCarried[1])
println("The maximum calories being carried by the top 3 Elf is " + maxCalorieBeingCarried[2])

