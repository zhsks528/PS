/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = s => {
  if (
    s ===
    s
      .split("")
      .reverse()
      .join("")
  )
    return s;
  let charArray = [],
    countArray = [];

  let currentWord = s[0];
  let count = 1;
  let sLength = s.length + 1;

  //build array of repeating characters
  for (let i = 1; i < sLength; i++) {
    if (s[i] === s[i - 1]) {
      //simply advance by incrementing count and character to currentWord
      count++;
      currentWord += s[i];
    } else {
      //different character found
      //save character & count
      countArray.push(count);
      charArray.push(currentWord);

      //reset currentWord, count
      currentWord = s[i];
      count = 1;
    }
  }

  let head = 0;
  let tail = 0;
  let maxWord = "";
  let charLength = charArray.length;
  //step through character array to check for characters surrounding repeated characters
  for (let k = 0; k < charLength; k++) {
    currentWord = charArray[k];
    tail = head + countArray[k] - 1;
    let steps = sLength - countArray[k]; //num of steps we need to take surrounding repeated characters
    for (let l = 1; l < steps; l++) {
      if (s[head - l] === s[tail + l]) {
        currentWord = s[head - l] + currentWord + s[tail + l];
      } else {
        //check currentWord against maxWord
        maxWord = maxWord.length < currentWord.length ? currentWord : maxWord;
        head = tail + 1;
        break;
      }
    }
  }
  return maxWord;
};
