function sum(n) {
    n= Math.floor(n)
    if (n < 1) return 0;    
    return n  + sum(n - 1); 
}
console.log(sum(5));
console.log(sum(2.5));
console.log(sum(-1));


function recursiveSigma(n) {
    let num= parseInt(n);
    if (isNaN(num)) {
        return null;
    }
    if (number <=0) {
        return 0;
    }
    return number + recursiveSigma(number -1);
}