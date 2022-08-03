def dice_sum(dice: int, desired_sum: int):
    dice_sum_helper(dice, desired_sum, [])


def dice_sum_helper(dice: int, desired_sum: int, chosen: []):
    # if dice is 0
    #   in backtracking, accumulate all the work done by the previous calls
    if dice == 0:
        if desired_sum == 0:
            print(chosen)
    # else
    #   handle 1 die
    #   try all possible values (1 - 6)
    else:
        for i in range(1, 7):
            # choose i
            chosen.append(i)
            # explore what could follow that
            # by trying using one fewer dice
            # and finding possible values that, while they may add up to a lower sum down in the call stack
            # and may not add up to the desired sum
            # up in the call stacks, they may add up to the desired sum
            dice_sum_helper(dice - 1, desired_sum - i, chosen)
            # un-choose i
            # explored all possibilities of i, now undo the fact that i was chosen
            chosen.pop()


def dice_sum_helper_optimized(dice: int, desired_sum: int, chosen: []):
    if dice == 0:
        if desired_sum == 0:
            print(chosen)
    # else condition: we need at least 1 dice and at most 6 dices to produce desired sum
    elif dice * 1 <= desired_sum <= dice * 6:
        for i in range(1, 7):
            chosen.append(i)
            dice_sum_helper(dice - 1, desired_sum - i, chosen)
            chosen.pop()


if __name__ == '__main__':
    dice_sum(2, 7)
