list_01 = []
dict_01 = {"1":".Push","2":".Pop","3":".Peek","0":".Exit"}

def push_01(num_01):
    if len(list_01) >= 5:
        print("> Stack이 차 있어서 더 이상 추가할 수 없습니다.")            
    else:
        #   입력된 데이터 출력
        input_02 = int(input("> 데이터 입력 : "))
        #   현재 저장된 스택상태 출력
        list_01.append(input_02)
    #   현재 스택 상태
    print(f"> 현재 스택 상태: {list_01}")

def pop_02(num_02):
    global list_01
    #   스택이 비어있으면
    if len(list_01) <= 0:
        print("> Stack이 비어있습니다.")
    #   스택에 값이 있으면
    else: 
        num_02 = list_01[-1]
        print(f"> 가져온 데이터: {num_02}")
        list_01 = list_01[:-1]
    #   현재 스택 상태
    print(f"> 현재 스택 상태: {list_01}")
    
def peek_03(num_03):
    global list_01
    #   스택이 비어있으면
    if len(list_01) <= 0:
        print("> Stack이 비어있습니다.")
    #   스택에 값이 있으면
    else: 
        num_03 = list_01[-1]
        print(f"> 가져올 데이터: {num_03}")
    print(f"> 현재 스택 상태: {list_01}")    


while True:
    print("----------[ 정수형 스택 연산 실습 (용량 5)]----------")
    print("="*30)
    #   메뉴 출력 위한 길자란 생성
    str_01 = ""
    #   dict_01에 따른 메뉴 출력 위한 반복문 실행
    for key_01, value_01 in dict_01.items():
        str_01 += f"{key_01}{value_01}\t"
    print(str_01)
    print("="*30)
    
    #   메뉴 선택에 따른 기능 실행
    input_01 = int(input("> 메뉴 선택 : "))
    if input_01 == 1: push_01(input_01)
    elif input_01 == 2: pop_02(input_01)
    elif input_01 == 3: peek_03(input_01)
    elif input_01 == 0: 
        print("----------[ 정수형 스택 연산 실습 종료]----------")
        break
    else: continue