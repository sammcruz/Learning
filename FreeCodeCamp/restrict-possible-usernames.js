let username = "JackOfAllTrades";
let userCheck = /^[a-z](\d{2,}|[a-z]+\d*)$/i; // Change this line
let result = userCheck.test(username);