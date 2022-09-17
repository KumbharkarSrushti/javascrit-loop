const a = require("readline-sync");
var n = a.questionInt("enter the number: ");
var i =1
var sum=0
while (i <=n) {
    sum=sum+i
    console.log(i-1)
    i=i+1
}
console.log(n)
console.log("=",sum)