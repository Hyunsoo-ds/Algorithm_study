n  = int(input())

change = []
answer_list = []
for i in range(n):
    change.append(int(input()))

for i in change:
    num = i
    answer = []
    for value in [25,10,5,1]:
        answer.append(num // value)
        num = num % value
    answer_list.append(answer)

for answer in answer_list:
    print(' '.join(str(i) for i in answer))
