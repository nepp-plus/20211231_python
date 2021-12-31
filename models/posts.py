class Posts:
    def __init__(self, data_dict):
        self.id =  data_dict['id']
        self.user_id =  data_dict['user_id']
        self.title =  data_dict['title']
        self.content =  data_dict['content']
        self.created_at =  data_dict['created_at']
        
    # 게시글 목록 표시 (간단 정보)
    # 제목 : 실제제목 (8월 5일 작성됨.)
    def get_simple_post(self):
        
        format_date = self.created_at.strftime( '%m월 %d일' )
        
        print(f'제목 : {self.title} ({format_date} 작성됨)')