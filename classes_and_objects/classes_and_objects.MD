# Classes and Objects

- Class: A template for a new type of object
- Object: Entity that combines state and behavior
  - Object-oriented programming (OOP): Programs that perform their behavior as interactions between objects
  - Abstraction: Separation between concepts and details

## Elements of a class

- Member variables: State inside each object
  - Also called "instance variables" or "fields"
  - Each object has a copy of each member
- Member functions: Behavior inside each object
  - Also called "methods"
  - Each object has a copy of each method
  - The method can interact with the data inside that object
- Constructor: Initializes new objects as they are created
  - Sets the initial state of each new object
  - Often accepts parameters for the initial state of the fields

## Using objects

- An object groups multiple variables together
  - Each object contains a name and balance field inside it
  - We can get/set them individually
  - Code that uses your objects is called client code

## The implicit parameter

- Implicit parameter:
  - The object on which a member function is called
  - Ex: During the call account1.deposit(...), the object account1 is the implicit parameter
  - The member function can refer to that object's member variables
    - We say that it executes in the context of a particular object
    - The function can refer to the data of the object it was called on
    - It behaves as if each object has its own copy of the member functions

## Arrays in C++

```c++
type* name = new type[length];
```

- A dynamically allocated array
- The variable that refers to the array is called a pointer
- The memory allocated for the array must be manually released or else the program will have a memory leak
- Another type of array creation syntax:
  ```cpp
  type name[length];
  ```
  - A fixed array; initialized at declaration; can never be resized
  - Stored in a different place in memory; the first syntax uses the heap and the second uses the stack

### Array initialization

```cpp
type* name = new type[length]; // uninitialized
type* name = new type[length](); // initialize to 0
```

- If () are written after the array [], it will set all array elements to their default zero-equivalent value for 
  the data type (slower)
- If no () are written, the elements are uninitialized so whatever garbage values were stored in that memory 
  beforehand will be your elements.