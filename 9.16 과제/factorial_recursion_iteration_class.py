#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 방준영
#  작성일: 2025-09-21
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

import time

# -------------------------------
# 1) 함수 구현
# -------------------------------

def factorial_iter(n: int) -> int:
    """반복문으로 n! 계산"""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n: int) -> int:
    """재귀 호출로 n! 계산"""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n-1)

def run_with_time(func, n: int):
    """함수를 실행하고 실행 결과와 경과 시간을 반환"""
    start = time.time()
    result = func(n)
    elapsed = time.time() - start
    return result, elapsed

# -------------------------------
# 2) 인터랙티브 메뉴
# -------------------------------

TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def menu():
    while True:
        print("\n===== 팩토리얼 계산기 =====")
        print("1. 반복문으로 계산")
        print("2. 재귀로 계산")
        print("3. 두 방식 비교")
        print("4. 테스트 데이터 실행")
        print("q. 종료")
        choice = input("메뉴를 선택하세요: ").strip()

        if choice in ("q", "quit", "Q"):
            print("프로그램을 종료합니다.")
            break

        elif choice in ("1", "2", "3"):
            n_str = input("정수를 입력하세요: ").strip()
            if not n_str.isdigit():
                print("오류: 정수를 입력해야 합니다.")
                continue
            n = int(n_str)

            try:
                if choice == "1":
                    res, t = run_with_time(factorial_iter, n)
                    print(f"[반복문] {n}! = {res} (시간: {t:.6f}초)")
                elif choice == "2":
                    res, t = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {res} (시간: {t:.6f}초)")
                elif choice == "3":
                    res_iter, t_iter = run_with_time(factorial_iter, n)
                    print(f"[반복문] {n}! = {res_iter} (시간: {t_iter:.6f}초)")
                    res_rec, t_rec = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {res_rec} (시간: {t_rec:.6f}초)")
                    print("결과 일치:", res_iter == res_rec)
            except ValueError as e:
                print("오류:", e)
            except RecursionError:
                print("RecursionError: 입력값이 너무 큽니다.")

        elif choice == "4":
            print("\n===== 테스트 데이터 실행 =====")
            for n in TEST_DATA:
                print(f"\n▶ n = {n}")
                try:
                    res_iter, t_iter = run_with_time(factorial_iter, n)
                    print(f"[반복문] {n}! = {res_iter} (시간: {t_iter:.6f}초)")
                    res_rec, t_rec = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {res_rec} (시간: {t_rec:.6f}초)")
                    print("결과 일치:", res_iter == res_rec)
                except ValueError as e:
                    print("오류:", e)
                except RecursionError:
                    print("RecursionError 발생 (입력값이 너무 큼)")

        else:
            print("잘못된 입력입니다. 메뉴 번호를 다시 선택하세요.")

# -------------------------------
# 실행부
# -------------------------------
if __name__ == "__main__":
    menu()

