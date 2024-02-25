/**
 * Developer: Ashley Grevelink
 * Date: Feb 25, 2024
 * Course: SNHU IT-145
 */

 import java.util.ArrayList;
 import java.util.Scanner;
 
 /**
  * The driving class for the Grazioso Salvare project. Contains static
  * attributes, static methods, and no constructors.
  */
 public class Driver {
   // ArrayLists to hold the custom data types of Dog and Monkey
   private static ArrayList<Dog> dogList = new ArrayList<Dog>();
   private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();
 
   // static boolean to prevent menu loop from running if a sub-loop is running
   private static boolean runSubLoop;
 
   // the entry-point for the program
   public static void main(String[] args) {
 
     // create new objects to initialize the list member variables
     initializeDogList();
     initializeMonkeyList();
 
     // high-level on/off switch for the main menu loop; starts on
     boolean runMenuLoop = true;
     // start the program with no sub-loops running
     runSubLoop = false;
     
     // set up ways to get user input
     Scanner scnr = new Scanner(System.in);
     String currentInput;
 
     // main driving while loop of the program
     // if a sub-loop is running, the menu loop is temporarily disabled
     //
     // each selection in the if/else chain leads to a different method call
     // or quitting the program, or an error message and rerunning the loop
     while (runMenuLoop && !runSubLoop) {
       displayMenu(); // main bulk of repeated print statements
       currentInput = scnr.nextLine();
       if (currentInput.equals("1")) {
         System.out.println("\nYou have selected: [1] Intake a new dog.");
         System.out.println("Intaking...");
         runSubLoop = true;
         intakeNewDog(scnr);
 
       } else if (currentInput.equals("2")) {
         System.out.println("\nYou have selected: [2] Intake a new monkey.");
         System.out.println("Intaking...");
         runSubLoop = true;
         intakeNewMonkey(scnr);
 
       } else if (currentInput.equals("3")) {
         System.out.println("\nYou have selected: [3] Reserve an animal.");
         System.out.println("Reserving...");
         runSubLoop = true;
         reserveAnimal(scnr);
 
       } else if (currentInput.equals("4")) {
         System.out.println("\nYou have selected: [4] Print a list of all dogs.");
         System.out.println("Printing...\n");
         printAnimals("dog");
 
       } else if (currentInput.equals("5")) {
         System.out.println("\nYou have selected: [5] Print a list of all monkeys.");
         System.out.println("Printing...\n");
         printAnimals("monkey");
 
       } else if (currentInput.equals("6")) {
         System.out.println("\nYou have selected: [6] Print a list of all animals "
             + "that are not reserved.");
         System.out.println("Printing...\n");
         printAnimals("available");
 
       } else if (currentInput.equals("q")) {
         runMenuLoop = false;
         System.out.println("\nYou have selected: [q] Quit application.");
         System.out.println("Quitting...");
         break;
 
       } else {
         System.out.println("\nError. Please try again.");
       }
     }
 
   }
 
   // This method prints the menu options
   public static void displayMenu() {
     System.out.println("\n\n");
     System.out.println("\t\t\t\tRescue Animal System Menu");
     System.out.println("[1] Intake a new dog");
     System.out.println("[2] Intake a new monkey");
     System.out.println("[3] Reserve an animal");
     System.out.println("[4] Print a list of all dogs");
     System.out.println("[5] Print a list of all monkeys");
     System.out.println("[6] Print a list of all animals that are not reserved");
     System.out.println("[q] Quit application");
     System.out.println();
     System.out.println("Enter a menu selection");
   }
 
   // Adds dogs to a list for testing
   public static void initializeDogList() {
     Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", 
         "05-12-2019", "Germany", "fully trained",
         false, "France");
     Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", 
         "02-03-2020", "England", "Phase I", false,
         "Wales");
     Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", 
         "12-12-2019", "Peru", "in service", true,
         "Chile");
 
     dogList.add(dog1);
     dogList.add(dog2);
     dogList.add(dog3);
   }
 
   // Adds monkeys to a list for testing
   public static void initializeMonkeyList() {
     Monkey monkey1 = new Monkey("dax", "male", "1", "25.6", "05-12-2019", 
         "Madagascar", "fully trained", false,
         "South Africa", "capuchin", "20", "40", "70");
     Monkey monkey2 = new Monkey("beatrice", "female", "1", "25.6", "05-12-2019", 
         "Mexico", "fully trained", false,
         "Panama", "tamarin", "20", "40", "70");
     Monkey monkey3 = new Monkey("siddhartha", "male", "1", "25.6", "05-12-2019", 
         "Argentina", "intake", false,
         "Brazil", "squirrel monkey", "20", "40", "70");
 
     monkeyList.add(monkey1);
     monkeyList.add(monkey2);
     monkeyList.add(monkey3);
   }
 
   // Check if a dog is already in the system 
   // If yes, print a message and return to the main loop
   // If not, create a new Dog obeject via asking 
   // intake questions and then add it to the dogList
   public static void intakeNewDog(Scanner scanner) {
     
     // get a String ready for the scanner
     String userInput = "";
     
     // ask first question & read with the scanner
         System.out.println("What is the dog's name?");
     userInput = scanner.nextLine();
     for (Dog dog : dogList) {
       if (dog.getName().equalsIgnoreCase(userInput)) {
         // if dog is already in system, exit to main menu
         System.out.println("\n\nThis dog is already in our system.\n\n");
         runSubLoop = false;
         return;
       }
     }
     
     // start saving responses to intake the dog
     ArrayList<Object> responses = new ArrayList<Object>();
     responses.add(userInput);
     
     // send thank you message & prepare for 11 more Qs
     System.out.println("\nThank you. Let's add " + userInput + " to our system." + 
         "\nWe have 9 more questions.\n");
 
     // the other 9 intake questions other than name and species
     String[] intakeQuestions = { 
         "Breed?",
         "Gender?",
         "Age?", 
         "Weight?", 
         "Acquisition date?", 
         "Acquisition location?", 
         "Training status?", 
         "Is the dog currently in service? (true/false)",
         "If yes, what is their country of service? (or n/a)", 
         };
     
     // Add the code to instantiate a new dog and add it to the appropriate list
 
     // ask the other questions and save the responses
     int count = 0;
     userInput = ""; // reset user input to empty string
     while (count < 9) {
       System.out.print("Question" + (count + 1) + ": ");
       System.out.println(intakeQuestions[count]);
 
       userInput = scanner.nextLine();
       if (!userInput.equals("")) {
         System.out.println("Saved as: " + userInput + ".\n");
 
         responses.add(userInput);
         count++;
         userInput = "";
       }
     }
 
     // convert a String object to a boolean primitive for
     // the Dog constructor we're using
     boolean reserved = false;
     if (responses.get(8).toString().equalsIgnoreCase("true")) {
       reserved = true;
     } else if (responses.get(8).toString().equalsIgnoreCase("false")) {
       reserved = false;
     }
 
     // create the new Dog object
     // use the intake responses for the parameters
     Dog newDog = new Dog(
         responses.get(0).toString(), 
         responses.get(1).toString(), 
         responses.get(2).toString(), 
         responses.get(3).toString(), 
         responses.get(4).toString(),
         responses.get(5).toString(), 
         responses.get(6).toString(), 
         responses.get(7).toString(),
         reserved, 
         responses.get(9).toString());
 
     // print statements for debugging/testing
 //		System.out.println(newDog.getName());
 //		System.out.println(newDog.getBreed());
 //		System.out.println(newDog.getGender());
 //		System.out.println(newDog.getAge());
 //		System.out.println(newDog.getWeight());
 //		System.out.println(newDog.getAcquisitionDate());
 //		System.out.println(newDog.getAcquisitionLocation());
 //		System.out.println(newDog.getTrainingStatus());
 //		System.out.println(newDog.getReserved());
 //		System.out.println(newDog.getInServiceLocation());
 
 
     // add the new Dog object to the static Dog ArrayList
     dogList.add(newDog);
     System.out.println("Thank you. " + newDog.getName() + 
         "'s information is saved in our system.");
     
     runSubLoop = false;
   }
   
   // Check if a monkey is already in the system
   // If not, check for monkey species
   // If species is allowed, ask intake questions,
   // create a new Monkey object and add it to the
   // monkeyList
   public static void intakeNewMonkey(Scanner scanner) {
 
     // get a String ready for the scanner
     String userInput = "";
     
     // ask the first question
     System.out.println("What is the monkey's name?");
     boolean monkeyNameLoop = true;
     while (monkeyNameLoop) {
       userInput = scanner.nextLine();
       if (!(userInput.equals(""))) {
         // we got input
         monkeyNameLoop = false;
       }
     }
 
     // see if the monkey is already in the system
     for (Monkey monkey : monkeyList) {
       if (monkey.getName().equalsIgnoreCase(userInput)) {
         System.out.println(userInput + " is already in our system\n\n");
         runSubLoop = false;
         return; // returns to menu
       }
     }
 
     // start saving responses in case we can intake the monkey
     ArrayList<Object> responses = new ArrayList<Object>();
     responses.add(userInput);
     
     // ask the second question
     System.out.println("\nThanks.\nWhich species is " + userInput + "?\n");
     boolean monkeySpeciesLoop = true;
     while (monkeySpeciesLoop) {
       userInput = scanner.nextLine();
       if (!(userInput.equals(""))) {
         // we got input
         monkeySpeciesLoop = false;
       }
     }
     
     // determine if we can intake this monkey species
     boolean validMonkeyType = false;
     switch (userInput.toLowerCase()) {
         case "capuchin":
             validMonkeyType = true;
             break;
         case "guenon":
             validMonkeyType = true;
             break;
         case "macaque":
             validMonkeyType = true;
             break;
         case "marmoset":
             validMonkeyType = true;
             break;
         case "squirrel monkey":
             validMonkeyType = true;
             break;
         case "tamarin":
             validMonkeyType = true;
             break;
         default:
             break;
     }
     
     // if monkey type isn't valid, exit to main menu
     if (!validMonkeyType) {
       System.out.println("Sorry, we cannot intake " + userInput + 
           " at this time.");
       runSubLoop = false;
       return;
     }
     
     // if monkey type is valid, prepare for 11 more Qs
     System.out.println("\nThank you.\nWe can intake " + userInput + 
         ".\nLet's add " + responses.get(0) + " to our system." + 
         "\nWe have 11 more questions.\n");
     responses.add(userInput);
 
     // the other 11 intake questions other than name and species
     String[] intakeQuestions = { 
         "Gender?",
         "Age?", 
         "Weight?", 
         "Acquisition date?", 
         "Acquisition location?", 
         "Training status?", 
         "Is the monkey currently in service? (true/false)",
         "If yes, what is their country of service? (or n/a)", 
         "Tail length?",
         "Height?", 
         "Body Length?" };
 
     // ask the other questions and save the responses
     int count = 0;
     userInput = ""; // reset user input to empty string
     while (count < 11) {
       System.out.print("Question" + (count + 1) + ": ");
       System.out.println(intakeQuestions[count]);
 
       userInput = scanner.nextLine();
       if (!userInput.equals("")) {
         System.out.println("Saved as: " + userInput + ".\n");
 
         responses.add(userInput);
         count++;
         userInput = "";
       }
     }
 
     // convert a String object to a boolean primitive for
     // the Monkey constructor we're using
     boolean reserved = false;
     if (responses.get(8).toString().equalsIgnoreCase("true")) {
       reserved = true;
     } else if (responses.get(8).toString().equalsIgnoreCase("false")) {
       reserved = false;
     }
 
     // create the new Monkey object
     // the responses order does not match
     // the order of fields in the constructor
     // because we had to ask the species before
     // determining if we could intake the monkey
     Monkey newMonkey = new Monkey(
         responses.get(0).toString(), 
         responses.get(2).toString(), 
         responses.get(3).toString(), 
         responses.get(4).toString(),
         responses.get(5).toString(), 
         responses.get(6).toString(), 
         responses.get(7).toString(),
         reserved, 
         responses.get(9).toString(),
         responses.get(1).toString(), 
         responses.get(10).toString(), 
         responses.get(11).toString(),
         responses.get(12).toString());
 
     // print statements for debugging/testing
 //		System.out.println(newMonkey.getName());
 //		System.out.println(newMonkey.getGender());
 //		System.out.println(newMonkey.getAge());
 //		System.out.println(newMonkey.getWeight());
 //		System.out.println(newMonkey.getAcquisitionDate());
 //		System.out.println(newMonkey.getAcquisitionLocation());
 //		System.out.println(newMonkey.getTrainingStatus());
 //		System.out.println(newMonkey.getReserved());
 //		System.out.println(newMonkey.getInServiceLocation());
 //		System.out.println(newMonkey.getSpecies());
 //		System.out.println(newMonkey.getTailLength());
 //		System.out.println(newMonkey.getHeight());
 //		System.out.println(newMonkey.getBodyLength());
     
     // add the new Monkey object to the static Monkey ArrayList
     monkeyList.add(newMonkey);
     System.out.println("Thank you. " + newMonkey.getName() + 
         "'s information is saved in our system.");
 
     runSubLoop = false;
     return; // returns to menu
 
   }
 
   // This will find the animal by animal type and in service country
   public static void reserveAnimal(Scanner scanner) {
     
     // get Strings ready for scanner
     String animalType = "";
     String serviceCountry = "";
     
     // ask two questions to the customer
     System.out.println("Which type of animal are you looking for?");
     boolean typeLoop = true;
     while (typeLoop) {
       // get input from the user
       animalType = scanner.nextLine();
       if (!(animalType.equals(""))) {
         // we got input, so terminate this loop
         typeLoop = false;
       }
     }
     System.out.println("Which service country are you looking for?");
     boolean serviceLoop = true;
     while (serviceLoop) {
       // get input from the user
       serviceCountry = scanner.nextLine();
       if (!(serviceCountry.equals(""))) {
         // we got input, so terminate this loop
         serviceLoop = false;
       }
     }
     
     // logic to check for an available dog in a certain country.	
     // if the user did want a dog but there was none available,
     // prints a message to them and returns to main menu
     if (animalType.equalsIgnoreCase("dog")) {
       
       // initialize a Dog object to null just in case we find a match
       Dog availableDog = null;
       
       // loop through the list of all dogs
       for (Dog dog : dogList) {
         
         // check if the service location matches
         if (dog.getInServiceLocation().equalsIgnoreCase(serviceCountry)) {
           
           // check if the dog is available
           if (dog.getReserved() == false) {
             
             // store the Dog object from the dogList in the 
             // availableDog object
             availableDog = dog;
           }
         }
       }
       
       // if there was a dog found, enter this logic
       if (availableDog != null) {
         
         // print a success confirmation message
         System.out.println(availableDog.getName() + " is an available dog in " 
                 + serviceCountry + ". They are now reserved for you.");
         
         // set the reserved status of the dog to true.
         // since Dog is a reference type, availableDog points
         // to the correct object, so we can update it
         availableDog.setReserved(true);
         
       } 
       
       // if there was no dog found, enter this logic
       else {
         
         // print a message that we could not find a dog
         System.out.println("Sorry, we do not have any dogs available in " 
                 + serviceCountry + ". If you'd "
                 + "like to try a different animal/country combination,"
                 + "please try 'reserve animal' again from the main menu.");
         
         // return to the main menu
         runSubLoop = false;
         return;
       }
     }
     
     
     // logic to check for an available monkey in a certain country.	
     // if the user did want a monkey but there was none available,
     // prints a message to them and returns to main menu
     if (animalType.equalsIgnoreCase("monkey")) {
       
       // initialize a Monkey object to null just in case we find a match
       Monkey availableMonkey = null;
       
       // loop through the list of all monkeys
       for (Monkey monkey : monkeyList) {
         
         // check if the service location matches
         if (monkey.getInServiceLocation().equalsIgnoreCase(serviceCountry)) {
           
           // check if the monkey is available
           if (monkey.getReserved() == false) {
             
             // store the Monkey object from the dogList in the 
             // availableMonkey object
             availableMonkey = monkey;
           }
         }
       }
       
       // if there was a monkey found, enter this logic
       if (availableMonkey != null) {
         
         // print a success confirmation message
         System.out.println(availableMonkey.getName() + " is an available monkey in " 
                 + serviceCountry + ". They are now reserved for you.");
         
         // set the reserved status of the monkey to true.
         // since Monkey is a reference type, availableMonkey points
         // to the correct object, so we can update it
         availableMonkey.setReserved(true);
         
       } 
       
       // if there was no monkey found, enter this logic
       else {
         
         // print a message that we could not find a monkey
         System.out.println("Sorry, we do not have any monkeys available in " 
                 + serviceCountry + ". If you'd "
                 + "like to try a different animal/country combination,"
                 + "please try 'reserve animal' again from the main menu.");
         
         // return to the main menu
         runSubLoop = false;
         return;
       }
     }
     
     // in case they were not looking for a dog or monkey,
     // make sure to turn the subLoop off
     runSubLoop = false;
   }
 
   /**
    * Based on the argument, prints one of three different lists.
    * 
    * Argument:
    * 1. dog: all from dogList
    * 2. monkey: all from monkeyList
    * 3. available: all from either dogList and/or monkeyList
    * 		where animal.getTrainingStatus() == "fully trained"
    * 		and animal.getReserved() == false 
    * 		
    * For each animal, prints:
    * - name
    * - training status
    * - acquisition country
    * - if the animal is reserved (true/false)
    */
   public static void printAnimals(String listType) {
     
     // if the method argument is "dog"
     if (listType.equals("dog")) {
       
       // keep track of how many dogs in the list to print out
       int count = 0;
       
       // loop through the list of all dogs
       for (Dog dog : dogList) {
         
         count++;
 
         // print statements for the dog information
         System.out.println("Dog " + count + ": ");
         System.out.println("Name: " + dog.getName());
         System.out.println("Training status: " + dog.getTrainingStatus());
         System.out.println("Acquisition country: " + dog.getAcquisitionLocation());
         System.out.println("Is the dog reserved?: " + dog.getReserved());
         System.out.println();	
         System.out.println();		
       }
     } 
     
     // if the method argument is "monkey" 
     else if (listType.equals("monkey")) {
       
       // keep track of how many monkeys in the list to print out
       int count = 0;
       
       // loop through the list of all monkeys
       for (Monkey monkey : monkeyList) {
         
         count++;
 
         // print statements for the monkey information
         System.out.println("Monkey " + count + ": ");
         System.out.println("Name: " + monkey.getName());
         System.out.println("Training status: " + monkey.getTrainingStatus());
         System.out.println("Acquisition country: " + monkey.getAcquisitionLocation());
         System.out.println("Is the monkey reserved?: " + monkey.getReserved());
         System.out.println();	
         System.out.println();		
       }
     } 
     
     // if the method argument is "available" 
     else if (listType.equals("available")) {
       
       // count how many animals found
       int count = 0;
       
       // loop through the list of all dogs
       for (Dog dog : dogList) {
         
         // check if the training status matches
         if (dog.getTrainingStatus().equalsIgnoreCase("fully trained")) {
           
           // check if the dog is available
           if (dog.getReserved() == false) {
             
             count++;
             
             // print statements for the dog information
             System.out.println("Animal " + count + ": ");
             System.out.println("Type: dog");
             System.out.println("Name: " + dog.getName());
             System.out.println("Training status: " + dog.getTrainingStatus());
             System.out.println("Acquisition country: " + dog.getAcquisitionLocation());
             System.out.println("Is the dog reserved?: " + dog.getReserved());
             System.out.println();	
             System.out.println();	
           }
         }				
 
       }	
       
       // loop through the list of all monkeys
       for (Monkey monkey : monkeyList) {
         
         // check if the training status matches
         if (monkey.getTrainingStatus().equalsIgnoreCase("fully trained")) {
           
           // check if the monkey is available
           if (monkey.getReserved() == false) {
             
             count++;
             
             // print statements for the monkey information
             System.out.println("Animal " + count + ": ");
             System.out.println("Type: monkey");
             System.out.println("Name: " + monkey.getName());
             System.out.println("Training status: " + monkey.getTrainingStatus());
             System.out.println("Acquisition country: " + monkey.getAcquisitionLocation());
             System.out.println("Is the monkey reserved?: " + monkey.getReserved());
             System.out.println();	
             System.out.println();	
           }
         }
       }			
       
       if (count == 0) {
         System.out.println("Sorry, we could not find any animals which "
             + "are both fully trained and available.");	
       }
     } 
     
     else {
       System.out.println("There was an error reading which type of "
           + "list you would like to print. Please try again from the "
           + "main menu.");
     }
     
     runSubLoop = false;
   }
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 