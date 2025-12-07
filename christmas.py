# 층 수를 입력받아 별 트리를 찍어 주는 코드

height = int(input("트리 높이를 입력하세요: "))

for i in range(1, height + 1):
    # 왼쪽 공백
    spaces = " " * (height - i)
    # 가운데 별 (1, 3, 5, 7, ...)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# 줄기
spaces = " " * (height - 1)
print(spaces + "|")
