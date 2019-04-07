const rl = require("readline-sync");
const HW = Array.from(rl.question("Enter height and width : ").split(" ")).map(Number);
const H = HW[0];
const W = HW[1];
var mainArr = [];
var price = 0;
for(let i = 0;i < H; i++){
    w = Array.from(rl.question().split(" ")).map(Number);
    mainArr.push(w);
}
for(let j = 0; j < mainArr.length-1; j++){
    for(let k = 0; k < mainArr[j].length-1; k++){
        price+=((mainArr[j][k]*4)+2);
        if(mainArr[j][k] < mainArr[j][k+1]){
            price-=(mainArr[j][k]*2);
        }
        else{
            price-=(mainArr[j][k+1]*2);
        }
        if(mainArr[j][k] < mainArr[j+1][k]){
            price-=(mainArr[j][k]*2);
        }
        else{
            price-=(mainArr[j+1][k]*2);
        }
    }
}
var last = mainArr.length - 1;
for(let m = 0; m < mainArr[last].length - 1; m++){
    price+=((mainArr[last][m]*4)+2);
    if(mainArr[last][m] < mainArr[last][m+1]){
        price-=(mainArr[last][m]*2);
    }
    else{
        price-=(mainArr[last][m+1]*2);
    }
}
var lastArr = [];
var last1 = 0;
for(let n = 0; n < mainArr.length; n++){
    last1 = mainArr[n].length-1;
    lastArr.push(mainArr[n][last1]);
}

for(let p = 0; p < lastArr.length-1; p++){
    price+=((lastArr[p]*4)+2);
    if(lastArr[p]<lastArr[p+1]){
        price-=(lastArr[p]*2);
    }
    else{
        price-=(lastArr[p+1]*2);
    }
}
price+=((lastArr[lastArr.length-1])*4)+2;
console.log(price);