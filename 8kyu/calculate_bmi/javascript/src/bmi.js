/*
 * Calculate BMI
 * https://www.codewars.com/kata/57a429e253ba3381850000fb
 *
 * Write function bmi that calculates body mass index (bmi = weight / height2).
 * if bmi <= 18.5 return "Underweight"
 * if bmi <= 25.0 return "Normal"
 * if bmi <= 30.0 return "Overweight"
 * if bmi > 30 return "Obese"
 */

const Values = {
  Underweight: "Underweight",
  Normal: "Normal",
  Overweight: "Overweight",
  Obese: "Obese",
};

/*
 * Write function bmi that calculates body mass index (bmi = weight / height2).
 * if bmi <= 18.5 return "Underweight"
 * if bmi <= 25.0 return "Normal"
 * if bmi <= 30.0 return "Overweight"
 * if bmi > 30 return "Obese"
 */
function bmi(weight, height) {
  const bmiValue = weight / (height * height);
  if (bmiValue <= 18.5) return Values.Underweight;
  if (bmiValue <= 25.0) return Values.Normal;
  if (bmiValue <= 30.0) return Values.Overweight;
  if (bmiValue > 30) return Values.Obese;
}

module.exports = { Values, bmi };
