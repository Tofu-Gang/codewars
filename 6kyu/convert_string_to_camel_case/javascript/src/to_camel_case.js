/*
 * Convert string to camel case
 * https://www.codewars.com/kata/517abf86da9663f1d2000003
 *
 * Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
 * within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
 * often referred to as Pascal case). The next words should be always capitalized.
 *
 * Examples
 * "the-stealth-warrior" gets converted to "theStealthWarrior"
 * "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
 * "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
 */

/*
 * Make first letter of the word passed in upper case.
 */
function capitalize(word) {
  return `${word.charAt(0).toUpperCase()}${word.slice(1)}`;
}

/*
 * Make first letter of the word passed in lower case.
 */
function decapitalize(word) {
  return `${word.charAt(0).toLowerCase()}${word.slice(1)}`;
}

/*
 * Complete the method/function so that it converts dash/underscore delimited words into camel casing.
 * The first word within the output should be capitalized only if the original word was capitalized
 * (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always
 * capitalized.
 */
function toCamelCase(str){
  const firstChar = str.charAt(0);
  const capitalizeFirst = firstChar === firstChar.toUpperCase();
  const result = str.split(/[-_]/).map((word) => capitalize(word)).join("");
  if (capitalizeFirst) {
    return result;
  } else {
    return decapitalize(result);
  }
}

module.exports = { toCamelCase };
