# 메뉴 입력 / 분기 처리 등
# 사용자 Contact 부분 전담. => Android App으로 대체 / HTML 웹으로 대체

# 메인 메뉴 출력 기능 (함수)
def show_main_menu():
    while True:
        print('===== 강의 관리 시스템 (LMS) =====')
        print('1. 수강생 목록 조회')
        print('0. 프로그램 종료')
        print('=================================')
        num = int( input('메뉴 선택 : ') )
        
        if num == 0:
            print('프로그램을 종료합니다.')
            break
        elif num == 1:
            # 코드를 불러낼떄 진짜 실행되는게 아님.
            # 코드가 다 불러지고 => 메뉴도 다 나타나고 => 키보드로 1번을 골랐을떄가 되어야 실행.
            # 함수 안의 다른 함수 호출 :  위아래 순서에 관계 없이 불러낼 수 있다.
            get_user_list_from_db()

# 1번 누르면 => DB에서 수강생 목록 조회를 요청하는 기능.
def get_user_list_from_db():
    print('db_handler에게 사용자 목록을 요청하자.')
    
#  python 명령어로 실행될때 => 위에서부터 밑으로 한줄씩 순서대로 실행됨.
#  함수도 만들어 두고 나서 사용해야함.
show_main_menu()
