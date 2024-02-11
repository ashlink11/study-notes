# meta

- statement: cannot be evaluated, but can be executed bc they are imperative instructions that perform an action or assign a value
- expression: can be evaluated and result in single value
- equation: expresses relationship between two expressions, asserting their equality; evaluating means finding the values of variables that make the equation true (only in math, not java)
- function: is evaluated for each input, yielding the output

- OOP composition
  - modular, reusable, maintainable, loosely-coupled
  - uses abstract classes
  - not monolithic
- functional composition
  - compose `f(x)` and `g(x)` to `h(x) = f(g(x))`

https://blog.sigma-star.io/2024/01/people-dont-understand-oop/ (#todo: read more)
- classes, prototypes and structs can create objects (OOP)
  - languages with objects:
    - javascript
    - python
    - typescript
    - java
    - c#
    - c++
    - (not C)
    - Go
    - Rust
    - Kotlin
    - Ruby
- subtyping:
  - Javascript: inheritance and duck typing
  - Python: ","
  - TypeScript: ",", and structural typing
  - Java: inheritance and nominal typing
  - C#: ","
  - C++: ",", and structural typing (concepts)
  - C: n/a
  - Go: structural typing
  - Rust: extension traits & nominal typing
  - Kotlin: inheritance, nominal typing
  - Ruby: inheritance, duck typing
- explanation of concepts:
  - structural typing: compatibility is based on presence of methods/properties regardless of explicit declarations
  - duck typing: pretty similar^ and doesn't use inheritance
  - nominal typing: compatibility is determined by explicit type names 
  

# chapter 1 notes

```java
import java.util.Scanner;

public class Example {
  public static void main(String [] args) {
    Scanner scnr = new Scanner(System.in);
    System.out.print()
    System.out.println() //newline after
  }
}
```

compiler errors: can be incorrect (e.g. missing paren instead of semicolon) and be caught after the line with the actual error

compiler warnings: reported during compilation; make suggestions (i.e. divide by 0 error)

"By default, Java compilers don't print every possible warning. Ex: A programmer's Java code may use something old that has a newer, better alternative. The compiler recognizes this, but since the code may still run fine, no warning is given. So, many programmers recommend the good practice of configuring compilers to be more picky with warnings than the default."

`javac -Xlint yourfile.java //compiles w all warnings` 

style notes: 
- indent with 3 spaces
- var/param names at least 2 words
- declare vars early but initialized when practical
- one use one underscore
- must start with letter

debugging:
- buffer overflow testing includes testing small and large numbers in case occasionally the output is different; also can hand-calculate to see if the value is above the variable's size

JVM compiler: may allocate variables on the stack or in registers

- expression: values, variables, or both (operators and operands)
- evaluate: find the value of an expression when a variable is a certain value
- solve: find an expression that defines a variable
- integer literal: i.e.: 13
- 
- 

## Reserved words

abstract
assert
boolean
break
byte
case
catch
char
class
const
continue
default
do
double
else
enum
extends	final
finally
float
for
goto
if
implements
import
instanceof
int
interface
long
native
new
package
private
protected	public
return
short
static
strictfp
super
switch
synchronized
this
throw
throws
transient
try
void
volatile
while

true, false, null (for literals)



## precedence rules

```
1. ()
2. unary minus -
3. * / %
4. + -
5. left to right
```

## data types

- use 0.0, 1.0, etc. for doubles (floats)
- floating-point number: real number with a decimal point that can float in the number
- floating-point literal: number with a fractional part (e.g. 0.0, 1.0)
- NaN: some division by 0
- 12.0 / 0.0 = positive infinity
- -12.0 / 0.0 = negative infinity
- 0.0 / 0.0 = NaN
- `System.out.printf("%.2f", myFloat);` // rounds the last digit, but remains intact in the floating point & ALSO PRINTS NEWLINE
- byte: 8 bits -128 to 127
- short: 16 bits -32,768 to 32, 767
- int: 32 bits -2.1b to 2.1b ish (10 digits)
- long: 64 bits -9 quintillion to 9 quintillion ish
- float: 32 bits -3e38 to 3e38 (7 sig digits)
- double: 64 bits -2e308 to 2e308 (16 sig digits)
- one bit for sign, some bits for mantissa and some for exponent
- overflow with floating-point results in infinity
  

## standard library features

```java
import java.util.Random;

Random randGen = new Random();  // New random number generator
randGen.setSeed(5); // same sequence

System.out.println(randGen.nextInt());

```

- pseudo-random: if seeded, yields the same sequence, with the next number computed from the previous one. millions of numbers can be generated without reaching a repeating pattern within the sequence
- constant variable = final variable
- `final int FLAT_FEE_CENTS = 75;`
- `Math.sqrt(x)`, `Math.PI`, `Math.pow(x,y)`, `Math.abs(x)`
- integer division: truncates the remainder, so there is no fraction (floors it)
- if there's any double, then floating-point arithmetic is used
- modulo (%): remainder (100 % 0 = Error) (0 % 7 = 0)
- can also use randNum with modulo to generate a random number within a range (can use +/- too)
- can use modulo and division in succession to get ones/tens/hundreds digits, etc., because it shifts right and left


```java
onesDigit     = userVal % 10;    // Ex: 927 % 10 is 7. 
tmpVal        = userVal / 10;

tensDigit     = tmpVal % 10;     // Ex: tmpVal = 927 / 10 is 92. Then 92 % 10 is 2.
tmpVal        = tmpVal / 10;

hundredsDigit = tmpVal % 10;     // Ex: tmpVal = 92 / 10 = 9. Then 9 % 10 is 9.

int phoneNum = 1365551212;

int tmpVal = phoneNum / 10000; // / 10000 shifts right by 4, so 136555. 
int prefixNum = tmpVal % 1000; // % 1000 gets the right 3 digits, so 555.
```

## type conversions

- implicit converstion (automatic)
- type casting: explicit conversion: precede an expression with (type)
- `avgKidsPerFamily = (double)(kidsInFamily1 + kidsInFamily2) / (double)numFamilies`

## more types

- char: character literal
- `myChar = scnr.next().charAt(0);`
- ASCII standard (C/C++) 8 bits
- Unicode (Java, etc.) 16 bits
- integer literal
- escape sequences: `\n \t \' \" \\`
- compiler treats escape sequences as single characters with one ASCII value

```java
      a = scnr.next().charAt(0);
      b = scnr.next().charAt(0);
      c = scnr.next().charAt(0);
```

- string literal 
- String data type is an object
- `userName = "Sarah";`, not `userName = new String("Sarah");`
- whitespace character: spaces, tabs, newlines
- `scnr.next()` omit first whitespace then gets chars until next whitespace, e.g. will leave a newline char at the end of the line bc only scans to the last char; it will skip over newlines too to the next line
- `scnr.nextLine()` gets entire line including leading spaces ; if after a `next()`, get the rest of the line; remember it doesn't skip leading whitespace, so sometimes the rest of the line will just be a newline; if it gets a whole line though it consumes the newline at the end

## overflow

- compiler message: "possible loss of precision"
- be careful of intermediate calculations

## exceptions
- InputMismatchException
















# chapter 2 notes

terminology:
- void method
- incremental design (using method stubs which return 0)
- modular design
- stack frame (holds local vars)
  - call & return are push and pop
  - arguments are copied to the parameters and become local variables; invoking a method also stores a return address to jump back to
- class scope: a "field" is the name for a class member variable
- method scope: local variables and actually entire class too
- side effects: if a method updates a field
- access specifiers (e.g. private, protected) are for outside classes
- public class: other classes can access methods and actually also fields
- abstraction: aka information hiding and encapsulation. lower-level internal details are hidden. 
- abstract data type (ADT): a data type whose creation and update are constrained to specific well-defined operations. a class can be used to implement an ADT #todo: review more
  - which abstractions would a user understand?
  - getters and setters are reasonable but access to internal variables is not encapsulation because there's more risk involved with the wrong types and perhaps data races, idk
- class member variables exist and so do class' public member methods
- classes define a new type! omg of course! and can be used to create objects
- `.` is the member access operator
- reference variable: refers to an object
- #todo: how many bytes per char, int, double, etc.?
- Java automatically imports the `java.lang` package
- class members: fields and methods
- helper methods are private within a class and help the public methods
- Not finding any programmer-defined constructor, the compiler generates a constructor with no arguments. Initializes ints to 0.

```java
   public CarRecord () {
      yearMade = 0;
      vehicleIdNum = -1;
   }
```

- overload a constructor by making more than one with different signatures
- error if no signatures match
- must define a default constructor if created other constructors
- variables (#todo: fields?) of a class data type are reference variables
- when create object, allocates memory for its vars and returns a ref
- implicit parameter: e.g. person1.method(), 'person' is the implicit parameter bc it stands for an object
- within a member method, the implicitly-passed object is accessible via 'this'
- `this` differentiates between a class field and a parameter name
- reference to 'this' is passed implicitly
  calling overloaded constructor using `this`:

```java
  public class ElapsedTime {
   private int hours;
   private int minutes;

   // Overloaded constructor definition
   public ElapsedTime(int timeHours, int timeMins) {
      hours   = timeHours;
      minutes = timeMins;
   }
   
   // Default constructor definition
   public ElapsedTime() {
      this(0, 0);
   }
   
   // Other methods ...
}
```

  - `this(x, y)` in the body of the default constructor calls the overloaded constructor with the corresponding signature



```java

public class Cat extends Pet {
  private int catSpaceNumber;

  public Cat () {
    catSpaceNumber = 0;
  }

  public Cat (int catSpaceNumber) {
    this.catSpaceNumber = catSpaceNumber;
  }

  public int getCatSpaceNumber() {
    return catSpaceNumber;
  }

  public void setCatSpaceNumber(int num) {
    catSpaceNumber = num;
  } 

}

```










# chapter 3 notes

- myDouble == 3.26 compiles but invalid : due to imprecision of floating-point representations, such comparisons may yield unexpected results.
- myString == "Hello" compiles but invalid , unexpected results because of pointers 
- look up order of precedence if needed
- "For integral operand types such as int, & and | represent bitwise operators, which perform AND or OR on corresponding individual bits of the operands. Bitwise operators have highly-specialized usage, not common in beginning programs and not discussed here."
- switch statements: go to the next statement if there's no break
- cant use logical operators like AND and OR in switch cases

### Strings

- String comparison:
  - dont use `==`
  - use `str1.equals(str2)` and `!str1.equals(str2)`
  - `str1.equalsIgnoreCase(str2)`
  - `str1.compareToIgnoreCase(str2)`
  - `str1.compareTo(str2)` `< 0` `== 0` `> 0` unicode values
  - The `+` operator can return a new string that appends a string to another string. makes new string object. `s1.concat(s2)` is same and `str0 += str1` is same. they all use strings, not chars
  - `.length()` is used for Strings
  - use `==` for chars, e.g. `userInput.charAt(0) == firstLetter`

- more String operations
  - `str.indexOf()`  Item may be char, String variable, or string literal. returns `-1` if not in string
    - `str.indexOf(item)` gets index of first item occurrence in a string, else -1. Item may be char, String variable, or string literal.
    - `str.indexOf(item, indx)` starts at index indx.
    - `str.lastIndexOf(item)` finds the last occurrence of the item in a string, else -1.
  - `substring(startIndex)` (inclusive)
  - `substring(startIndex, endIndex)` (`endIndex` not inclusive)
  - `replace(findChar, replaceChar)` `replace(findStr, replaceStr)` so replace can use a char or String
  - strings are immutable, so cannot change a char at an index, for example

### Errors & comments

- Exception: runtime error: prints error message and terminates program
- `// FIXME:` best practices for comments todo


### Characters

- `Character` class
- `Character.toLowerCase(userStr.charAt(6))` doesn't return error if the char is `?`, just returns `?`

### Floats (doubles are floats too)

- "Avoid `float1 == float2`. Reason: Some floating-point numbers cannot be exactly represented in the limited available memory bits like 64 bits. Floating-point numbers expected to be equal may be close but not exactly equal."
- `Math.abs(x - y) < 0.0001` deemed equal
- 0.0001 is a common epsilon
- representations: 32-bit and 64-bit with sign, exponent, and mantissa
- small floating points can be stored accurately, like 0.0, 2.0 or 0.25
- for each number there is a nearest floating-point value with like 15 zeroes after the decimal before numbers other than 0

### Loops

- "A sentinel value is a special value indicating the end of a list"
- loop expression is "the expression checked for whether to enter the loop body"
- incrementing chars example:

```java

for(currentRow = 1; currentRow <= numRows; ++currentRow) {
         char colChar = 'A';
   for(currentColumn = 1; currentColumn <= numColumns; currentColumn++) {
      System.out.print("" + currentRow + colChar + " ");
      colChar++;
   }
}
```
output: `1A 1B 1C 2A 2B 2C 3A 3B 3C 4A 4B 4C 5A 5B 5C `

- `break` only breaks one level of a nested loop
- `continue` causes an immediate jump to the loop condition check (can improve readability)
- both can avoid excessive indenting/nesting within a loop
- don't use them too much though

- enumeration type (enum) 
  - set of named values
  - named constants
  - declares a new data type
  - `public enum LightState {RED, GREEN, YELLOW, DONE};`

```java
public enum HVACStatus {OFF, ON, AUTO};
HVACStatus systemStatus;
systemStatus = HVACStatus.ON;
```

- static methods can only directly call static methods, i.e. main() can only directly call static methods, but has to call non-static methods indirectly using their object instances

- unit testing: testing smallest units possible
- to do this, create a testbench, i.e. test harness (separate program) to check for method returns
- each unique set of input values is known as a test vector
- a unit: a method (typically)
- assert operator
- `assert testExpression : detailedMessage;`

```java
   public static void main(String[] args) {
      System.out.println("Testing started");

      assert (hrMinToMin(0, 0) == 0) : "Assertion (hrMinToMin(0, 0) == 0) failed";
      assert (hrMinToMin(0, 1) == 1) : "Assertion (hrMinToMin(0, 1) == 1) failed";
      assert (hrMinToMin(0, 99) == 99) : "Assertion (hrMinToMin(0, 99) == 99) failed";
      assert (hrMinToMin(1, 0) == 60) : "Assertion (hrMinToMin(1, 0) == 60) failed";
      assert (hrMinToMin(5, 0) == 300) : "Assertion (hrMinToMin(5, 0) == 300) failed";
      assert (hrMinToMin(2, 30) == 150) : "Assertion (hrMinToMin(2, 30) == 150) failed";
      // Many more test vectors would be typical...

      System.out.println("Testing completed");
   }
```

- border cases: fringe scenarios. "For a method, border cases might include 0, a very large negative number, and a very large positive number."
- e.g. three integer input method: "One might instead test dozens of normal cases, and perhaps ten or so border cases."

- `do-while` loops: first executes the loop body's statements, then checks the loop condition

```java
do {
   // Loop body
} while (loopExpression);
```

### discussion post:

There are four fundamental object-oriented (OOP) design principles: inheritance, encapsulation, abstraction, and polymorphism. 

An important idea in programming to prevent repeating code, so using inheritance (‘extends’) to create a sub-class prevents rewriting certain fields and methods, etc. Another way to prevent repeating code is with polymorphism, so you can use multiple different types as arguments and/or return values for a method. Less repetition means more reuse and more maintainability.

Other than preventing repetition of code, a second important programming idea is to simplify and work at a higher level of abstraction without too many complex details. Abstract classes use abstraction to define methods but not implement them, so the programmer can think on a higher level when designing a subclass. Encapsulation also allows programmers to avoid accidentally changing certain code that is either private or protected and work at a higher-level without being distracted by irrelevant details. 

Other than those important coding ideas, the four OOP principles work in other ways to make good applications. Encapsulation helps prevent side effects like changing fields you didn’t mean to, which makes the code more maintainable. Abstract classes depend on inheritance so their subclasses can be implemented. Polymorphism uses inheritance and method overloading to achieve dynamic types during the JVM compiler runtime. This means less code and therefore, more maintainable code.

The most interesting and also the think I need to learn more about in this class is polymorphism. It’s amazing that we can use multiple types in one method (I think). I would love to learn more about how the dynamic runtime works in the JVM.

- OOP composition: modular, not monolithic

I learned from you that polymorphism makes things adaptable. I hadn't thought of it like that I appreciate that you explained it in the clearest way possible so I could understand the high-level concept. I agree that it does mean that the compiler can adapt to different types during static binding and dynamic binding.

I find it interesting that you can distill the concepts into their most abstract forms, which must be helpful for your studies and coding.

I learned from you that a great application of inheritance would be for a video game with different main classes and specialized sub-classes of characters. Thanks for the example. Polymorphism started to make more sense when you explained it like that. I hadn't realized that polymorphism relates to both 'extends' and 'implements'. Thanks again.

I found it really interesting that you explained the OOP concept via an example, since I didn't think to use any examples in my post.



# chapter 4 notes


- arrays are initialized with values of 0
- NOTE PECULIARITY OF LANGUAGE: `.length` doesn't have () at the end because it's a property, not a method
- post-increment vs pre-increment : i++ use first value then increment, or ++i increment first value then use incremented value BUT NOT IN THE CONTEXT OF LOOPS ACTUALLY
- normal for-loop structure is with a < so it doesnt loop out of range

- `import java.util.ArrayList;`
- `ArrayList<Integer> vals = new ArrayList<Integer>()`
- ordered list of reference type items
- each item is an element
- doesn't support primitive types, but can use Integer, etc.
- reference types are the opposite of primitive types
- `add(elt)` `get(index)` `set(index, elt)` `size()`
- other Collections are LinkedList, Set, Queue, Map, etc.

- `for each` loop (enhanced for loop)

```java
for (String varThatGetsAssignedAValue : iterableTypes) {
  System.out.println(playerName);
}
```

- common error: "Modifying the loop variable in an enhanced for loop does not modify the array elements."
- iterable reference types include arrays and collections (lists, sets, maps, etc.), and they implement the `Iterable` interface
- arrays are reference types that can hold primitive types
- an interface is a reference type (#todo: ???)
- The primitive types in Java are `int, long, short, byte, float, double, char, and boolean` (not collections and not iterable) - to iterate over you would use an array of that primitive type or a wrapper from `java.util`
- 
- you can pass a `Scanner` from `main()` as an argument (it can be a parameter for a method)
- 

# chapter 5 notes

- derived class = subclass = child class
- base class = superclass = parent class
- the `protected` modifier provides access to derived classes and all classes in the same package (only)
- no modifier (`[default]` modifier): "Accessible by self and other classes in the same package." (i.e. "`[package-private]`")
- use `[package-private]` when creating class definitions instead of protected
- "Protected is not a valid specifier for class definitions and will produce an error."
- a derived class can override a base class's methods if they have an identical signature using `@Override` "so the compiler verifies that an identical base class method exists".
- `@Override` is an annotation that helps compiler
- overloading has different method signatures, i.e. same number of parameters but different parameter types
- "the `super` keyword is a reference variable used to call the parent class's methods or constructors"
`super.methodCall()`; if `methodCall()` is `@Override`
- infinite loop if you forget super because overridden method call would keep calling itself 
- you can also write other code in an an overridden derived class method other than calling `super.methodCall()`
- Object class is different than an object
- Object class has `toString()` and `equals(otherObject)`
- "by default, toString() returns a String containing the object's class name followed by the object's hash code in hexadecimal form. Ex: `java.lang.Object@372f7a8d`"
- `equals(otherObject)` compares the references, not the objects' contents
- Integer overrides `toString()` to return an `Integer` (?)

- Is-a versus has-a relationships
  - Composition: one object can be made of other sub-object attribute/member variables (has-a)
  - Inheritance: extending classes (is-a) 
- Unified Modeling Language (UML) diagrams are for class inheritance relationships
  - `#` protected
  - `-` private
  - `+` public

- static main and objects
  - static main can't directly call an instance method, but main can call the object, which then calls its member method, etc.
  - a constructor technically is an instance method too
- "Regression testing means to retest an item like a class anytime that item is changed; if previously-passed test cases fail, the item has "regressed". Regression testing means to check if a change to an item caused previously-passed test cases to fail."


## polymorphism: determining which code to execute depending on data types
- method overloading is a form of compile-time polymorphism (uses the methods arguments to determine the signature)
- runtime polymorphism: determination is made while program is running
- derived/base class reference conversion: e.g. if you're adding a SpecificItem to an ArrayList of GenericItems, the reference is converted to the base class reference without explicit casting 
- explicit casting is for double to int for example bc you have to explicitly do it to avoid an error
- that reference conversion is just for adding to an ArrayList for example but the original reference is retained so the proper overloaded methods can be called during runtime polymorhpism (I guess the compiler doesnt know it ahead of time, although I feel like it could #todo)

## class generics / generic classes
- class definition has a special type parameter that may be used in place of types in the class
- `public class TripleItem <TheType extends Comparable<TheType>> { ... }`
- a variable declared of the generic class type must indicate a specific types
- in `<TheType>`, `TheType` is the type parameter
- "A key advantage of generic classes is relieving the programmer from having to write redundant code that differs only by type."
- `public class ClassName <Type1 extends BoundType1, Type2 extends BoundType2> {...}`
- type bounds:
  - upper bound: `<T extends Number>` "In this example, T must be a subtype of Number."
  - lower bound: `List<? super T> list` "In this method, list must be a list of a type that is a supertype of T."
- generic methods too
  - `public static <TheType extends Comparable<TheType>> TheType tripleMin(TheType item1, TheType item2, TheType item3) {...}`
  - in this example `TheType` is just one type used multiple times in the sig

```java
public class Pair <T extends Comparable<T>> {
   private T item1;
   private T item2;

   public Pair(T i1, T i2) {
      item1 = i1;
      item2 = i2;
   }

   public T chooseItem() {
      T chosenItem;

      if (item1.compareTo(item2) > 0) { 
         chosenItem = item1;
      }
      else {
         chosenItem = item2;
      }
      return chosenItem;
   }
}
public class PairManager {
   public static void main(String[] args) {
      Pair<Integer> twoInts = new Pair<Integer>(37, 31); 
      Pair<Double> twoDbls = new Pair<Double>(42.3, 41.5);
      Pair<Character> twoChars = new Pair<Character>('k', 'b');

      System.out.println(twoInts.chooseItem());
      System.out.println(twoDbls.chooseItem());
      System.out.println(twoChars.chooseItem());
   }
}
```

## Module 5 lab

- `ItemToPurchase.java` 
- `ShoppingCartPrinter.java` // Driver example
- input:
```
Apple
1
3
Orange
2 
4 
```

```java
public class ItemToPurchase {
   //Private fields - itemName, itemPrice, and itemQuanity
   private String itemName;
   private int itemPrice;
   private int itemQuantity;
   
      /*Default Constructor
    itemName - Initialized to "none"
    itemPrice - Initialized to 0
    itemQuantity - Initialized ito 0
   */
   public ItemToPurchase() {
      itemName = "none";
      itemPrice = 0;
      itemQuantity = 0;
   }
   

   //public member methods (mutators & accessors)
   
   //setName() & getName() 
   
      public void setName(String itemName) {
      this.itemName = itemName;  
   }
   
   public String getName() {
      return this.itemName;  
   }
   
   //setPrice() & getPrice() 
   
   public void setPrice(int itemPrice) {
      this.itemPrice = itemPrice;  
   }
   
   public int getPrice() {
      return this.itemPrice;  
   }
   //setQuantity() & getQuantity() 
   
   public void setQuantity(int itemQuantity) {
      this.itemQuantity = itemQuantity;  
   }
   
   public int getQuantity() {
      return this.itemQuantity;  
   }
   
   //print item to purchase
   
   public void printItemPurchase() {
      System.out.println(itemName + " " + itemQuantity + " @ $" + itemPrice +  
                         " = $" + (itemPrice * itemQuantity));
   }
}

```


```java
import java.util.Scanner;

public class ShoppingCartPrinter {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int i = 0;
      String productName;
      int productPrice = 0;
      int productQuantity = 0;
      int cartTotal = 0;
      
  
      ItemToPurchase item1 = new ItemToPurchase();
      ItemToPurchase item2 = new ItemToPurchase();
      
      
      // Get item 1 details from user, create itemToPurchase object
      
      System.out.println("Item 1");
      
      System.out.println("Enter the item name: ");
      productName = scnr.nextLine();
      item1.setName(productName);
               
      System.out.println("Enter the item price: ");
      productPrice = scnr.nextInt();
      item1.setPrice(productPrice);
            scnr.nextLine();
            
      System.out.println("Enter the item quantity: ");
      productQuantity = scnr.nextInt();
      item1.setQuantity(productQuantity);
            scnr.nextLine();
 
       
      System.out.println("");
      
 
 
      // Get item 2 details from user, create itemToPurchase object

      System.out.println("Item 2");
      
      System.out.println("Enter the item name: ");
      productName = scnr.nextLine();
      item2.setName(productName);
            
      System.out.println("Enter the item price: ");
      productPrice = scnr.nextInt();
      item2.setPrice(productPrice);
            scnr.nextLine();
            
      System.out.println("Enter the item quantity: ");
      productQuantity = scnr.nextInt();
      item2.setQuantity(productQuantity);
      
      // Add costs of two items and print total
      // cartTotal = item one price + item two price
      // Totoal Cost
      // item one information
      // item two information
      // Total output
      
      System.out.println("");
      
      System.out.println("TOTAL COST");
      item1.printItemPurchase();
      item2.printItemPurchase();
      cartTotal = ((item1.getPrice() * item1.getQuantity()) 
               + (item2.getPrice() * item2.getQuantity()));
      
      System.out.println("");
             
      System.out.println("Total: $" + cartTotal);
      return;
   }
}
```





- a class with `main()` can be called `Driver.java`

# Milestone 5 --> Project 2

```java
import java.utils.Scanner;

public class Driver () {

  public static void main(args[]) {
    boolean done = false;
    String input;
    Scanner scnr = new Scanner(System.in);
    ArrayList<Monkey> monkeys = new ArrayList<Monkey>();

    while (!done) {
      displayMenu();
      input = scnr.next();
      // input validation &/or error messages
      // go to intakeNewMonkey();
    }
    

  }

}

```