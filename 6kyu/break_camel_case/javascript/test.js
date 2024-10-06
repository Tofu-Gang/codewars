const { solution } = require("./src/solution");

test("6kyu Break camelCase", () => {
  expect(solution("")).toStrictEqual("");
  expect(solution("camelCasing")).toStrictEqual("camel Casing");
  expect(solution("camelCasingTest")).toStrictEqual("camel Casing Test");
});
