/*
 * Break camelCase
 * https://www.codewars.com/kata/5208f99aee097e6552000148
 *
 * Complete the solution so that the function will break up camel casing, using a space between words.
 * Example
 * "camelCasing"  =>  "camel Casing"
 * "identifier"   =>  "identifier"
 * ""             =>  ""
 */


/*
 * Return true if the string passed in is lowercase, false otherwise.
 */
function isLowerCase(text) {
  return text === text.toLowerCase() && text !== text.toUpperCase();
}

/*
 * Break up camel casing, using a space between words. Return the result.
 */
function solution(text) {
  let result = "";
  for (let i = 0; i < text.length - 1; i++) {
    // read character and add it to the output
    const character1 = text.charAt(i);
    result += character1;
    const character2 = text.charAt(i + 1);
    if (isLowerCase(character1) && !isLowerCase(character2)) {
      // if this character is lowercase and the next one is not, insert space to the output
      result += " ";
    }
  }
  // don't forget the last character which we did not process yet
  result += text.charAt(text.length - 1);
  return result;
}

module.exports = { solution };
