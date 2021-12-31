#  users 테이블을 표현하는 용도.
#  DB의 테이블을 => 프로그램에서 표현하는 클래스들을 => model 이라고 부름.

class Users:
    
    def __init__(self, info_dict):
        # info_dict 안의 이름표 / 실제값을 이용해서 데이터 세팅.
        print(info_dict)
    