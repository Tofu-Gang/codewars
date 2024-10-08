const { areYouPlayingBanjo } = require("./src/are_you_playing_banjo");

test("8kyu Are You Playing Banjo?", () => {
  expect(areYouPlayingBanjo("Adam")).toStrictEqual("Adam does not play banjo");
  expect(areYouPlayingBanjo("Paul")).toStrictEqual("Paul does not play banjo");
  expect(areYouPlayingBanjo("Ringo")).toStrictEqual("Ringo plays banjo");
  expect(areYouPlayingBanjo("bravo")).toStrictEqual("bravo does not play banjo");
  expect(areYouPlayingBanjo("rolf")).toStrictEqual("rolf plays banjo");
});
