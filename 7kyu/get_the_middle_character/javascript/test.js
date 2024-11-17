const { getMiddle } = require("./src/get_middle");

test("7kyu Get the Middle Character", () => {
  expect(getMiddle("test")).toStrictEqual("es");
  expect(getMiddle("testing")).toStrictEqual("t");
  expect(getMiddle("middle")).toStrictEqual("dd");
  expect(getMiddle("A")).toStrictEqual("A");
});
