eng = ["apple", "banana", "orange"]
kor = ["사과", "바나나", "오렌지"]

print(list(zip(kor, eng)))  # 리스트 두개를 세로로 합친다.

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))
# 다시 풀떄는 * 을 붙인다.

kor2, eng2 = zip(*mixed)
print(kor2, eng2)
