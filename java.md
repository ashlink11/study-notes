
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
