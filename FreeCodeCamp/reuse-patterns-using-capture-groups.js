let repeatNum = "42 42 42";
let reRegex = /^(\d+) \1 \1$/g; // Change this line
let result = reRegex.test(repeatNum);

console.log(reRegex.test("42 42 42 42"))