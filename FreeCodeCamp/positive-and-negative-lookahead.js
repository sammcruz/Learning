let sampleWord = "astronaut";
let pwRegex = /([a-z]{1,})(?=\w{3,6})(?=\D*\d{2,})/; // Change this line
let result = pwRegex.test(sampleWord);