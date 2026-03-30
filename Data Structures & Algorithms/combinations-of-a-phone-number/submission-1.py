class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits:
            self.letterCombinationsHelper(digits, digitsToLetters, res, "", 0)

        return res

    def letterCombinationsHelper(self, digits, digitsToLetters, res, currString, i):
        if len(currString) == len(digits):
            res.append(currString)
            return

        for letter in digitsToLetters[digits[i]]:
            self.letterCombinationsHelper(digits, digitsToLetters, res, currString + letter, i + 1)