# https://www.algoexpert.io/questions/Validate%20Subsequence
# O(N) T - O(1) S

def isValidSubsequence(array, sequence):
    for number in array:
        if sequence and number == sequence[0]:
            sequence.pop(0)

    return sequence == []
