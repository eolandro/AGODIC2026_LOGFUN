def combinaListas(L1, L2):

    if not L1 and not L2:
        return []

    if not L1 or not L2:
        match (L1, L2):

            case ([A, *F1], []):
                return [[A]] + combinaListas(F1, [])

            case ([], [B, *F2]):
                return [[B]] + combinaListas([], F2)

    match (L1, L2):

        case([A], [B]):
                    return [[A, B]]

        case ([A, *F1], [B, *F2]):
            return [[A, B]] + combinaListas(F1, F2)

R = combinaListas([1,2,3],["a","b","c"])
print(R)
# [1,"a",2,"b",3,"c"]

R = combinaListas([1],["a","b","c"])
print(R)
# [1,"a","b","c"]

R = combinaListas([1,2,3],["a"])
print(R)
# [1,"a",2,3]


R = combinaListas([1,2,3],[])
print(R)
# [1,2,3]


R = combinaListas([],["a","b","c"])
print(R)
# ["a","b","c"]