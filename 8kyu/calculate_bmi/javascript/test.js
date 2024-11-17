const { bmi, Values } = require("./src/bmi");

test("8kyu Calculate BMI", () => {
  expect(bmi(50, 1.80)).toStrictEqual(Values.Underweight);
  expect(bmi(80, 1.80)).toStrictEqual(Values.Normal);
  expect(bmi(90, 1.80)).toStrictEqual(Values.Overweight);
  expect(bmi(100, 1.80)).toStrictEqual(Values.Obese);
});
