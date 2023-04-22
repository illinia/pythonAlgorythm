"""
1. 설명
    * 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸기
    * 교환하기 위한 기준을 피벗이라고 표현한다. 리스트에서 첫 번째 데이터를 피벗으로 정한다.
    1. 피벗의 왼쪽부터 피벗보다 큰 데이터를 찾고, 오른쪽부터 피벗보다 작은 데이터를 찾는다.
    2. 계속 진행하다 왼쪽 값과 오른쪽 값이 엇갈린 경우 작은 데이터와 피벗의 위치를 서로 변경한다.
    3. 가운데 있는 피벗 기준으로 왼쪽에는 피벗보다 작은 데이터, 오른쪽에는 피벗보다 큰 데이터 가 존재하게 된다.
    4. 정렬이 한번 완료되면 재귀 호출하여 피벗 양 옆의 배열을 다시 정렬한다. 재귀 함수의 종료 조건은 배열 길이가 1인 경우이다.
2. 코드 설계
    1. 무작위 수 배열
    2. 퀵정렬 함수 정의(배열, 시작 인덱스, 끝 인덱스)
        1. 배열의 원소 길이가 1 인 경우 종료
        2. 피벗 = 첫 번째 원소
        3. 왼쪽 인덱스 = 두 번재 원소, 오른쪽 인덱스 = 마지막 원소
        4. 왼쪽 인덱스가 오른쪽 인덱스보다 작거나 같으면 반복
            1. 피벗보다 큰 데이터를 찾기위해 반복(왼쪽 인덱스가 끝 인덱스보다 작거나 같고, 왼쪽 값이 피벗 값보다 작거나 같으면 반복 -> 크면 찾았다는 뜻이므로 종료)
                1. 왼쪽 인덱스에 1을 더해준다.
            2. 피벗보다 작은 데이터를 찾기 위해 반복(오른쪽 인덱스가 시작 인덱스보다 크고(피벗 인덱스), 오른쪽 값이 피벗 값보다 크거나 같으면 반복 -> 작으면 찾았다는 뜻이므로 종료)
                1. 오른쪽 인덱스에 1을 빼준다.
            3. 왼쪽 인덱스가 오른쪽 인덱스보다 크면(엇갈렸다면) 작은 데이터와 피벗을 교체
            4. 왼쪽 인덱스가 오른쪽 인덱스보다 같거나 작다면, 왼쪽 인덱스와 오른쪽 인덱스의 값을 교체
        5. 분할 이후 피벗 기준 왼쪽 배열과 오른쪽 배열에서 각각 함수 실행
"""
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

