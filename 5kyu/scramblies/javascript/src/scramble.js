/*
 * Scramblies
 * https://www.codewars.com/kata/55c04b4cc56a697bb0000048
 *
 * Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
 * match str2, otherwise returns false.
 * Notes:
 * -Only lower case letters will be used (a-z). No punctuation or digits will be included.
 * -Performance needs to be considered.
 * Examples
 * scramble('rkqodlw', 'world') ==> True
 * scramble('cedewaraaossoqqyt', 'codewars') ==> True
 * scramble('katas', 'steak') ==> False
 */


/*
 * return number of char occurrences in str
 */
function charCount(char, str) {
  return str.split(char).length - 1;
}

/*
 * return object where keys are small letters (a-z) and values are counts of these letters in the string passed in
 */
function charCounts(str) {
  return {
    "a": charCount("a", str),
    "b": charCount("b", str),
    "c": charCount("c", str),
    "d": charCount("d", str),
    "e": charCount("e", str),
    "f": charCount("f", str),
    "g": charCount("g", str),
    "h": charCount("h", str),
    "i": charCount("i", str),
    "j": charCount("j", str),
    "k": charCount("k", str),
    "l": charCount("l", str),
    "m": charCount("m", str),
    "n": charCount("n", str),
    "o": charCount("o", str),
    "p": charCount("p", str),
    "q": charCount("q", str),
    "r": charCount("r", str),
    "s": charCount("s", str),
    "t": charCount("t", str),
    "u": charCount("u", str),
    "v": charCount("v", str),
    "w": charCount("w", str),
    "x": charCount("x", str),
    "y": charCount("y", str),
    "z": charCount("z", str)
  }
}

/*
 * return true if a portion of str1 characters can be rearranged to match str2, otherwise returns false
 */
function scramble(str1, str2) {
  const map1 = charCounts(str1);
  const map2 = charCounts(str2);

  for (const char of Object.keys(map1)) {
    const count1 = map1[char];
    const count2 = map2[char];

    if (count1 < count2) {
      return false;
    }
  }
  return true
}

module.exports = { scramble };
