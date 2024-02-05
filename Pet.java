/**
 * Author: Ashley Grevelink
 * Date: February 4, 2024
 * 
 * This class can be used to create an 
 * object of type Pet, or to access/change 
 * the static global variables associated
 * with the class.
 * 
 * It does not implement any interfaces
 * or extend any classes (other than the
 * implicit inheritance of the Object class.)
 * 
 * This class can be extended by a sub-class.
 */
public class Pet {

  /**
   * Declares private member variables that will
   * be a unique set of values for an object 
   * instance if one is created using this class.
   *  
   * This section does not initialize the 
   * variables because a constructor would do 
   * that instead.  
   */
  private String petType;
  private String petName;
  private int petAge;
  private int daysStay;
  private double amountDue;

  /**
   * These static member variables belong to
   * the class and not any instance. 
   */ 
  private static int dogSpaces;
  private static int catSpaces;

  /**
   * A Pet constructor with no parameters. It calls
   * the Pet constructor with five parameters and 
   * passes five default arguments which initializes 
   * all of its instance fields.
   */ 
  public Pet () {
    this(null, null, 0, 0, 0.0);
  }

  /**
   * This constructor is used if an employee has asked
   * a customer for the petType without knowing if
   * there is currently room for the pet to stay at
   * Pet BAG. The employee won't ask for more info
   * if there is no available space. But it's still 
   * useful business information because Pet BAG
   * is interested in maybe raising their capacity 
   * eventually.
   * 
   * It calls the Pet constructor with five parameters
   * like the default constructor, except it passes a
   * petType that is not necessarily null, and then 
   * four default values.
   */ 
  public Pet (String type) {
    this(type, null, 0, 0, 0.0);
  }

  /**
   * This constructor has 5 parameters, corresponding
   * to all the possible information for the 5 private 
   * member variables of a Pet object.
   * 
   * An employee can use this upon either check-in or
   * check-out.
   */ 
  public Pet (String type, String name, int age, int days, double amount) {
    petType = type;
    petName = name;
    petAge = age;
    daysStay = days;
    amountDue = amount;
  }

  /**
   * The following methods are all sets of getters
   * and setters. Two sets are static and use the
   * class global variables, and the remaining five
   * sets are not static and use `this` to get the
   * reference to the object instance that would
   * call the getter/setter. 
   * 
   * All of these methods are public, whereas all 
   * the variables they access are private, which
   * follows the Java best practices of encapsulation.
   */

  public String getPetType() {
    return this.petType;
  }

  public void setPetType(String petType) {
    this.petType = petType;
  } 

  public String getPetName() {
    return this.petName;
  }

  public void setPetName(String petName) {
    this.petName = petName;
  } 

  public int getPetAge() {
    return this.petAge;
  }

  public void setPetAge(int petAge) {
    this.petAge = petAge;
  } 

  public static int getDogSpaces() {
    return dogSpaces;
  }

  public static void setDogSpaces(int spaces) {
    dogSpaces = spaces;
  } 

  public static int getCatSpaces() {
    return catSpaces;
  }

  public static void setCatSpaces(int spaces) {
    catSpaces = spaces;
  } 

  public int getDaysStay() {
    return this.daysStay;
  }

  public void setDaysStay(int daysStay) {
    this.daysStay = daysStay;
  } 

  public double getAmountDue() {
    return this.amountDue;
  }

  public void setAmountDue(double amountDue) {
    this.amountDue = amountDue;
  } 

}
