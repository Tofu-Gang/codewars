const { accum } = require("./src/accum");

test("7kyu Mumbling", () => {
  expect(accum("abcd")).toStrictEqual("A-Bb-Ccc-Dddd");
  expect(accum("RqaEzty")).toStrictEqual("R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy");
  expect(accum("cwAt")).toStrictEqual("C-Ww-Aaa-Tttt");
  expect(accum("ZpglnRxqenU")).toStrictEqual("Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu");
  expect(accum("NyffsGeyylB")).toStrictEqual("N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb");
  expect(accum("MjtkuBovqrU")).toStrictEqual("M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu");
  expect(accum("EvidjUnokmM")).toStrictEqual("E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm");
  expect(accum("HbideVbxncC")).toStrictEqual("H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc");
});
