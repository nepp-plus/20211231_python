#  users 테이블을 표현하는 용도.
#  DB의 테이블을 => 프로그램에서 표현하는 클래스들을 => model 이라고 부름.

class Users:
    
    def __init__(self, info_dict):
        # info_dict 안의 이름표 / 실제값을 이용해서 데이터 세팅.
        self.id = info_dict['id']
        self.name = info_dict['name']
        self.birth_year = info_dict['birth_year']
        self.address = info_dict['address']
        self.gender = info_dict['gender']
        self.height = info_dict['height']
        self.created_at = info_dict['created_at']
        self.friend_id = info_dict['friend_id']
    
    # 사용자의 정보를 가공해서 간략하게 출력.
    # 이름 - 35세, 남성
    def get_simple_info(self):
        print(f'{self.name} - {self.get_age()}세,  {self.gender}')
    
    # 사용자의 나이를 계산해주는 기능 추가.
    def get_age(self):
        # 현재 일자의 연도를 얻어오면, 자동으로 현재 나이 계산 가능.
        return 2021 - self.birth_year + 1