"""
1. 문제 이해
    1. 설명
        * n 개의 정수로 이루어진 임의의 수열
        * 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합
        * 첫째 줄에 정수 n (1 <= n <= 100,000) 주어지고 둘째줄에 n 개의 정수로 이루어진 수열 주어진다.
    2. 제약사항
        * 1 <= n <= 100,000
        * -1,000 <= 수 <= 1,000
2. 접근 방법
    * 연속된 수를 선택해서 합을 구하기 때문에 이전의 값들의 합이 현재 값에 영향을 미친다.
    * 이미 계산한 이전 값들을 저장해놓고 현재 최대값 계산시 사용하면 될듯. dp 문제
    * 현재 값과, 현재값 + 이전 원소를 포함하는 최대 부분합을 더한 값을 비교해서 부분 최댓값 리스트에 저장
    * 이전 원소를 포함하는 이라는 조건이 붙은 이유는 연속된 값들의 합을 구해야하기 때문에
      연속되지 않은 경우에는 이미 연속되지 않은 값이 이전 값보다 큰 경우라
      후에 부분 최댓값 리스트에서 최댓값 구하면 되기 때문
    * 최댓값은 부분 최댓값 리스트에서 가장 큰 수를 찾으면 됨
3. 코드 설계
    1. n 입력, 리스트에 n 개의 수열을 저장
    2. 부분 최댓값 리스트 생성
    3. 부분 최댓값 리스트 첫번째 요소는 입력 리스트 첫번째 요소로 저장
    4. 입력 리스트 요소들 두번째 요소부터 반복
        1. 부분 최댓값 리스트에 현재 값과, 현재 값 + 이전 요소값 포함하는 부분 최대값 중 최댓값을 저장
    5. 부분 최댓값 리스트에서 최댓값 출력
"""

from sys import stdin

# 1
n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

# 2
part_max_list = list()

# 3
part_max_list.append(numbers[0])

# 4
for i in range(1, n):
    part_max_list.append(max(numbers[i], numbers[i] + part_max_list[i - 1]))

print(max(part_max_list))