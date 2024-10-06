const { isIsogram } = require("./src/is_isogram");

test("7kyu Isograms", () => {
  expect(isIsogram("Dermatoglyphics")).toStrictEqual(true);
  expect(isIsogram("isogram")).toStrictEqual(true);
  expect(isIsogram("aba")).toStrictEqual(false); // same chars may not be adjacent
  expect(isIsogram("moOse")).toStrictEqual(false); // same chars may not be same case
  expect(isIsogram("isIsogram")).toStrictEqual(false);
  expect(isIsogram("")).toStrictEqual(true); // an empty string is a valid isogram
});
