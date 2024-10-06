/*
 * Isograms
 * https://www.codewars.com/kata/54ba84be607a92aa900000f1
 *
 * An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
 * determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore
 * letter case.
 * Example: (Input --> Output)
 * "Dermatoglyphics" --> true
 * "aba" --> false
 * "moOse" --> false (ignore letter case)
 */


/*
 * return number of char occurrences in str
 */
function charCount(char, str) {
  return str.split(char).length - 1;
}

/*
 * return true if str is isogram (each letter is only once in it), false otherwise (case insensitive)
 */
function isIsogram(str){
  const lowercase = str.toLowerCase();

  for(let i = 0; i < lowercase.length; i++) {
    const char = lowercase.charAt(i);
    if (charCount(char, lowercase) !== 1) {
      return false;
    }
  }
  return true;
}

module.exports = { isIsogram };
