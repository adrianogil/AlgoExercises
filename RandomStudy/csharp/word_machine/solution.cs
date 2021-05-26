using System;
using System.Text;
using System.Collections.Generic;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {

    const int PROCESS_ERROR = -1;
    const int NO_ERROR = 0;
    const int MAX_STACK_SIZE = 1000;
    private int[] stack;
    private int currentStackPos;

    protected void initialize()
    {
        stack = new int[MAX_STACK_SIZE];
        currentStackPos = -1;
    }

    protected int addToStack(int number)
    {
        currentStackPos += 1;
        stack[currentStackPos] = number;

        return NO_ERROR;
    }

    protected void popElementFromStack()
    {
        currentStackPos -= 1;
    }

    protected void sumTopMostStackElements()
    {
        currentStackPos -= 1;
        stack[currentStackPos] += stack[currentStackPos+1];
    }

    protected void subtractTopMostStackElements()
    {
        currentStackPos -= 1;
        stack[currentStackPos] = stack[currentStackPos+1] - stack[currentStackPos];
    }

    protected int getTopMostValue()
    {
        return stack[currentStackPos];
    }

    public int solution(string S) {
        initialize();

        const int MAX_VALUE = 1048575;

        StringBuilder currentCommand = new StringBuilder("");

        for (int i = 0; i < S.Length; i++)
        {
            // Console.WriteLine(i + "/" + S.Length + ": " + S[i]);

            // Buffer command input while waiting for a space
            if (S[i] != ' ' || i == (S.Length - 1))
            {
                currentCommand.Append(S[i]);
            }

            // Try to parse current command buffer
            if (S[i] == ' ' || i == (S.Length - 1))
            {
                string command = currentCommand.ToString();
                currentCommand.Clear();

                int number = -1;

                // Console.WriteLine("Parsing command: " + command);

                if (Int32.TryParse(command, out number))
                {
                    // Current command is a number
                    // For the sake of simplicity, it's not verified if number is 20-bit unsigned integer
                    // Console.WriteLine(number);
                    addToStack(number);
                } else if (command == "POP") {
                    // Console.WriteLine("POP");
                    if (currentStackPos <= -1)  return PROCESS_ERROR;

                    popElementFromStack();
                } else if (command == "DUP") {
                    // Console.WriteLine("DUP");
                    if (currentStackPos <= -1)  return PROCESS_ERROR;

                    addToStack(getTopMostValue());
                } else if (command == "+") {
                    // Console.WriteLine("+");
                    if (currentStackPos <= 0)  return PROCESS_ERROR;

                    sumTopMostStackElements();

                    // Verify overflow in addition
                    if (getTopMostValue() > MAX_VALUE) return PROCESS_ERROR;
                }  else if (command == "-") {
                    // Console.WriteLine("-");
                    if (currentStackPos <= 0)  return PROCESS_ERROR;

                    subtractTopMostStackElements();

                    // Verify underflow in subtraction
                    if (getTopMostValue() < 0) return PROCESS_ERROR;
                }
                // Console.WriteLine("Testing array: " + String.Join(" ", new List<int>(stack).ConvertAll(j => j.ToString()).ToArray()));
            }
        }

        // Verify is stack is empty
        if (currentStackPos <= -1)  return PROCESS_ERROR;

        return getTopMostValue();
    }

    public void Test(String A, int expectedResult)
    {
        Console.WriteLine("\nTesting command: " + A);

        var dateOne = DateTime.Now;
        int result = this.solution(A);
        var dateTwo = DateTime.Now;

        var diff = dateTwo.Subtract(dateOne);
        var res = String.Format("{0} ms", diff.TotalMilliseconds);
        Console.WriteLine("Runtime: " + res);

        if (result == expectedResult)
        {
            Console.WriteLine("Result is right! Found " + result);
        } else {
            Console.WriteLine("Result is wrong! Found " + result + " but expected " + expectedResult);
        }
    }

    static void Main()          // Method declaration
    {
        Console.WriteLine ("Starting Testing ");    // Statement 2

        Solution m = new Solution();
        m.Test("13 DUP 4 POP 5 DUP + DUP + -", 7);
        m.Test("13 DUP 4 POP 5 DUP + DUP + - +", 20);
        m.Test("13 DUP 4 POP 5 DUP + DUP + - + DUP POP POP POP", -1);
        m.Test("5 6 + -", -1);
        m.Test("3 DUP 5 - -", -1);
    }
}
