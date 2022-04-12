// let str1 = "";

// let str1WordArr = str1.split(" ");

// let reverseWord=[];

// for(let i=(str1WordArr.length)-1;i>=0;i--)
// {
//     reverseWord.push(str1WordArr[i]);
// }
// console.log(reverseWord.join(" "));

// var str = 'Welcome to JavaScript'
// function reverseByWord(s){
//   return s.split(" ").reverse().join(" ");
// }

// reverseByWord(str)

// function reverseByWord(s){
//     return s.split(" ").reverse().join(" ");
// }

// function reverseArray(str){
//     var arr = [];
// var newstr = reverseWord(str);

// for(var i=0; i<str.length-1; i++){
//     arr[i]= reverseWord(str);

//     }
// }
// function reverseWord(str){
//     var newstr = "";
//     for(var i=str.length-1; i>=0;i--){
//         newstr += str[i];

//     } return newstr;
// }
// console.log(reverseByWord(str1));

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

function reverseInPlace(str) {
var words = [];
words = str.match(/\S+/g);
var result = "";
for (var i = 0; i < words.length; i++) {
    result += words[i].split("").reverse().join("") + " ";
}
result = result.substring(0, result.length - 1);
return result;
}
console.log(reverseInPlace(str1));
console.log(reverseInPlace(str2));
console.log(reverseInPlace(str3));
