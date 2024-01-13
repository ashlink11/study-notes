
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