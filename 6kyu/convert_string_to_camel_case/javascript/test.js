const { toCamelCase } = require("./src/to_camel_case");

test("6kyu Break camelCase", () => {
  expect(toCamelCase("")).toStrictEqual("");
  expect(toCamelCase("the_stealth_warrior")).toStrictEqual("theStealthWarrior");
  expect(toCamelCase("the-stealth-warrior")).toStrictEqual("theStealthWarrior");
  expect(toCamelCase("The_Stealth_Warrior")).toStrictEqual("TheStealthWarrior");
  expect(toCamelCase("The-Stealth-Warrior")).toStrictEqual("TheStealthWarrior");
  expect(toCamelCase("The_Stealth-Warrior")).toStrictEqual("TheStealthWarrior");
  expect(toCamelCase("A-B-C")).toStrictEqual("ABC");
});
