def letterCombinations(digits):
    keys = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    tmp = []
    results = []
    for n in digits:
        for letter in keys[n]:
            if len(results) == 0:
                tmp.append(letter)
            else:
                for r in results:
                    tmp.append(r+letter)
        results, tmp = tmp, []
    return results