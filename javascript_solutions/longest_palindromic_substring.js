// Given a string s, return the longest palindromic substring in s.
 
/**
 * @param {string} s
 * @return {string}
 */
// O(n^3)
var longestPalindrome1 = function (s) {
  let longestPalindrome = 0;
  let longestPalindromeStartIndex = 0;
  for (let l = 0; l < s.length; l++) {
    for (let r = s.length - 1; r >= l; r -= 1) {
      let isPalindrome = true;
      if (longestPalindrome > r - l + 1) {
        isPalindrome = false;
        break;
      }
      for (k = 0; k < r - l; k++) {
        if (s[l + k] != s[r - k]) {
          isPalindrome = false;
          break;
        }
      }
      if (isPalindrome) {
        longestPalindrome = r - l + 1;
        longestPalindromeStartIndex = l;
      }
    }
  }
  return s.substring(
    longestPalindromeStartIndex,
    longestPalindromeStartIndex + longestPalindrome
  );
};

// O(n^2)
var longestPalindrome2 = function (s) {
  const length = s.length;
  const tab = [];
  let longestPalindromeStr = s[0];

  for (let i = 0; i < length; i++) {
    tab[i] = [];
    tab[i][i] = 1;

    if (i + 1 <= length && s[i] == s[i + 1]) {
      tab[i][i + 1] = 1;
      longestPalindromeStr = s.substring(i, i + 2);
    } else {
      tab[i][i + 1] = 0;
    }
  }
  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length - 2 - i; j++) {
      if (s[j] == s[j + i + 2] && tab[j + 1][j + i + 1] === 1) {
        tab[j][j + 2 + i] = 1;
        if (i + 3 > longestPalindromeStr.length) {
          longestPalindromeStr = s.substring(j, j + i + 3);
        }
      } else {
        tab[j][j + 2 + i] = 0;
      }
    }
  }
  return longestPalindromeStr;
};
