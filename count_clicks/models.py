# count_clicks/models.py

from django.db import models

# count_id => AUTO INCREMENT, PK
# clicked_date => Date
 
class ClickModel(models.Model):
    count_id = models.AutoField(primary_key =  True)
    clicked_date = models.DateTimeField(auto_now_add = True) # POST 요청이 들어오면 현재 날짜가 자동으로 생성됨!

    def __str__(self):
        return f"Click {self.count_id} on {self.clicked_date}"
    
    # 데이터베이스의 레코드를 5000개만 유지하기 위해 ClickModel의 save메서드를 오버라이드
    # => 데이터베이스의 레코드 수를 체크함, 레코드가 5000개가 넘는다면 가장 오래된 레코드를 삭제
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if ClickModel.objects.count() > 5000:
            ClickModel.objects.earliest('count_id').delete()