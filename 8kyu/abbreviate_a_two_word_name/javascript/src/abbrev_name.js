/*
 * Abbreviate a Two Word Name
 * https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
 *
 * Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
 * The output should be two capital letters with a dot separating them.
 * It should look like this:
 * Sam Harris => S.H
 * patrick feeney => P.F
 */
function abbrev_name(name){
  const words = name.split(" ");
  const first = words[0];
  const last = words[1];
  return `${first.charAt(0).toUpperCase()}.${last.charAt(0).toUpperCase()}`;
}

module.exports = { abbrevName: abbrev_name };
