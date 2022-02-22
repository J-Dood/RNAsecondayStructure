# Jordan Dood and Braeden Sopp
# 2/19/2022
# This code determines the secondary structure of a given ACGU RNA sequence.
# It then returns the number of paired bases in teh sequence, as a score.



# Imports
import numpy as np



# Functions
# Read input and return valid AGUC sequences in lower case form
def read_input():
    flag = True
    while (flag):
        seq = input("Enter a sequence of A, G, C, and U's: ").strip().lower()
        if (seq.count('a') + seq.count('g') + seq.count('c') + seq.count('u')) == len(seq):
            flag = False
        else:
            print("Hmm, that sequence had an issue, try again!")

    return seq


# Takes to chars as input and returns true if they are a valid base pairing
def base_pair(char1, char2):
    if char1 == 'a':
        if char2 == 'u':
            return True
        else:
            return False
    elif char1 =='u':
        if char2 == 'a':
            return True
        else:
            return False
    elif char1 =='g':
        if char2 == 'c':
            return True
        else:
            return False
    elif char1 =='c':
        if char2 == 'g':
            return True
        else:
            return False
    else:
        print("Error: Unknown char")
        return False


# This is a wrapper function for the recursive algorithm, to contain the memoization
def wrapper(sequence):
    size = len(sequence)
    memo_array = np.zeros((size, size))
    # Call to function
    recurse(sequence, memo_array, 0, size-1)
    score = memo_array[0, size-1]
    return score


# This function handles the recursion
def recurse(sequence, memo_array, i, j):
    if i > j-4:
        opt = 0
    elif memo_array[i, j] != 0:
        opt = memo_array[i, j]
    else:
        opt = recurse(sequence, memo_array, i, j-1)
        for k in range(i, j):
            if base_pair(sequence[k], sequence[j]):
                result_pair = 1 + recurse(sequence, memo_array, i, k-1) + recurse(sequence, memo_array, k+1, j-1)
                if result_pair > opt:
                    opt = result_pair
    memo_array[i, j] = opt
    return opt


# Main function
def main():
    sequence = read_input()
    #sequence = "ccccaaaagggg" # TEST STRING known value of: 4
    score = wrapper(sequence)
    print("The score is: " + str(score))


# Runs the main function
main()

