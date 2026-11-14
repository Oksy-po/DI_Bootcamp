// Instructions

// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

let star = "*"
let stars=""
for (let i=1; i <7; i ++){
    stars = stars + star
    console.log(stars)
}

let secondStar = "*"

for (let i = 1; i <= 7; i++) {
   let otherStars=""
  for (let j = 1; j<= i ; j++) {
    otherStars=secondStar +otherStars
  }
  console.log(otherStars)
}