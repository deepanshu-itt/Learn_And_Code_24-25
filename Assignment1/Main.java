import java.util.Scanner;

public class Main {
    static String[] countryCodes;
    static String[][] adjacentCountries;

    public static void main(String[] args) {
        initializeCountryInformation();
        String inputCountryCode = getUserCountryCodeInput();
        printAdjacentCountries(inputCountryCode);
    }
    
    private static void initializeCountryInformation() {
        countryCodes = new String[]{"IN", "US", "NZ"};
        adjacentCountries = new String[][]{
                {"Pakistan", "China", "Nepal", "Bangladesh"}, 
                {"Canada", "Mexico"},                        
                {"Australia"}                                
        };
    }

   
    private static String getUserCountryCodeInput() {
        Scanner userInput = new Scanner(System.in);
        System.out.println("Please Enter country code (IN/US/NZ) to find adjacent countries: ");
        String inputCountryCode = userInput.nextLine(); 
        userInput.close();
        return inputCountryCode;
    }

   
    private static void printAdjacentCountries(String countryCode) {
        int countryIndex = findCountryIndex(countryCode);
        if (countryIndex == -1) {
              System.out.println("Invalid country code entered. Please try again.");
        } else {
            System.out.println("Adjacent Countries are : ");
            for (String adjacentCountry : adjacentCountries[countryIndex]) {
                System.out.print( adjacentCountry + ", " );
            }
        }
    }


    private static int findCountryIndex(String countryCode) {
        int countryIndex=-1;
        for (int countryCodeIndex = 0; countryCodeIndex < countryCodes.length; countryCodeIndex++) {
            if (countryCodes[countryCodeIndex].equals(countryCode)) {
               countryIndex= countryCodeIndex; 
            }
        }
        return countryIndex; 
    }
}
