using System;
using System.Numerics;

class MeanFromSubarray {
    static void Main(string[] args) {
        try{
            calculateMeanFromSubarray();
        }

        catch (Exception error)
        {
            Console.WriteLine($"Error occurred: {error.Message}");
        }
    }

    static void calculateMeanFromSubarray(){
        var arraySizeandQueries = getUserArrayFromConsole();
        var userInputArray = getUserArrayLongFromConsole();

        long[] subarraySum = calculateSubarraySums(userInputArray);

        processUserInputQueries(subarraySum, arraySizeandQueries[1]);
    }

    static int[] getUserArrayFromConsole() {
        return Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
    }

    static long[] getUserArrayLongFromConsole() {
        return Array.ConvertAll(Console.ReadLine().Split(' '), long.Parse);
    }


    static long[] calculateSubarraySums(long[] userInputArray) {
        long[] subarraySum = new long[userInputArray.Length + 1];
        subarraySum[0] = 0;
        for (int index = 1; index <= userInputArray.Length; index++) {
            subarraySum[index] = subarraySum[index - 1] + userInputArray[index - 1];
        }
        return subarraySum;
    }

    static void processUserInputQueries(long[] subarraySum, int userInputQueryCount) {
        for (var query = 0; query < userInputQueryCount; query++){
            var rightSubarraySum = getUserArrayFromConsole();
                handleValidateQuery(rightSubarraySum,subarraySum.Length);
                var mean = calculateMean(subarraySum,rightSubarraySum);
                Console.WriteLine(mean);
        }
    }

    static void handleValidateQuery(long[] rightSubarraySum, long subarraySumLength){
        if (rightSubarraySum[0] < 1 || rightSubarraySum[1] > subarraySumLength - 1 || rightSubarraySum[0] > rightSubarraySum[1])
                {
                    throw new ArgumentException("User Input Query Range is Invalid. Ensure the first index is less than or equal to the second index.");
                }

    }

    static long calculateMean(long[] subarraySum,long[] rightSubarraySum){
        return (long)((long)(subarraySum[rightSubarraySum[1]] - subarraySum[rightSubarraySum[0] - 1]) / (rightSubarraySum[1] - rightSubarraySum[0] + 1));
    }
}
