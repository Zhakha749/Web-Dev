let john = {
  name: "John",
  sayHi: function() {
    alert("Hi buddy!");
  }
};

john.sayHi(); // Hi buddy!



// -3 divides by 1 with 3 zeroes
1e-3 === 1 / 1000; // 0.001

// -6 divides by 1 with 6 zeroes
1.23e-6 === 1.23 / 1000000; // 0.00000123

// an example with a bigger number
1234e-2 === 1234 / 100; // 12.34, decimal point moves 2 times



let a = 0b11111111; // binary form of 255
let b = 0o377; // octal form of 255

alert( a == b ); // true, the same number 255 at both sides



alert( isFinite("15") ); // true
alert( isFinite("str") ); // false, because a special value: NaN
alert( isFinite(Infinity) ); // false, because a special value: Infinity


alert( Number.isNaN(NaN) ); // true
alert( Number.isNaN("str" / 2) ); // true

// Note the difference:
alert( Number.isNaN("str") ); // false, because "str" belongs to the string type, not the number type
alert( isNaN("str") ); // true, because isNaN converts string "str" into a number and gets NaN as a result of this conversion



alert( Number.isFinite(123) ); // true
alert( Number.isFinite(Infinity) ); // false
alert( Number.isFinite(2 / 0) ); // false

// Note the difference:
alert( Number.isFinite("123") ); // false, because "123" belongs to the string type, not the number type
alert( isFinite("123") ); // true, because isFinite converts string "123" into a number 123


let arr = ["I", "study", "JavaScript"];

// from index 2
// delete 0
// then insert "complex" and "language"
arr.splice(2, 0, "complex", "language");

alert( arr ); // "I", "study", "complex", "language", "JavaScript"



let Arr = ["t", "e", "s", "t"];

alert( Arr.slice(1, 3) ); // e,s (copy from 1 to 3)

alert( Arr.slice(-2) ); // s,t (copy from -2 till the end)



let a_rr = [1, 2];

// create an array from: arr and [3,4]
alert( a_rr.concat([3, 4]) ); // 1,2,3,4

// create an array from: arr and [3,4] and [5,6]
alert( a_rr.concat([3, 4], [5, 6]) ); // 1,2,3,4,5,6

// create an array from: arr and [3,4], then add values 5 and 6
alert( a_rr.concat([3, 4], 5, 6) ); // 1,2,3,4,5,6



let _arr = [1, 0, false];

alert( _arr.indexOf(0) ); // 1
alert( _arr.indexOf(false) ); // 2
alert( _arr.indexOf(null) ); // -1

alert( _arr.includes(1) ); // true



let str = `Hello`;

// the first character
alert( str[0] ); // H
alert( str.at(0) ); // H

// the last character
alert( str[str.length - 1] ); // o
alert( str.at(-1) );



let _str = 'Widget with id';

alert( _str.indexOf('Widget') ); // 0, because 'Widget' is found at the beginning
alert( _str.indexOf('widget') ); // -1, not found, the search is case-sensitive

alert( _str.indexOf("id") ); // 1, "id" is found at the position 1 (..idget with id)








