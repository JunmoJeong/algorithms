import time
words = []

def solution(word):
    global words
    words = ['']
    answer = 0
    VOWELS = ['A', 'E', 'I', 'O', 'U']

    for i1 in range(0, 5):
        words.append( VOWELS[i1])
        for i2 in range(0,5):
            words.append(VOWELS[i1] + VOWELS[i2])
            for i3 in range(0, 5):
                words.append(VOWELS[i1] + VOWELS[i2]+VOWELS[i3])
                for i4 in range(0, 5):
                    words.append(VOWELS[i1] + VOWELS[i2] + VOWELS[i3]+VOWELS[i4])
                    for i5 in range(0, 5):
                        words.append(VOWELS[i1] + VOWELS[i2] + VOWELS[i3] + VOWELS[i4]+ VOWELS[i5])

    for idx, i in enumerate(words):
        if word == i:
            answer = idx
            break
    return answer



# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
start=time.time()
for i in range(1000):
    word1 = "EAAAE"
    ret1 = solution(word1)
end=time.time()
# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(end-start, "solution 함수의 반환 값은 ", ret1, " 입니다.")



'''
word2 = "AAAE"
ret2 = solution(word2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
'''