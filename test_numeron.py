from numeron import *
import logging

def is_two_dimension(request: list):
    return (type(request) == list and type(request[0]) == list)

def is_list_unique(request: list):
    req_len = len(request)

    for i in range(0, req_len, 1):
        for j in range(i + 1, req_len, 1):
            if request[i] == request[j]:
                return False
    return True

def is_lists_unique(request: list):
    for row in request:
        flag = is_list_unique(row)
        if flag == False:
            return False, row
    return True, None

def n_numeron(request: list, hit: int, blow: int):
    # 
    assert is_two_dimension(request) #, f"求められた結果情報が2次元配列ではありませんでした\n{request}"

    # 
    is_lists_unique_flag, duplicate = is_lists_unique(request)
    assert is_lists_unique_flag , f"求められた結果情報に重複の数字が含まれていました{duplicate}"

def n_test(request: list, hit: int, blow: int):
    response = [[1, 2, 3], [1, 1, 3]]# NumerOn.forecast(request, hit, blow)
    n_numeron(response, hit, blow)

def test_main():
    # Test1
    n_test([1, 2, 3], 0, 0)
