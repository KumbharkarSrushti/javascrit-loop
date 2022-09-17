var i=0
var sum=0
const a = require("readline-sync");
var n = a.questionInt("enter the number: ");
while (i <=n){
    num=a.questionInt("enter the number: ");
    sum=sum+num
    i=i+1
    console.log(sum)
}