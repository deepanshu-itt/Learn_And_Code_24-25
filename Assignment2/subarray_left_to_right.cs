using System;
using System.Linq;

class CalculateMeanFromSubarray {
    static void Main(string[] args) {
        var arraySizeandQueries = getUserArrayFromConsole();
        var userInputArray = getUserArrayLongFromConsole();

        long[] subarraySum = CalculateSubarraySums(userInputArray);

        processUserInputQueries(subarraySum, arraySizeandQueries[1]);
    }

    static int[] getUserArrayFromConsole() {
        return Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
    }

    static long[] getUserArrayLongFromConsole() {
        return Array.ConvertAll(Console.ReadLine().Split(' '), long.Parse);
    }


    static long[] CalculateSubarraySums(long[] userInputArray) {
        long[] subarraySum = new long[userInputArray.Length + 1];
        subarraySum[0] = 0;
        for (int index = 1; index <= userInputArray.Length; index++) {
            subarraySum[index] = subarraySum[index - 1] + userInputArray[index - 1];
        }
        return subarraySum;
    }

    static void processUserInputQueries(long[] subarraySum, int userInputQueryCount) {
        for (var query = 0; query < userInputQueryCount; query++) {
            var rightSubarraySum = getUserArrayFromConsole();
            var sum = subarraySum[rightSubarraySum[1]] - subarraySum[rightSubarraySum[0] - 1];
            var mean = (long)(sum / (rightSubarraySum[1] - rightSubarraySum[0]; + 1)); 
            Console.WriteLine(mean);
        }
    }
}
