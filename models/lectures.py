class Lectures:
    def __init__(self, data_dict):
        self.name = data_dict['name']
        
        # 평균점수 : DB에서 긴 소수점이 와도 => 파이썬에서 소수점 1자리로만 넣어주자.
        self.avg_score = round(data_dict['avg_score'], 1)