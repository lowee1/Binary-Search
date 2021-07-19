def iterative_binary_search(search_list: list, target, offset=0):
    while True:
        midpoint = len(search_list) // 2
        midpoint_value = search_list[midpoint]
        if midpoint_value > target:
            (search_list, target, offset) = (search_list[0:midpoint], target, offset)
        elif midpoint_value < target:
            (search_list, target, offset) = (
                search_list[midpoint + 1 :],
                target,
                offset + midpoint + 1,
            )
        elif midpoint_value == target:
            return midpoint + offset


if __name__ == "__main__":
    print(iterative_binary_search(list(range(1000000000)), 0))
