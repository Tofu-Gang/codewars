const { removeChar } = require("./src/remove_char");

test("8kyu Remove First and Last Character", () => {
  expect(removeChar('eloquent')).toStrictEqual('loquen');
  expect(removeChar('country')).toStrictEqual('ountr');
  expect(removeChar('person')).toStrictEqual('erso');
  expect(removeChar('place')).toStrictEqual('lac');
  expect(removeChar('ooopsss')).toStrictEqual('oopss');
});
