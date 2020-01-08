/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  n = x + "";
  k = n
    .split("")
    .reverse()
    .join("");

  if (n == k) {
    return true;
  }
  return false;
};
