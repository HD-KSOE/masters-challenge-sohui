def solution(left, right):
    answer = 0
    count = 0
    isTrue = []
    isFalse = []
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            isTrue.append(i)
        else:
            isFalse.append(i)
    print(isTrue, isFalse)
    answer = sum(isTrue) - sum(isFalse)
    
    return answer