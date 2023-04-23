"""
1. 설명
    1. 매개변수 탐색(Parametric Search) 란
        * 이진탐색과 유사한 알고리즘
        * 최적화 문제를 "결정 문제"로 풀 수 있는 알고리즘
        * 시간 복잡도 O(LogN)
    2. 매개변수 탐색을 사용하는 시기
        1. 결정문제로 풀면 쉽게 문제를 풀 수 있을 때
        2. 어떤 시점까지는 조건을 만족하지만, 그 후로는 조건을 만족하지 않는 경우. 조건을 만족하는 최댓값 찾기
        3. 어떤 시점까지는 조건을 만족하지 않지만, 그 후로는 조건을 만족하는 경우. 조건을 만족하는 최솟값 찾기
    3. 매개변수 탐색에서 중요한 문제 - 매개변수와 결정함수
        1. 매개 변수
            * 매개변수 탐색은 조건에 만족하는 최솟값/최댓값을 찾는 문제
            * 검사하는데 사용하는 매개변수를 param 이라고 가정
            * param 은 검사 범위(left, right)에서 중간값. 해당 범위에서 (left + right) / 2 가 param 이 된다.
        2. 결정 함수
            * param 이 조건을 만족하면 true, 만족하지 않으면 false 를 반환하는 함수
            * 반환값에 따라서 검사 범위를 변경하게 된다.
            * param 의 범위는 연속이어야 하는데 fn(param) 값이 false, true 가 바뀌는 부분이 생긴다.
            * 이때 true 를 반환할 때 param 이 찾고자 하는 min/max 값이 된다.
            * 결정함수 fn(param) 의 결과에 따라서 검사 범위를 변경한다.
2. 접근 방법
    1. 결정 함수의 구현
        * 결정함수 설명에서 어떤 조건을 만족한다는 것은 param 의 값에 따라서 문제에서 주어진 조건을 만족하는가를 믇는 것이다
        * 따라서 어떤 조건이 무엇인지 알고 싶다면 문제에서 조건을 알아본다
    2. 매개변수 탐색 작동 방식
        1. 조건을 만족하는 최댓값을 찾을 때
        2. 배열 가운데 위치한 x를 결정함수에 대입해 조건을 만족하는지 알아본다.
        3. 조건을 만족한다면 검사 범위를 x 보다 큰 쪽으로 설정, 만족하지 않는다면 검사 범위를 x 보다 작은 쪽으로 설정
        4. 1, 2 번을 살펴볼 배열이 남아있지 않을 때까지 반복
"""
"""
1. 백준 1654 예
    1. N 개의 랜선을 만들어야하고 길이가 다른 K 개의 랜선을 가지고 있을 때 각각 잘라서 N 개를 만들 수 있는 최대 길이를 구하기
    2. 조건을 만족하는 최대 길이 구하는 문제이므로 매개변수 탐색을 사용할 수 있다.
    3. 탐색의 시간 복잡도는 이분 탐색이랑 같고 최소, 최대 길이 사이에서 길이를 탐색하는 과정 LogN, 각 랜선을 잘라서 갯수를 카운트하는 과정 N, 총 O(NLogN) 시간이 걸린다.
    4. 랜선의 길이는 2^31 - 1 이므로 int 형으로 처리 가능
2. 접근 방법
    1. 매개변수 탐색을 사용시 타겟과 결정함수를 정의해야한다.
    2. target 은 자를 랜선의 길이 x 로 정의
    3. 결정함수는 K 개의 랜선들을 x 길이만큼 잘랐을 때 만들 수 있는 랜선들의 갯수가 N 보다 같거나 많은 경우에 true, 아니면 false
    4. 중간값을(자를 랜선의 길이) 구해서 해당 값이 결정함수로 계산했을 때 true 이면 시작값을 중간값 + 1, false 이면 끝값을 중간값 - 1
3. 코드 설계
    1. K(가지고 있는 랜선의 갯수), N(필요한 랜선의 갯수) 입력
    2. 선 리스트 정의하고, K 번 만큼 선의 갯수 입력
    3. 결정함수 정의
        1. 자를 선의 길이를 매개변수 x 로 받고, 최종 출력할 자른 랜선의 갯수 count 를 0 으로 초기화
        2. K(랜선) 리스트를 반복하면서 매개변수로 받은 선의 길이만큼 나눈 몫을 count 에 더하기
        3. 반복 종료 후 count 가 N 보다 크거나 같은 경우 true 반환(자른 랜선의 갯수가 필요한 랜선의 갯수보다 많다. 조건 만족), 작은 경우 false 반환
    4. left(최소 선의 길이) = 1, right(최대 선의 길이) = 선 리스트에서 최댓값
    5. left <= right 인 경우 반복
        1. mid = (left + right) // 2
        2. mid 를 결정 함수에 넣어서 반환값이 true 이면 left = mid + 1, false 이면 right = mid - 1
    6. 최댓값을 구해야하므로 조건을 만족하지 않다가 만족하게 되는 순간 큰 값(right) 이 최댓값이므로 right 출력
"""
from sys import stdin

K, N = map(int, stdin.readline().split())

lines = []
for _ in range(K):
    lines.append(int(stdin.readline()))


def fn(x):
    count = 0
    for line in lines:
        count += line // x
    if count >= N:
        return True
    else:
        return False


left = 1
right = max(lines)

while left <= right:
    mid = (left + right) // 2
    if fn(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)