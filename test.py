def solution(arr):
    left, right = 0, len(arr) - 1
    idx = 0
    answer = [0 for _ in range(len(arr))]
    while left <= right:
        if left % == 0:
            answer[idx] = arr[left]
            left += 1
        else:
            answer[idx] = arr[right]
            right -= 1
        idx += 1
    return answer

    arr = [1, 2, 3, 4, 5, 6]
    ret = solution(arr)

    print("solution 함수의 반환 값은 ", ret, "입니다.")
