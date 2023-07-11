/* 
Acronyms

Create a function that, given a string, returns the string’s acronym 
(first letter of each word capitalized). 

Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";



function acronymize(str) {
    var words = str.split(' ');
    var acronym = '';
    for (var i = 0; i < words.length; i++) {
        acronym += words[i][0].toUpperCase();
    }
    return acronym;
    }

    var result = acronymize(str1);
    // var result = acronymize(str2);
    // var result = acronymize(str3);
    console.log(result);



    function acronymize(str) {
        var words = str.trim().split(' ');
        var acronym = '';
        for (var i = 0; i < words.length; i++) {
            if (words[i] !== '') {
                acronym += words[i][0].toUpperCase();
            }
        }
        return acronym;
    }
    
    var result = acronymize(str4);
    console.log(result);