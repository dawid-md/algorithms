def tsp(cities, paths, dist):
    citiesperms = permutations(cities)
    for perm in citiesperms:
        distance = 0
        for p in range(len(perm)-1):
            distance += paths[p][p+1]
        if distance < dist:
            return True
    return False

# don't touch below this line

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res






###def verify_tsp(paths, dist, actual_path):
    # for path in actual_path:
    #     print(actual_path)
    #     total_dist = 0
    #     for j in range(1, path):
    #         total_dist += paths[path[j-1]][path[j]]
    #     if total_dist < dist:
    #         return True
    # return False