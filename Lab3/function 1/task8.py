def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 7, 2, 0, 4, 5, 0]))