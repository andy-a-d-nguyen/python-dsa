# Memory addresses

- The &("address-of") operator produces a value's memory address.
  - Usually written as hex (base-16) numbers

# Pointers

```cpp
type* name = address;
```

- Pointer: A variable that stores a memory address
  - In the code bellow, p points to x
  ```cpp
  int x = 42;
  int* p = &x;
  cout << p << endl; // 0x7f8e20
  ```
  - The int x is the "pointee" of the pointer p
  - The pointer is also a variable that occupies memory

## Dereferencing a pointer

*p means "the value that p points to"
- This is called dereferencing the pointer

```cpp
int x = 42;
int* p = &x;

// access the pointee
cout << p << endl; // 0x7f8e20
cout << *p << endl; // 42

// modify the pointee
*p == 99;
cout << x << endl; // 99
```

## Null/garbage pointers

- Null pointer: Memory address 0; "points to nothing"
- Uninitialized pointer: Points to a random address
- If you dereference these, the program will probably crash

```cpp
int x = 42;
int* p1 = nullptr;   // stores 0
int* p2;             // uninitialized
cout << p1 << endl;  // 0
cout << *p1 << endl; // crash
cout << *p2 << endl; // crash

// testing for nullness
if (p1 == nullptr) {...} // true
if (p1)            {...} // false
if (!p1)           {...} // true
```

## Pointer to a struct

```cpp
type* name = new type(parameters);
```

- Creates a new struct or object and returns a pointer to it
- Operator -> refers to members of the object

```cpp
Date* d1 = new Date();
d1->month = 7;
d1->day = 13;

Date* d2 = d1;
d2->month = 9;

cout << d1<-month << endl; // 9
cout << d1<-day << endl; // 13
```

## Non-pointer vs pointer initialization

Non-pointer:

```cpp
void foo() {
    Date d1;
    d1.month = 7;
    d2.day = 13;
    ...
} // d1 is thrown away when the scope ends
```

Pointer:

```cpp
void foo2() {
    Date* d2 = new Date();
    d2->month = 7; // equivalent to (*d2).month = 7;
    d2->day = 13;
    ...
} // d2 is NOT thrown away when the scope ends
```

## Reassigning pointers

- When you say:
  - ```cpp
    a->next = b -> next  
    ```
- You are saying:
  - "Make the variable `a->next` refer to the same value as `b->next`"
  - Or, "make `a->next` point to the same place that `b->next` points"

### Incorrect code

```cpp
void addFront(ListNode* front, int value) {
  ListNode* temp = new ListNode(value);
  temp->next = front;
  front = temp;
}

int main() {
  ListNode* list = ...;
  addFront(list, 10);
}

// front and list are separate pointers because list was passed as a value to addFront
// when front points to temp
// list is still pointing to the original front
```

### Modify list by reference

- When writing functions that modify a list, you must pass the front by reference so that the change will be seen in 
  main
  - The function's pointer directly refers to main's pointer; not a copy

```cpp
void addFront(ListNode*& front, int value) {
  ...
}

// Now, the same pointer that was used in the calling function is passed to addFront
```

### Correct code

```cpp
void addFront(ListNode*& front, int value) {
  ListNode* temp = new ListNode(value);
  temp->next = front;
  front = temp;
}

int main() {
  ListNode* list = ...;
  addFront(list, 10);
}

// front is now an alias for list, not a new pointer (copy) of list
```

# The keyword const

- A const reference parameter can't be modified by the function

```cpp
void foo(const BankAccount& ba) {...}
```

- A const member function can't change the object's state:

```cpp
class BankAccount {
  double getBalance() const;
}
```

# Operator overloading

- Operator overloading: Redefining the behavior of a common operator in the C++ language
- Syntax:
  ```cpp
  returnType operator op(parameters); // .h
  returnType operator op(parameters) { // .cpp
    statements;
  };
  ```
- Example: `a + b` becomes `operator +(Foo& a, Foo& b)`

# Make objects printable

- To make it easy to print your object to cout, overload `<<`
  ```cpp
  ostream& operator <<(ostream& out, Type& name) {
    statements;
    return out;
  }
  ```
- `ostream` is a base class that represents `cout`, file output streams, ...

# Destructor

```cpp
~Classname(); // .h

Classname::~ClassName() {...} // .cpp
```

- Destructor: Called when the object is deleted by the program (when the object falls out of {} scope)
  - Useful if your object needs to free any memory as it dies
    - `delete` for any pointers stored as private members
    - `delete[]` for any arrays stored as private members