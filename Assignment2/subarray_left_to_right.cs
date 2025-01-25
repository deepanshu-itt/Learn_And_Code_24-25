using System;
using System.Numerics;
class CalculateMeanFromSubarray {
    static void Main(string[] args) {
       var arraySizeandQueries = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            var userInputarray = Array.ConvertAll(Console.ReadLine().Split(' '), long.Parse);
            long[] subarraySum = new long[arraySizeandQueries[0] + 1];
            subarraySum[0] = 0;
            for (int index = 1; index <= arraySizeandQueries[0]; index++)
            {
                subarraySum[index] = subarraySum[index - 1] + userInputarray[index - 1];
            }
            for (var query = 0; query < arraySizeandQueries[1]; query++)
            {
                var rightSubarraySum = Array.ConvertAll(Console.ReadLine().Split(' '), int.
                Console.WriteLine((long)((long)(subarraySum[rightSubarraySum[1]] - subarraySum[rightSubarraySum[0] - 1]) / (rightSubarraySum[1] - rightSubarraySum[0] + 1)));
            }
    }
}