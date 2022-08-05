"""
Write a function permute that accepts a vector of strings as a
parameter and outputs all possible rearrangements of the strings
in that vector. The arrangements may be output in any order
"""
from typing import List, NoReturn, Set


def permute(string: List[str]) -> NoReturn:
    permute_helper(string, [])


def permute_helper(string: List[str], chosen: List[str]) -> NoReturn:
    if len(string) == 0:
        print(chosen)
    else:
        # for each choice:
        for i, el in enumerate(string):
            # choose
            chosen.append(el)
            string.pop(i)

            # explore
            permute_helper(string, chosen)

            # un-choose
            chosen.pop()
            string.insert(i, el)


def permute_optimized(string: List[str]) -> NoReturn:
    permute_optimized_helper(string, [], set())


def permute_optimized_helper(string: List[str], chosen: List[str], printed: Set[str]) -> NoReturn:
    if len(string) == 0:
        str_chosen = ' '.join(chosen)
        if str_chosen not in printed:
            print(chosen)
            printed.add(str_chosen)
    else:
        # for each choice:
        for i, el in enumerate(string):
            # choose
            chosen.append(el)
            string.pop(i)

            # explore
            permute_optimized_helper(string, chosen, printed)

            # un-choose
            chosen.pop()
            string.insert(i, el)


if __name__ == '__main__':
    # permute(['a', 'b', 'c', 'd'])
    # permute(['a', 'b', 'b', 'a', 'd'])
    permute_optimized(['a', 'b', 'b', 'a', 'd'])
