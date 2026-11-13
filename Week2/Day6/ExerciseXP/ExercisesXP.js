// Exercise 1 : List of people

// Instructions
// Part I - Review about arrays

// Write code to remove “Greg” from the people array.people.

const people = ["Greg", "Mary", "Devon", "James"];
const updatedListOfPeople=people.shift();
console.log(updatedListOfPeople);
console.log(people);

// Write code to replace “James” to “Jason”.

people[2]="Jason";
console.log(people);

// Write code to add your name to the end of the people array.

people.push("Oksana");
console.log(people);

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

console.log(people.indexOf("Mary"));

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

const copiedListOfPeople=people.slice(1,3);
console.log(copiedListOfPeople);


// Write code that gives the index of “Foo”. Why does it return -1 ?

console.log(people.indexOf("Foo"));


// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?


const last=people[people.length -1];
console.log(last);

// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.


for (const person of people){
    console.log(person)
};
// Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
// Hint: take a look at the break statement in the lesson.


for (const person of people) {
    console.log(person);
    if (person === "Devon") {
    break;
  }

  
};


//  Exercise 2 : Your favorite colors

// Instructions

// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

let colors=["green","orange","yellow","white","black"];


// for (let i = 0; i < colors.length; i++) {
//   console.log("My #" + (i+ 1) + " choice is " + colors[i]);
// }


for (let i = 0; i < colors.length; i++) {
  switch (i + 1) {
  case 1:
    console.log("My " + (i+1) + "st choice is " + colors[i]);
    break;
  case 2:
    console.log("My " + (i+1) + "nd choice is " + colors[i]);
    break;
  case 3:
    console.log("My " + (i+1) + "rd choice is " + colors[i]);
    break;
  default:
    console.log("My " + (i+1) + "th choice is " + colors[i]);
}}


// Exercise 3 : Repeat the question

// Instructions

// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let userInput;

do {
  userInput = Number(prompt("Give me number"));
} while (userInput < 10);

console.log(typeof userInput);


// Exercise 4 : Building Management

// Instructions:

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}


// Console.log the number of floors in the building.
console.log(building.numberOfFloors)

// Console.log how many apartments are on the floors 1 and 3.
console.log("Apartments on the floor 1 are " + building.numberOfAptByFloor.firstFloor + " and apartments on the floor 3 are " + building.numberOfAptByFloor.thirdFloor)

// Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log("Name of the second tenant is "+ building.nameOfTenants[1]+" and the number of rooms he has "+ building.numberOfRoomsAndRent.dan[0])

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

if ((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]){
    building.numberOfRoomsAndRent.dan[1]=1200
  }
console.log(building)


// Exercise 5 : Family

// Instructions

// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.


const family={
  father:"Tim",
  mother:"Kim",
  son:"Pit",
  daughter:"Nik"
}

for (const key in family) {
  console.log(key);
}

for (const value in family) {
  console.log(value);
}


// Exercise 6 : Rudolf

// Instructions

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}
// Given the object above and using a for loop, console.log “my name is Rudolf the reindeer”

let sentence = "" 

for (const key in details){
  sentence = sentence + key + " " + details[key]
  
}

console.log(sentence)


// Exercise 7 : Secret Group

// Instructions

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

let secretSociety=""
names.sort()
for (const name of names){
    if (!secretSociety.includes(name[0])) {
      secretSociety=secretSociety + name[0]
    }
}

console.log(secretSociety)