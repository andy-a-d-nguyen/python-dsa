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
            dice_sum_helper(dice - 1, desired_sum - i, chosen)
            # un-choose i
            # explored all possibilities of i, now undo the fact that i was chosen
            chosen.pop()


if __name__ == '__main__':
    dice_sum(2, 7)
