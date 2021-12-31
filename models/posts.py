class Posts:
    def __init__(self, data_dict):
        self.id =  data_dict['id']
        self.user_id =  data_dict['user_id']
        self.title =  data_dict['title']
        self.content =  data_dict['content']
        self.created_at =  data_dict['created_at']
        self.writer_name = data_dict['writer_name']
        
    # 게시글 목록 표시 (간단 정보)
    # 제목 : 실제제목 (8월 5일, 조경진이 작성함.)  => 작성자 이름도 같이 표시.
    def get_simple_post(self):
        
        format_date = self.created_at.strftime( '%m월 %d일' )
        
        print(f'제목 : {self.title} ({format_date}, {self.writer_name}이(가) 작성함)')