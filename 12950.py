'''
문제 : 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은행, 같은 열의 값을 서로 더한 결과가 된다. 
2개의 행렬 arr1과 arr2를 입력받아 행렬 덧셈의 결과를 반환하는 함수를 만든다. 
'''

# 행렬은 2차원 배열로 구성되어 있는데 전체 배열의 길이가 행의 크기이고, 배열 원소의 길이가 열의 크기가 되는 구조
# 2중 반복을 이용하면 행렬의 덧셈을 구할 수 있다. 

def solution(arr1, arr2):
    for j in range(len(arr1)):
        for k in range(len(arr1[j])):
            arr1[j][k] = arr1[j][k] + arr2[j][k]
    return arr1


