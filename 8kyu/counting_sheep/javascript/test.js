const { countSheeps } = require("./src/count_sheeps");

test("8kyu Counting sheep...", () => {
  expect(countSheeps([])).toStrictEqual(0);
  expect(countSheeps([undefined])).toStrictEqual(0);
  expect(countSheeps([null])).toStrictEqual(0);
  expect(countSheeps([false])).toStrictEqual(0);
  expect(countSheeps([true])).toStrictEqual(1);
  expect(countSheeps([undefined, null, false, true])).toStrictEqual(1);
  expect(countSheeps([undefined, null, false, true, true, false, null, undefined])).toStrictEqual(2);
  expect(countSheeps([
    true, true, true, false,
    true, true, true, true,
    true, false, true, false,
    true, false, false, true,
    true, true, true, true,
    false, false, true, true])).toStrictEqual(17);
});
