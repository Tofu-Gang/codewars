/*
 * Get the Middle Character
 * https://www.codewars.com/kata/56747fd5cb988479af000028
 *
 * You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
 * - If the string's length is odd, return the middle character.
 * - If the string's length is even, return the middle 2 characters.
 * Examples:
 * "test" --> "es"
 * "testing" --> "t"
 * "middle" --> "dd"
 * "A" --> "A"
 */

/*
 * Return the middle character of the word passed in.
 * If the word's length is odd, return the middle character.
 * If the word's length is even, return the middle 2 characters.
 */
function getMiddle(s) {
  const length = s.length;
  return length % 2 === 0 ? `${s.charAt((length / 2) - 1)}${s.charAt(length / 2)}` : s.charAt(Math.floor(length / 2));
}

module.exports = { getMiddle };
