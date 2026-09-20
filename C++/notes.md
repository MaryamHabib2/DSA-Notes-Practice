## For storing an integer in Memory
- One integer = 4 bytes in a memory
- Computer understand binary numbers 0 and 1
- 0 and 1 is one digit
- this one digit takes one bit 
- 1 byte = 8 bits
- So, 4 bytes = 8 * 4 = 32 bits 
- So, one integer takes 32 bits in a memory
- In computer memory, always the number stored in binary form (0 and 1)

# When we are storing an integer in a variable, this integer reserves 32 bit spaces in our memory, and that integer gets stored in those spaces in the form of 0 and 1. 

We can use "sizeof(variable)" function to print the size of a particular variable based on its data type. If it is an integer, it will print 4 

## For Storing Characters in Memory
- We convert the character into ASCII value before storing it into memory
- One char = 1 byte
- ASCII = American Standard Code Information Interchange
- For example, A has a fixed ASCII value of 65, B of 66, C of 67 and a has 97, b has 98 and so on.
- Compiler then convert these ASCII values to binary numbers and then store them in memory

- Good Engineers and Programmers generally represent a variable, whose value is constant, in "UPPERCASE" 

## Rule for storing float values in C++
Use f with the value otherwise the compiler think that we're using a double value
- e.g., float PI = 3.14f;

float = 4 bytes 

## Boolean Datatype
- bool = 1 byte 
- boolean datatype has only two values 'true' and 'false'
- true is stored as 1 in our memory and false is stored as 0 in the memory
- e.g., bool isSafe = true;
- Output: 1

