function palindrome(str) {

  const replaced = str.replace(/[^a-z0-9]/gi, '').toLowerCase();
  const separado = replaced.split(" ")
  console.log(replaced); // 👉️ Abc
  for (let i=0; i < replaced.length; i++){
    if(replaced[i] != replaced[replaced.length-1-i]){
      return false
      console.log("NOT PALINDROME", replaced[i], "!=",replaced[replaced.length-1-i])
    }


  }
  return true;
}

//palindrome("eye");
console.log("true: ", palindrome("eye"))
console.log("true: ", palindrome("_eye"))
console.log("true: ", palindrome("race car"))
console.log("false: ", palindrome("not a palindrome"))
console.log("true: ", palindrome("A man, a plan, a canal. Panama"))
console.log("true: ", palindrome("never odd or even"))
console.log("false: ", palindrome("nope"))
console.log("false: ", palindrome("almostomla"))
console.log("true: ", palindrome("My age is 0, 0 si ega ym."))
console.log("false: ", palindrome("1 eye for of 1 eye."))
console.log("true: ", palindrome("0_0 (: /-\ :) 0-0"))
console.log("false: ", palindrome("five|\_/|four"))