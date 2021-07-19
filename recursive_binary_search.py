def recursive_binary_search(search_list: list, target, offset=0):
    midpoint = len(search_list) // 2
    midpoint_value = search_list[midpoint]
    if midpoint_value == target:
        return midpoint + offset

    if midpoint_value > target:
        return recursive_binary_search(search_list[0:midpoint], target, offset)

    if midpoint_value < target:
        return recursive_binary_search(
            search_list[midpoint + 1 :], target, offset + midpoint + 1
        )


if __name__ == "__main__":
    print(recursive_binary_search(list(range(1000000000)), 0))
