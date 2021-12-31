# 사용자에게 보여지는 부분 전담. => View

# Model + Controller + View 조합 코딩 패턴 => MVC 패턴.

# 메뉴 입력 / 분기 처리 등
# 사용자 Contact 부분 전담. => Android App으로 대체 / HTML 웹으로 대체
from db_handler import get_user_list, get_posts, get_all_user_count, get_all_lectures
from models import Users, Posts, Lectures
from time import sleep


# 메인 메뉴 출력 기능 (함수)
def show_main_menu():
    while True:
        print('===== 강의 관리 시스템 (LMS) =====')
        print('1. 수강생 목록 조회')
        print('2. 게시글 목록 조회')
        print('3. 강의 목록 조회')
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
        elif num == 2:
            # DB에서 게시글 목록 조회
            page_num =  int( input('몇페이지의 글을 보겠습니까? : ') )
            get_posts_by_page_num(page_num)
        elif num == 3:
            print('===== 강의 관리 ======')
            # DB에서 강의목록 + 평균 평점 조회.
            get_lecutres_from_db()
            # 신규 과목 추가 or 이전 항목으로.
            print('1. 신규 과목 추가')
            print('0. 이전으로')
            print('=====================')
            lecture_menu_num = int( input('메뉴 선택 : ') )
            if lecture_menu_num == 1:
                # 추가 강의 입력. 항목들은 main.py에서 입력
                
                lecture_name = input('강의명 : ')
                max_count = int(input('정원 : '))
                fee = int(input('강의료 : ') )
                
                # DB에 추가 => db_handler.py에서 SQL.
                
                print('강의 추가가 완료되었습니다.')
                sleep(2)
                
                

# 1번 누르면 => DB에서 수강생 목록 조회를 요청하는 기능.
def get_user_list_from_db():
    result = get_user_list()  # DB 전담 클래스가 보내준 결과 (dict여러개 -> tuple) 를 => UI에서 활용.
    
    # for문으로 돌아보면서 -> 문구 가공 / 출력
    for row  in result:
        # print(row)  # row한줄 : 하나의 dict로 표현됨.
        user = Users(row)
        user.get_simple_info() # user에 만들어진 메쏘드 활용.
        
    # DB한번 더 접근. => 인원수 파악.
    user_count = get_all_user_count()  # 이 함수는 내부에서 숫자만 추출해서 리턴.
    print(f'총 수강생 : {user_count}명')
    
# 2번 누르면 => DB에서 게시글을 페이지에 맞게 요청하는 기능.
def get_posts_by_page_num(page):
    result = get_posts(page)
    for row in result:
        # print(row)
        post = Posts(row)
        post.get_simple_post()
        

# 3번 누르면 => DB에서 강의목록 + 강의별 평균 점수.
def get_lecutres_from_db():
    query_result = get_all_lectures()
    
    for row in query_result:
        lecture = Lectures(row)
        print(lecture.name,  lecture.avg_score)
    
    
    
#  python 명령어로 실행될때 => 위에서부터 밑으로 한줄씩 순서대로 실행됨.
#  함수도 만들어 두고 나서 사용해야함.
show_main_menu()
