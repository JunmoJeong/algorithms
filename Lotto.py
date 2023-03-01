from pprint import pprint

eunsun_lotto=[
    [3,23,32,39,41,44],
    [6,8,13,22,26,31],
    [8,12,18,28,29,35],
    [20,29,31,32,42,45],
    [1,6,20,23,25,33]
]

junmo_lotto=[
    [16,22,31,38,39,40],
    [2,3,7,24,33,37],
    [10,13,20,21,22,32],
    [4,5,18,28,32,40],
    [17,27,28,32,38,40]
]
print("")
print("====== Eunsun Lotto ======")
print("")
print(*eunsun_lotto, sep='\n\n')
print("")
print("====== Junmo Lotto ======")
print("")
print(*junmo_lotto, sep='\n\n')
print("")