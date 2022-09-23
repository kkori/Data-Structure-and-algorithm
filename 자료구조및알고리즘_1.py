import heapq

def heap_sort(value):
    data = []
    result = []
    for s1 in value:
        heapq.heappush(data, s1)

    while len(data) > 0:
        a = heapq.heappop(data)
        result.append(a)

    return result

def heap_sort2(value):
    data = []
    result = []
    for s1 in value:
        heapq.heappush(data, -s1)

    while len(data) > 0:
        a = heapq.heappop(data)
        result.append(-a)

    return result

def problem1():
    sco_num = int(input("스코빌 지수를 지정하시오. >> "))
    food_scovil = list(map(int, input("음식들의 스코빌 지수를 입력하시오. >>").split()))
    count = 0
    food_scovil = heap_sort(food_scovil)

    while min(food_scovil) < sco_num:
        first = heapq.heappop(food_scovil)
        second = heapq.heappop(food_scovil)
        mix = first + 2 * second
        heapq.heappush(food_scovil, mix)
        food_scovil = heap_sort(food_scovil)
        count += 1

    result = print(f'{food_scovil}, {count}')
    return result


def problem2():
    num1 = 0
    while num1 < 1:
        work_load = list(map(int, input("작업량을 입력하시오. >>").split()))
        work_load
        if len(work_load) > 200 or len(work_load) < 1:
            print("Works의 길이를 다시 입력하세요.")
        elif max(work_load) > 500:
            print("Works는 500을 넘을 수 없습니다. 다시 입력하세요.")
        else:
            num1 += 1

    num2 = 0
    while num2 < 1:
        work_times = int(input("남은 시간을 입력하시오. >> "))
        work_times
        if work_times > 10000 or work_times < 1:
            print("Work time은 10000이하의 자연수여야 합니다. 다시 입력하세요.")
        else:
            num2 += 1

    original_work_times = work_times

    while work_times >= 1:
        work_load = heap_sort2(work_load)
        min1 = heapq.heappop(work_load)
        min1 = min1 - 1
        heapq.heappush(work_load, min1)
        work_times -= 1
        work_load = heap_sort2(work_load)

    work_tired = []
    for i in range(len(work_load)):
        tired = work_load[i] ** 2
        heapq.heappush(work_tired, tired)

    work_tired_sum = sum(work_tired)

    result = print(f'{work_load} {original_work_times} {work_tired_sum}')

    return result

if __name__ == "__main__":
    problem1()
    problem2()