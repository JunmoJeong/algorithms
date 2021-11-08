import time
words = []
cnt=0

def create_words(lev, s):
    global words
    global cnt
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    for i in range(0, 5):
        if lev < 5:
            cnt+=1
            print(cnt, "i:",i, "lev:", lev,s+VOWELS[i])
            create_words(lev+1, s + VOWELS[i])


def solution(word):
    global words
    words = []
    answer = 0
    create_words(0, '')
    for idx, i in enumerate(words):
        if word == i:
            answer = idx
            break
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
start=time.time()
for i in range(10000):
    word1 = "EAAAE"
    ret1 = solution(word1)
end=time.time()

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(end-start,"solution 함수의 반환 값은 ", ret1, " 입니다.")
'''
word2 = "AAAE"
ret2 = solution(word2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")
'''