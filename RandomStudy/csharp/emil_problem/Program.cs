using System;
using System.Collections.Generic;

namespace ProblemB
{
    class Program
    {
        public static string winnerSentence;
        static void Main(string[] args)
        {
            for (int cases = 0; cases < 5; cases++)
            {
                winnerSentence = "";
                // string pairCountString = Console.ReadLine();
                // if (pairCountString == null)
                //     break;
                // int pairCount = Int32.Parse(pairCountString);
                // List<string> pairLeft = new List<string>();
                // List<string> pairRight = new List<string>();

                // for (int p = 0; p < pairCount; p++)
                // {
                //     string[] pairString = Console.ReadLine().Split(new char[] { ' ' }, StringSplitOptions.None);
                //     pairLeft.Add(pairString[0]);
                //     pairRight.Add(pairString[1]);
                // }

                // List<string> pairLeft = new List<string>() { "are", "you", "how", "alan", "dear" };
                // List<string> pairRight = new List<string>() { "yo", "u", "nhoware", "arala", "de" };
                //List<string> pairLeft = new List<string>() { "i", "ing", "resp", "ond", "oyc", "hello", "enj", "or" };
                //List<string> pairRight = new List<string>() { "ie", "ding", "orres", "pon", "y", "hi", "njo", "c" };
                //List<string> pairLeft = new List<string>() { "efgh", "d", "abc"};
                //List<string> pairRight = new List<string>() { "efgh", "cd", "ab"};
                //List<string> pairLeft = new List<string>() { "a", "b", "c"};
                //List<string> pairRight = new List<string>() { "ab", "bb", "cc"};
                List<string> pairLeft = new List<string>() { "de", "aralanho", "ware","you"};
                List<string> pairRight = new List<string>() { "dear", "ala","nh","owareyou"};

                for (int i = 0; i < pairLeft.Count; i++)//check for strong beginners
                {
                    if (pairLeft[i].StartsWith(pairRight[i]) || pairRight[i].StartsWith(pairLeft[i])) //if combination matches, then start the recursion
                    {
                        ResolvePairChain(new PairChain(GetNewList(pairLeft, i), GetNewList(pairRight, i), pairLeft[i], pairRight[i]));
                    }
                }
                string result = string.IsNullOrEmpty(winnerSentence) ? "IMPOSSIBLE" : winnerSentence;
                Console.WriteLine("Case {0}: {1}", (cases + 1), result);
            }
        }

        private static List<string> GetNewList(List<string> list, int indexToRemove)
        {
            List<string> newList = new List<string>(list);
            newList.RemoveAt(indexToRemove);
            return newList;
        }

        private static void ResolvePairChain(PairChain pairChain)
        {
            if (string.IsNullOrEmpty(pairChain.sentenceDifference))
            {
                if (pairChain.sentenceLeft == pairChain.sentenceRight)
                    StoreFinalSentence(pairChain.sentenceLeft);
            }
            else
            {
                for (int i = 0; i < pairChain.pairToCompare.Count; i++)
                {
                    if (pairChain.pairToCompare[i].StartsWith(pairChain.sentenceDifference)
                    || pairChain.sentenceDifference.StartsWith(pairChain.pairToCompare[i]))
                    {
                        ResolvePairChain(new PairChain(GetNewList(pairChain.pairLeft, i), GetNewList(pairChain.pairRight, i), pairChain.sentenceLeft + pairChain.pairLeft[i], pairChain.sentenceRight + pairChain.pairRight[i]));
                    }
                }
            }
        }

        private static void StoreFinalSentence(string sentence)
        {
            if (string.IsNullOrEmpty(winnerSentence) || sentence.Length < winnerSentence.Length) //first check sentence length
                winnerSentence = sentence;
            else if (sentence.Length == winnerSentence.Length)
            {
                char[] candidateChar = sentence.ToCharArray();
                char[] winnerChar = winnerSentence.ToCharArray();
                for (int i = 0; i < sentence.Length; i++)
                {
                    int charDif = winnerChar[i].CompareTo(candidateChar[i]); //its like a subtraction (winner - candidate)
                    if (charDif > 0) //check lexicographically
                    {
                        winnerSentence = sentence;
                        return;
                    }
                    else if (charDif < 0)
                        return;
                }
            }
        }

        class PairChain
        {
            public List<string> pairLeft;
            public List<string> pairRight;
            public List<string> pairToCompare;
            public string sentenceLeft;
            public string sentenceRight;
            public string sentenceDifference;
            public PairChain(List<string> pLeft, List<string> pRight, string sLeft, string sRight)
            {
                pairLeft = pLeft;
                pairRight = pRight;
                sentenceLeft = sLeft;
                sentenceRight = sRight;
                sentenceDifference = GetDifferenceFromSentences();
                pairToCompare = (IsLeftSentenceBigger() ? pairRight : pairLeft);
            }
            private string GetDifferenceFromSentences()
            {
                string minSentence = sentenceRight;
                string maxSentence = sentenceLeft;
                if (sentenceLeft.Length < sentenceRight.Length)
                {
                    minSentence = sentenceLeft;
                    maxSentence = sentenceRight;
                }
                return maxSentence.Substring(minSentence.Length);
            }
            private bool IsLeftSentenceBigger()
            {
                return sentenceLeft.Length > sentenceRight.Length;
            }
        }
    }
}