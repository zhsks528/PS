/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  var DIGIT_VALUES = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
  };

  var result = 0;
  var input = s.split("");

  for (var i = 0; i < input.length; i++) {
    var currentLetter = DIGIT_VALUES[input[i]];
    var nextLetter = DIGIT_VALUES[input[i + 1]];
    if (currentLetter === undefined) {
      return "null";
    } else {
      if (currentLetter < nextLetter) {
        result += nextLetter - currentLetter;
        i++;
      } else {
        result += currentLetter;
      }
    }
  }

  return result;
};
