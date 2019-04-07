var rl = require("readline-sync");
var S = rl.question("Enter : ").split(" ").join("").toLowerCase();
var rt = Math.sqrt(S.length);
var row = Math.floor(rt)
var col = Math.ceil(rt)
var mainArr = []
var m = 0
var c = ""
console.log(row,col)
for(let l of S){
    c = c+l
    if(c.length==col){
        mainArr.push(c)
        c = ""
    }
}
if(c.length!=0){
    mainArr.push(c)
}
console.log(mainArr)
var s = ""
for(let i = 0; i < mainArr[0].length; i++){
    for(let j = 0; j < mainArr.length; j++){
        if(mainArr[j][i] == undefined){
            break
        }
        else{
            s = s + mainArr[j][i]
        }
    }
    s = s + " "
}
console.log(s)