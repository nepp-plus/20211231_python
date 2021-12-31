# DB를 조회 / 수정 / 삭제 / 추가 등등 => DB를 제어 (Control)
# 모델을 이용해 데이터를 컨트롤 =>  Controller

# DB 연결 / 쿼리 / 결과 분석 표시 등등
# 데이터베이스와 관련된 파이썬 코드.
from pymysql import connect
from pymysql.cursors import DictCursor  # DB SELECT 결과를 dict 형태로 가져오게 해주는 클래스

# connect 함수를 직접 import => pymysql.  코드 생략
db = connect(
    host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306, # port : 한대의 컴퓨터가 여러개의 프로그램을 돌릴때 -> 각각의 (인터넷을 통해서) 프로그램을 찾아갈 때 사용하는 고유 번호. -> mysql : 보통 3306번 포트에 실행시켜두는게 일반적.
    user='admin',
    passwd='Vmfhwprxm!123',  # 프로젝트!123  (첫글자만 대문자)
    db='test_202112_python',  # 호스트에 있는 여러 논리DB중 사용할 DB 선정.
    charset='utf8',  # 연결할 DB가 한글을 utf8 인코딩으로 한글 처리진행.
    cursorclass=DictCursor
)

# 쿼리수행 전담 변수  (연결된 DB에서 수행)
cursor = db.cursor()

#  필요기능들을 함수로 작성.

def get_user_list():
    sql = f"SELECT * FROM users"
    cursor.execute(sql)
    
    result = cursor.fetchall()
    # API => 원하는 쿼리의 수행 결과를, 가공해서 화면단에서 사용할 수 있게 전달해주는 역할.
    return result

# 페이지에 맞는 게시글 목록 가져오기

def get_posts(page):
    # 1페이지당 5개의 글을 보여준다.
    
    # 1페이지 : 0개의 글 패스, 그 다음 5개. (1~5)
    # 2페이지 : 5개 패스, 그 다음 5개.
    # 3페이지 : 10개의 글 패스, 그 다음 5개의 글 보여주기. (11~15)
    # 4페이지? : 15개 패스, 5개.
    
    # ORDER BY / LIMIT 쿼리 활용.
    # LIMIT 건너뛸갯수, 보여줄 갯수 활용.
    
    # 몇페이지냐에 따른 -> 건너뛸 갯수는 몇개?  쿼리 작성가능.
    offset = (page - 1) * 5
    
    sql = f"SELECT * FROM posts AS p ORDER BY p.created_at DESC LIMIT {offset}, 5"
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    print(result)
    
    return result