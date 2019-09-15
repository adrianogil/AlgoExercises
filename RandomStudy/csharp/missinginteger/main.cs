using System;
using System.Collections.Generic;

class MissingInteger
{
    public int Find1(int[] A)
    {
        const int MAX_EXPECTED_ARRAY_SIZE = 100000;

        bool found = false;

        for (int i = 1; i <= MAX_EXPECTED_ARRAY_SIZE; i++)
        {
            found = false;

            for (int j = 0; j < A.Length; j++)
            {
                if (A[j] == i)
                {
                    found = true;
                    break;
                }
            }

            if (!found) return i;
        }

        return MAX_EXPECTED_ARRAY_SIZE + 1;
    }

    public int Find2(int[] A)
    {
        const int MAX_EXPECTED_ARRAY_SIZE = 100000;

        bool[] pos = new bool[MAX_EXPECTED_ARRAY_SIZE];

        int minInteger = 1;

        for (int j = 0; j < A.Length; j++)
        {
            if (A[j] > 0 && A[j] < MAX_EXPECTED_ARRAY_SIZE)
            {
                pos[A[j] - 1] = true;

                if (A[j] == minInteger)
                {
                    for (int i = minInteger; i < MAX_EXPECTED_ARRAY_SIZE; i++)
                    {
                        if (!pos[i]) {
                            minInteger = i+1;
                            break;
                        }
                    }
                }
            }
        }

        return minInteger;
    }

    public void Test(int[] A, int expectedResult)
    {
        Console.WriteLine("\nTesting array ");
        // Console.WriteLine("\nTesting array: " + String.Join(" ", new List<int>(A).ConvertAll(i => i.ToString()).ToArray()));

        var dateOne = DateTime.Now;
        int result = this.Find2(A);
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

        int[] a1 = new int[] {1, 2, 3};
        int[] a2 = new int[] {6, 3, 4, 5, 9, 1, 12, 45, 67, 7, 8};

        int[] a3 = new int[10000];
        for (int i = 0; i < a3.Length; i++)
        {
            a3[i] = i;
        }

        MissingInteger m = new MissingInteger();
        m.Test(a1, 4);
        m.Test(a2, 2);
        m.Test(a3, 10000);
    }
}