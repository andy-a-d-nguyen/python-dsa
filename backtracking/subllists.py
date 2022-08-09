"""
Write a function sub_lists that finds every possible sub-list of a given vector. A sub-list of a vector V contains
>= 0 of V's elements
- You can print the sub-lists out in any order, one per line
"""
from typing import List


def sub_lists(list: List) -> None:
    sub_lists_helper(list, [])


"""
This problem is different from permutation in that we want to explore possibilities with an item and possibilities 
without and item instead of finding combinations of an item and the remaining items
"""


def sub_lists_helper(list: List, chosen: List) -> None:
    if len(list) == 0:
        # print what was accumulated
        print(chosen)
    else:
        item = list.pop(0)

        # choose/explore (without item)
        sub_lists_helper(list, chosen)

        # choose/explore (with item)
        chosen.append(item)
        sub_lists_helper(list, chosen)

        # un-choose
        list.insert(0, item)
        chosen.pop()


if __name__ == '__main__':
    sub_lists(['Jane', 'Bob', 'Matt', 'Sara'])
