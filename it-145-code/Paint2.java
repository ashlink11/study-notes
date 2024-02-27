/**
 * Ashley Grevelink
 * February 26, 2024
 * IT-145: Module 7 Assignment
 * 
 * Note: I used some of my code from Paint1 since it 
 * has input validation.
 */

/**
 * The Scanner import help to get user input from 
 * the command line.
 */
import java.util.Scanner;

/**
 * This class has one main() method, and no constructors
 * or other methods. Essentially, it is a static class.
 * 
 * It asks for input from a user and calculates how much
 * paint is needed for the area of a wall.
 */
public class Paint2 {

	/**
	 * The main method, which is the only method
	 * and all the variables are within the scope
	 * of this main() method.
	 */
    public static void main(String[] args) {
    	
    		/**
    		 * Variables for accepting input as Strings
    		 * and the doubles are for calculations.
    		 */
        Scanner scnr = new Scanner(System.in);
        double wallHeight = 0.0;
        String wallHeightStr = "";
        double wallWidth = 0.0;
        String wallWidthStr = "";
        double wallArea = 0.0;
        double gallonsPaintNeeded = 0.0;
        int cansPaintNeededInt = 0;
        
        /**
         * Variables for running and stopping the 
         * do-while input validation loops.
         */
        boolean validInput = false;
        boolean loopRunning = false;
        
        /**
         * I'm using StringBuilders here because Strings are 
         * immutable and I didn't want to create a new object
         * for every character of the input.
         */
        StringBuilder heightDoubleBuilder = new StringBuilder("");
        StringBuilder widthDoubleBuilder = new StringBuilder("");

        /**
         * This is a constant because the number of gallons of
         * paint needed per square foot does not change.
         */
        final double squareFeetPerGallons = 350.0;
        
        /**
         * For both of the user input do-while loops:
         * 
         * Only accepts positive integers, just like the test cases
         * show in the assignment. While I was debugging, I did run
         * into InputMismatchExceptions and NumberFormatExceptions,
         * but I decided not to use throws & try/catch because I 
         * can't replicate the crashes. I think they're all prevented.
         *  
         * The user can only input integers up to the integer memory
         * limit of the JVM.
         */
        
        // do-while loop to ensure the height is valid
        loopRunning = true;
        do {
            // prompting user to input wall's height
            validInput = true;
            System.out.println("Enter wall height (feet): ");
            wallHeightStr = scnr.nextLine();
            
            // loop through the input checking each character
            for (int i = 0; i < wallHeightStr.length(); i++) {
            	
            		// checks if the character is a digit
                if (Character.isDigit(wallHeightStr.charAt(i)) && 
                			!(wallHeightStr.charAt(i) == '0')) { 
            			heightDoubleBuilder.append(wallHeightStr.charAt(i));	
                }
                
                // if not, breaks the loop so we can get new input
                else {
            		System.out.println("Sorry, \"" + wallHeightStr + "\" is an " 
            				+ "invalid integer. Please try again.\n");
            		validInput = false;
            		break;
                }
            }
            
            // if we've checked the input and it's valid, end the loop
            if (validInput) {
            		// turn the string into a double
            		wallHeight = Double.parseDouble(heightDoubleBuilder.toString());
                loopRunning = false;
            }
   
        } while(loopRunning);

        System.out.println("");
        
        // do-while loop to ensure the width is valid   
        loopRunning = true;
        do {
            // prompting user to input wall's width
            validInput = true;
            System.out.println("Enter wall width (feet): ");
            wallWidthStr = scnr.nextLine();
            
            // loop through the input checking each character
            for (int i = 0; i < wallWidthStr.length(); i++) {
            	
            		// checks if the character is a digit
                if (Character.isDigit(wallWidthStr.charAt(i)) && 
            			!(wallWidthStr.charAt(i) == '0')) {
                		widthDoubleBuilder.append(wallWidthStr.charAt(i));	
                }
                
                // if not, breaks the loop so we can get new input
                else {
	            		System.out.println("Sorry, \"" + wallWidthStr + "\" is an " 
	            				+ "invalid integer. Please try again.\n");
	            		validInput = false;
	            		break;
                }
            }
            
            // if we've checked the input and it's valid, end the loop
            if (validInput) {
            		// turn the string into a double
                wallWidth = Double.parseDouble(widthDoubleBuilder.toString());
                loopRunning = false;
            }
        } while(loopRunning);
        
        System.out.println("");

        // close the scanner to prevents memory/resource leaks
        // as well as flushes the buffer
        scnr.close();

        // Calculate and output wall area
        wallArea = wallHeight * wallWidth;
        System.out.println("Wall area: " + wallArea + " square feet");

        // Calculate and output the amount of paint (in gallons) needed to paint the wall
        gallonsPaintNeeded = wallArea/squareFeetPerGallons;
        System.out.println("Paint needed: " + gallonsPaintNeeded + " gallons");
        
        // 1 can of paint = 1 gallon
        // Math.ceil() gives the ceiling, which is rounding up to the
        // next double, yet is equivalent to an integer, so we can cast
        // it safely to an integer.
        // Also, we do not need to import the Math library because it
        // is included in the Java standard library.
        cansPaintNeededInt = (int) Math.ceil(gallonsPaintNeeded);
        
        System.out.println("Cans needed: " + cansPaintNeededInt + " can(s)");
    }
}













































