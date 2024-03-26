# c++

- i/o while-loop repl 

```cpp
/*
 * Expressions.cpp
 *
 * Date: 3/24/24
 * Author: Ashley Grevelink
 */

#include <iostream>
using namespace std;

int main() {
    char statement[100];
    int op1, op2;
    char operation;
    char answer = 'y';

    while (answer == 'y' || answer == 'Y') {

        cout << "Enter expression" << endl;
        cin >> op1 >> operation >> op2;

        if (operation == '+') {
            cout << op1 << " + " << op2 << " = " << op1 + op2 << endl;
        }
        else if (operation == '-') {
            cout << op1 << " - " << op2 << " = " << op1 - op2 << endl;
        }
        else if (operation == '*') {
            cout << op1 << " * " << op2 << " = " << op1 * op2 << endl;
        }
        else if (operation == '/') {
            cout << op1 << " / " << op2 << " = " << op1 / op2 << endl;
        }

        cout << "Do you wish to evaluate another expression? " << endl;
        cin >> answer;

        if (answer == 'n' || answer == 'N') {
            cout << "Program finished." << endl;
        }
    }
    return 0;
}
```