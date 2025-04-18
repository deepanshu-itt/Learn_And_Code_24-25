class Employee {

    string name;
    
     int age;
    
     float salary;
    
    public : string getName();
    
    void setName(string name);
    
     int getAge();
    
    void setAge(int age);
    
    float getSalary();
    
    void setSalary(float salary);
    
     };
    
// Employee employee;
    
// Is 'employee' an object or a data structure? Why?



//--------------------------------------------Solution-----------------------------------------//

// Here employee is the object as according to clean code Objects hide their data behind
// abstractions and expose functions that operate on that data. While Data structure expose data
// and have no meaningful functions.
