# 메뉴 입력 / 분기 처리 등
# 사용자 Contact 부분 전담. => Android App으로 대체 / HTML 웹으로 대체

# 메인 메뉴 출력 기능 (함수)
def show_main_menu():
    print('===== 강의 관리 시스템 (LMS) =====')
    print('1. 수강생 목록 조회')
    print('0. 프로그램 종료')
    print('=================================')
    num = int( input('메뉴 선택 : ') )
    
    if num == 0:
        pass
    elif num == 1:
        pass