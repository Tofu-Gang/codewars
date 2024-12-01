const { abbrevName } = require("./src/abbrev_name");

test("8kyu Abbreviate a Two Word Name", () => {
  expect(abbrevName("Sam Harris")).toStrictEqual("S.H");
  expect(abbrevName("patrick feeney")).toStrictEqual("P.F");
  expect(abbrevName("Patrick Feenan")).toStrictEqual("P.F");
  expect(abbrevName("Evan Cole")).toStrictEqual("E.C");
  expect(abbrevName("P Favuzzi")).toStrictEqual("P.F");
  expect(abbrevName("David Mendieta")).toStrictEqual("D.M");
});
