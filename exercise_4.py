import itertools

# string of example
input_s = "DATAMININGSAPIENZA"
l_input = list(input_s)

# check if a sting (in the form of a list) is palindrome


def palindrome_list(lis):

    rev = lis[::-1]
    if lis == rev:
        return True
    else:
        return False

# creates all the possible combination (with the
# specified length) of a list of characters and
# appends them to a list if they are palindrome.
# It returns the maximum length of an element
# that can be found in that list


def combinations(lis, min_len, max_len):
    poss = []
    for i in range(min_len, max_len):
        for subset in itertools.combinations(lis, i):
            if palindrome_list(list(subset)):
                poss.append(''.join(subset))

    longest = max(poss, key=len)
    # print([word for word in poss if len(word) == len(longest)])
    return len(longest)


print(combinations(l_input, 1, len(l_input)))


