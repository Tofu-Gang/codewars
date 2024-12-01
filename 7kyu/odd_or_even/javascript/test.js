const { Values, oddOrEven } = require("./src/odd_or_even");

test("7kyu Odd or Even?", () => {
  expect(oddOrEven([0])).toStrictEqual(Values.Even);
  expect(oddOrEven([1])).toStrictEqual(Values.Odd);
  expect(oddOrEven([])).toStrictEqual(Values.Even);
  expect(oddOrEven([0, 1, 4])).toStrictEqual(Values.Odd);
  expect(oddOrEven([0, 1, 5])).toStrictEqual(Values.Even);
  expect(oddOrEven([0, -1, -5])).toStrictEqual(Values.Even);
  expect(oddOrEven([0, 1, 3])).toStrictEqual(Values.Even);
  expect(oddOrEven([0, -1, -3])).toStrictEqual(Values.Even);
  expect(oddOrEven([1023, 1, 2])).toStrictEqual(Values.Even);
  expect(oddOrEven([-1023, 1, -2])).toStrictEqual(Values.Even);
  expect(oddOrEven([0, 1, 2])).toStrictEqual(Values.Odd);
  expect(oddOrEven([0, -1, 2])).toStrictEqual(Values.Odd);
  expect(oddOrEven([0, 1, 4])).toStrictEqual(Values.Odd);
  expect(oddOrEven([0, 1, -4])).toStrictEqual(Values.Odd);
  expect(oddOrEven([1023, 1, 3])).toStrictEqual(Values.Odd);
  expect(oddOrEven([-1023, -1, 3])).toStrictEqual(Values.Odd);
});
