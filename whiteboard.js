// Problem #1 - Classic Fizz Buzz
// Write a program that prints the numbers from 1 to 100. For multiples of 3, print 'Fizz'. For multiples of five, print 'Buzz'. For numbers that are multiples of both three and five, print 'Fizz Buzz'
// Solution 
for (let i = 1; i <= 100; i++) {
  let string = i;
  if (i % 3 == 0) {
    string += " Fizz";
  }
  if (i % 5 == 0) {
    string += " Buzz";
  }
  console.log(string);
}

// Problem #2 - Write a multiply function that multiples 2 integers without using *
// Solution 
function multiply(num1, num2) {
    let value = 0;
    for (let i = 0; i < num1; i++) {
        value += num2
    }
    return value;
}

let answer = multiply(5, 10);
console.log(answer);
