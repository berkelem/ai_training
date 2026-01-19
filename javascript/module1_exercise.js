// Module 1 Exercise: JavaScript Fundamentals for Python Developers
// Complete each task below. Run with: node module1_exercise.js

console.log("=== Module 1 Exercise ===\n");

// ============================================
// Task 1: Variables & Array Methods
// ============================================
// TODO: Create a constant array called 'numbers' with values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// TODO: Use .map() to create a new array 'squared' with each number squared
// TODO: Use .filter() to create a new array 'evens' with only even numbers from 'numbers'
// TODO: Log both arrays

// Your code here:

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const squared = numbers.map(x => x ** 2);
const evens = numbers.filter(x => x % 2 ===0);
console.log(squared)
console.log(evens)

// ============================================
// Task 2: Arrow Functions
// ============================================
// TODO: Create an arrow function called 'greet' that takes a name parameter
//       and returns "Hello, [name]!" using template literals
// TODO: Create a concise arrow function called 'double' that takes a number and returns it doubled
// TODO: Test both functions with console.log

// Your code here:

const greet = (name) => {
    return `Hello, ${name}`;
}
const double = (number) => 2 * number;
console.log(greet("John"))
console.log(double(45))


// ============================================
// Task 3: Objects & Destructuring
// ============================================
// TODO: Create an object called 'person' with properties: name, age, city
// TODO: Use object destructuring to extract name and age into separate variables
// TODO: Create a new object 'updatedPerson' using the spread operator {...person}
//       and update the age to be age + 1
// TODO: Log the original person and updatedPerson

// Your code here:
const person = { name: "Alice", age: 30, city: "New York" };
const { name, age, _ } = person;
const updatedPerson = {...person, age: age + 1};
console.log(person)
console.log(updatedPerson)



// ============================================
// Task 4: Array Destructuring
// ============================================
// TODO: Create an array called 'colors' with at least 5 color names
// TODO: Use array destructuring to extract the first, second, and rest of colors
//       Hint: const [first, second, ...rest] = colors;
// TODO: Log first, second, and rest separately

// Your code here:
const colors = ["red", "blue", "green", "yellow", "orange"];
const [first, second, ...rest] = colors;
console.log(first);
console.log(second);
console.log(rest);



// ============================================
// Task 5: Combining Methods
// ============================================
// TODO: Create an array of objects representing products:
//       [{ name: "Laptop", price: 1000 }, { name: "Mouse", price: 25 }, { name: "Keyboard", price: 75 }]
// TODO: Use .filter() to get products that cost less than 100
// TODO: Use .map() to create an array of just the names of these affordable products
// TODO: Log the result

// Your code here:

const products = [{ name: "Laptop", price: 1000 }, { name: "Mouse", price: 25 }, { name: "Keyboard", price: 75 }]
const lessthan100 = products.filter(x => x.price < 100);
const affordableProducts = lessthan100.map(x => x.name);
console.log(affordableProducts);


console.log("\n=== Exercise Complete ===");
