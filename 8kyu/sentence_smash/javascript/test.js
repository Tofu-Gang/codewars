const { smash } = require("./src/smash");

test("8kyu Sentence Smash", () => {
  expect(smash(['hello', 'world', 'this', 'is', 'great'])).toStrictEqual('hello world this is great');
  expect(smash([])).toStrictEqual('');
  expect(smash(["hello"])).toStrictEqual("hello");
  expect(smash(["hello", "world"])).toStrictEqual("hello world");
  expect(smash(["hello", "amazing", "world"])).toStrictEqual("hello amazing world");
  expect(smash(["this", "is", "a", "really", "long", "sentence"]))
    .toStrictEqual("this is a really long sentence");
});
