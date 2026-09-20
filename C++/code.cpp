// To print something in C++, we'll go from compilation to execution, such that, g++ code.cpp && ./a.exe  

#include <iostream>
using namespace std;
// This is the starting point of execution of the program
int main() {
    int age = 7;
    char grade = 'A';
    float PI = 3.14f; // f is used to tell the compiler that this is a float value
    bool isSafe = true;
    
    cout << sizeof(age)<< endl; // sizeof() returns size of variable in bytes
    cout << grade << endl;
    cout << PI << endl;
    cout << isSafe << endl;
    return 0; //always use ; at end of statement in C++. called Terminator 
}

// The above all code is basically called the "Boilerplate Code" which is going to be written in every C++ program

