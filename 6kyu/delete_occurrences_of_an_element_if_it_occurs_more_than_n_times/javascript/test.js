const { deleteNth } = require("./src/delete_nth");

test("6kyu Delete occurrences of an element if it occurs more than n times", () => {
  expect(deleteNth([20,37,20,21], 1)).toStrictEqual([20,37,21]);
  expect(deleteNth([1,1,3,3,7,2,2,2,2], 3)).toStrictEqual([1, 1, 3, 3, 7, 2, 2, 2]);
  expect(deleteNth([12,39,19,39,39,19,12], 1)).toStrictEqual([12, 39, 19]);
});
