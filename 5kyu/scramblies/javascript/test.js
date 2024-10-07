const { scramble } = require("./src/scramble");

test("5kyu Scramblies", () => {
  expect(scramble('rkqodlw', 'world')).toStrictEqual(true );
  expect(scramble('cedewaraaossoqqyt', 'codewars')).toStrictEqual(true );
  expect(scramble('katas', 'steak')).toStrictEqual(false);
  expect(scramble('scriptjavx', 'javascript')).toStrictEqual(false);
  expect(scramble('scriptingjava', 'javascript')).toStrictEqual(true );
  expect(scramble('scriptsjava', 'javascripts')).toStrictEqual(true );
  expect(scramble('javscripts', 'javascript')).toStrictEqual(false);
  expect(scramble('jscripts', 'javascript')).toStrictEqual(false);
  expect(scramble('aabbcamaomsccdd', 'commas')).toStrictEqual(true );
  expect(scramble('commas', 'commas')).toStrictEqual(true );
  expect(scramble('sammoc', 'commas')).toStrictEqual(true )
  let s1 = "abcdefghijklmnopqrstuvwxyz".repeat(10_000);
  let s2 = "zyxcba".repeat(9_000);
  expect(scramble(s1, s2)).toStrictEqual(true);
});
