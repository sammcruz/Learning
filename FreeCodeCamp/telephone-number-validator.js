function telephoneCheck(str) {

  // test if there's special characters
  if (/[^\d()-\s]/.test(str)){return false}

  const replaced = str.replace(/\D/gi, '');

  if (replaced.length > 11 || replaced.length < 10){ return false

  } else if (replaced.length == 11 && replaced[0] == 1){ 
    
    return /^(1\s?)(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}/.test(str)

  } else if (replaced.length == 11 && replaced[0] != 1){ return false 
  
  } else if (replaced.length == 10){
    return /^(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}/.test(str)

  }
}

// TESTS
console.log("true: ", telephoneCheck("555-555-5555"));
console.log("true: ", telephoneCheck("1 555-555-5555"))
console.log("true: ", telephoneCheck("1 (555) 555-5555"))
console.log("true: ", telephoneCheck("5555555555") )
console.log("true: ", telephoneCheck("555-555-5555"))
console.log("true: ", telephoneCheck("(555)555-5555"))
console.log("true: ", telephoneCheck("1(555)555-5555") )
console.log("true: ", telephoneCheck("1(555)555-5555"))
console.log("false: ", telephoneCheck("555-5555"))
console.log("false: ", telephoneCheck("5555555"))
console.log("false: ", telephoneCheck("1 555)555-5555"))
console.log("true: ", telephoneCheck("1 555 555 5555"))
console.log("true: ", telephoneCheck("1 456 789 4444"))
console.log("false: ", telephoneCheck("123**&!!asdf#"))
console.log("false: ", telephoneCheck("55555555"))
console.log("false: ", telephoneCheck("(6054756961)"))
console.log("false: ", telephoneCheck("2 (757) 622-7382"))
console.log("false: ", telephoneCheck("0 (757) 622-7382"))
console.log("false: ", telephoneCheck("-1 (757) 622-7382"))
console.log("false: ", telephoneCheck("2 757 622-7382"))
console.log("false: ", telephoneCheck("10 (757) 622-7382"))
console.log("false: ", telephoneCheck("27576227382"))
console.log("false: ", telephoneCheck("(275)76227382"))
console.log("false: ", telephoneCheck("2(757)6227382"))
console.log("false: ", telephoneCheck("2(757)622-7382"))
console.log("false: ", telephoneCheck("555)-555-5555"))
console.log("false: ", telephoneCheck("(555-555-5555"))
console.log("false: ", telephoneCheck("(555)5(55?)-5555"))
console.log("false: ", telephoneCheck("55 55-55-555-5"))
console.log("false: ", telephoneCheck("11 555-555-5555"))