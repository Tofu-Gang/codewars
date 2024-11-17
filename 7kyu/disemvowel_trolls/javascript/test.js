const { disemvowel } = require("./src/disemvowel");

test("7kyu Disemvowel Trolls", () => {
  expect(disemvowel("This website is for losers LOL!")).toStrictEqual("Ths wbst s fr lsrs LL!");
  expect(disemvowel("No offense but,\nYour writing is among the worst I've ever read")).toStrictEqual("N ffns bt,\nYr wrtng s mng th wrst 'v vr rd");
  expect(disemvowel("What are you, a communist?")).toStrictEqual("Wht r y,  cmmnst?");
});
