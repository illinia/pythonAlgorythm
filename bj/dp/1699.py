"""
1. 문제 이해
    1. 설명
        * 자연수 N 은 작거나 같은 제곱수의 합으로 나타낼 수 있다.
        * 제곱수 항의 최소 갯수를 구하기
    2. 제약사항
        * 1 <= N <= 100,000
2. 접근 방법
    * 예시
        1 = 1^2
        2 = 1^2 + 1^2
        3 = 1^2 + 1^2 + 1^2
        4 = 2^2
        5 = 2^2 + 1^2
        6 = 2^2 + 1^2 + 1^2
        7 = 2^2 + 1^2 + 1^2 + 1^2
        8 = 2^2 + 2^2
        9 = 3^2
        10 = 3^2 + 1^2
        11 = 3^2 + 1^2 + 1^2
    * 어떤 수보다 작은 제곱수를 구해서 빼고 남은 수는 dp 테이블에서 가져와서 계산
    * N + 1 길이의 dp 리스트에 인덱스에 해당하는 숫자 저장
    * 1 부터 N 까지 반복하면서 1 부터 N 까지 이중 반복문 실행
    * 이중 반복에서 반복 값의 제곱이 N 보다 클경우 반복문 탈출
    * 작거나 같을 경우 이중 반복 제곱 dp 값 = 1 + N - 이중 반복 제곱 dp
3. 코드 설계
    1. N 입력
    2. 0 부터 N 까지의 dp 테이블을 리스트로 생성, 인덱스에 해당하는 값을 저장
    3. 1 부터 N 까지 반복
        1. 1 부터 해당 인덱스까지 반복
            1. 이중 반복 값의 제곱이 N 보다 클 경우 이중 반복문 탈출
            2. 작거나 같을 경우, 이중 반복 값의 제곱 dp 테이블 + N - 반복값 제곱 dp 테이블 구하기
            3. 현재 N dp 테이블 값과 위에서 구한값 중 작은 값을 현재 N dp 테이블 에 다시 저장
    4. dp 테이블 N 번째 값 출력
"""
N = int(input())

dp = [x for x in range(0, N + 1)]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        if j ** 2 > i:
            break
        if dp[i] > 1 + dp[i - j ** 2]:
            dp[i] = 1 + dp[i - j ** 2]

print(dp[N])