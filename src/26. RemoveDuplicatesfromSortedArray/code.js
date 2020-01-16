/* 1번째 방법 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  nums.splice(0, nums.length, ...new Set(nums));
};

/* 2번째 방법 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let real = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== nums[real]) {
      real++;
      nums[real] = nums[i];
    }
  }
  return real + 1;
};
