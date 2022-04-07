function isPalindrome(str) {
    
// const len = str.length;
for (let i = 0; i < len; i++) {
    if (str[i] !== str[(len - i)- 1]) {
        return 'Not a palindrome';
        }
    }
    return 'It is a palindrome';
}

const str =('oho');
// const str =('racecar');
// const str =('Dud');
// const str =('a x a')
const value = isPalindrome(str);

console.log(value);