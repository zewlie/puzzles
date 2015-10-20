# Puzzle One
# ===========

# Merge two sorted lists.
# Without sort, ensure the new list is also sorted.

def mason_merge(list1, list2):
    """ Finally works!

    Takes any two sorted lists of ints:
    - of 1 or more items
    - with or without duplicate items

    ...and outputs a merged list that is also sorted.

    >>> a = [1]
    >>> b = [2, 5, 8, 300]
    >>> mason_merge(a, b)
    [1, 2, 5, 8, 300]

    >>> c = [1, 3, 8, 300]
    >>> d = [2, 5, 8, 300]
    >>> mason_merge(c, d)
    [1, 2, 3, 5, 8, 8, 300, 300]

    >>> e = [-4, -1, 0]
    >>> f = [2, 5, 8, 300]
    >>> mason_merge(e, f)
    [-4, -1, 0, 2, 5, 8, 300]


    >>> g = [1, 500]
    >>> h = [1, 5, 8, 300]
    >>> mason_merge(g, h)
    [1, 1, 5, 8, 300, 500]

    """
    a = 0
    b = 0
    last_a = len(list1) - 1
    last_b = len(list2) - 1

    new_list = []
    finish = False

    while finish is False:

# First, check if at least one index is on its last index.

        # If we're on the last index of one of our lists,
        # AND the value of the current index for the OTHER list
        # is equal to OR higher than the value of that last index,
        # we can just append with that last value and
        # then extend with the remainder of the other list.

        # If the value of the current index for the OTHER list
        # is lower than the value for our last index,
        # we'll have to skip down and append/increment, append/increment,
        # until that's no longer true.

        if b == last_b and a <= last_a and list1[a] >= list2[b]:
            new_list.append(list2[b])
            new_list.extend(list1[a:])
            finish = True

        elif a == last_a and b <= last_b and list2[b] >= list1[a]:
            new_list.append(list1[a])
            new_list.extend(list2[b:])
            finish = True

# If we get past this point, we'll be looping through again!

        elif list1[a] <= list2[b]:
            new_list.append(list1[a])
            a += 1

        elif list1[a] >= list2[b]:
            new_list.append(list2[b])
            b += 1

    return new_list


# Puzzle two
# ===========
# Create a homemade split function.
# No split() or regular expressions.
# Should be able to split on any char, word, etc.

# mason_splits('input string', 'split on this')


def mason_splits(unsplit, split_on):
    """ Homemade split().

    >>> mason_splits("How about we split this up?", " ")
    ['How', 'about', 'we', 'split', 'this', 'up?']

    >>> mason_splits("this and that and that and also that!", "that")
    ['this and ', ' and ', ' and also ', '!']

    """
    split_list = []
    chunk_size = len(split_on)
    idx_after_last_split = 0

    for idx, char in enumerate(unsplit):
        # These two variables are for improved readability
        # There'd be a couple less lines without them, but more comments.
        next_chunk = unsplit[idx:(idx + chunk_size)]
        content_between_splits = unsplit[idx_after_last_split:idx]

        if next_chunk == split_on:
            split_list.append(content_between_splits)
            idx_after_last_split = idx + chunk_size

    # Our loop will miss the last slice, so we add it here.
    split_list.append(unsplit[idx_after_last_split:])

    return split_list


# old version below - works, but it's unnecessarily long & complicated
# (relies on converting input strings into lists... I know... silly Mason)

# def mason_splits(split_this, on_this):
#     split_this_list = []
#     on_this_list = []
#     make_this_list = []

#     chunk_size = len(on_this)
#     start_from = 0
#     join_on = ""

#     for char in on_this:
#         on_this_list.append(char)
#     for char in split_this:
#         split_this_list.append(char)

#     for idx, char in enumerate(split_this_list):

#         if split_this_list[idx:idx + chunk_size] == on_this_list:
#             make_this_list.append(join_on.join(split_this_list[start_from:idx]))
#             start_from = idx + chunk_size

#     make_this_list.append(join_on.join(split_this_list[start_from:]))

#     return make_this_list


# Puzzle three
# =============

# 8 . . . . . . . .
# 7 . K . . . . . .
# 6 . . . . . . . .
# 5 . . . Q . . . .
# 4 . . . . . . . .
# 3 . . . . . . . .
# 2 . . . . . . . .
# 1 . . . . . . . .
#   A B C D E F G H

# The above represents a chessboard.
# Write a function to determine if the Q(ueen) can attack the K(ing).
# The Queen can move horizontally/vertically/diagnally in any direction,
# as far as needed.


def mason_kills_the_king(K, Q):
    """
    >>> mason_kills_the_king("D6", "H6")
    True

    >>> mason_kills_the_king("B7", "D5")
    True

    >>> mason_kills_the_king("A1", "H8")
    True

    >>> mason_kills_the_king("A8", "H1")
    True

    >>> mason_kills_the_king("D6", "H7")
    False

    >>> mason_kills_the_king("E6", "F4")
    False

    """
    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    y = ['1', '2', '3', '4', '5', '6', '7', '8']

    if K[0] == Q[0]:
        return True
    elif K[1] == Q[1]:
        return True
    elif abs(x.index(K[0]) - x.index(Q[0])) == abs(y.index(K[1]) - y.index(Q[1])):
        return True
    else:
        return False


# Puzzle four
# ============
# Check if a scrambled up string could be rearranged into a palindrome
# (word read the same from front to back and vis-versa).
# Do not need to check if the palindrome is a real word.

# All but one character must occur a number of times that is even.


def masondrome(word):
    """Check if a scrambled up string could be rearranged into a palindrome
    (word read the same from front to back and vis-versa).

    >>> masondrome("racecar")
    True
    >>> masondrome("springtime")
    False

    """
    char_count_dict = {}
    odd_char_count = 0

# Build out a dictionary with characters as keys and character-counts as values.

    for i in word:
        if i not in char_count_dict:
            char_count_dict[i] = 0
        char_count_dict[i] += 1

# Loop through dictionary, checking for odd character counts.
# No more than one may be present for the string to be a palindrome.

    for i in char_count_dict:
        if char_count_dict[i] % 2 != 0:
            odd_char_count += 1

    if odd_char_count > 1:
        return False
    else:
        return True















