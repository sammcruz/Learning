// Only change code below this line
let chewieRegex = /Aa*/g; // Change this line
// Only change code above this line

let result = chewieQuote.match(chewieRegex);

console.log(result)
console.log("He made a fair move. Screaming about it can't help you.".match(chewieRegex))
console.log("Let him have it. It's not wise to upset a Wookiee".match(chewieRegex))