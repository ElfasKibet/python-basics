function hi() {
  console.log("Good evening");
}

hi();

console.log(4 + "3");
console.log(typeof 4.5);
// comment

/**
 * Multiline
 */
let name = "John";
let name2 = String("Jane");
const fullName = `${name} Doe`;

let greeting = Number("45");
console.log(greeting);
console.log(typeof greeting);

// boolean expressions

// !! -> boolean constructor
console.log(!!"");
console.log(Boolean(0));
let isAdult = true;
// strings
// booleans
// numbers
// arrays
// null
// undefined
// objects

const person = {
  name: "Jane",
  address: {
    county: "Mombasa",
  },
};

console.log(person.address["county"]);
console.log(person["address"].county);

const { address } = person;

const colors = ["Blue"];
const cars = Array("");

console.log(colors.length === 0);

function sum(numbers = []) {
  console.log(numbers);
  //   checks if the array is empty
  if (numbers.length == 0) return 0;

  let sum = 0;

  //   using for loop
  //   for (let i = 0; i < numbers.length; i++) {
  //     sum += numbers[i]
  //   }
  numbers.forEach((number) => {
    sum += number;
  });

  // return sum;
  // reduce method -> aggregate arrays to single values
  return numbers.reduce((prev, curr) => prev + curr, 0);
}

console.log(sum([]));
console.log(sum([1, 3, 4]));

function printArray(array = []) {
  //show me the code!
  return array.join("");
}

console.log(printArray(["h", "o", "l", "a"]));
