# Click This !
https://clickthis.dlawork9888.site

## One Day Project ! 
for Deploy Practice ...

## Latest ! - 2024.05.30
```
- ClickThisModel의 DateField => DateTimeField -> 로그 등록을 위해
- migration: 기존 데이터를 유지하기 위해, 새로운 필드를 추가하고, 데이터를 변환한 후, 원래 필드를 제거
   - clickthis_django/count_clicks/migrations/0002_alter_clickmodel_clicked_date.py 참고
- ClickAPIView 수정
   - GET request에 쿼리 파라미터 추가
   - GET /api/clicks/?top100=true 이면 top100 로그를 반환
   - clickthis_django/count_clicks/views.py 참고
```
##2024.04.18
```
- 혹시 모를 DB볼륨 폭발을 방지하기 위한 Database Trigger 추가
   - 사실 트리거는 아니고(DB Trigger는 DB를 직접 건드려함), ClickModel의 save메서드를 오버라이드
   - 레코드 개수를 확인하고 일정 수가 넘으면 오래된 레코드를 삭제하도록 확장
- local test를 위해 settings.py의 DATABASES를 살짝 수정 => deploy, local_test 변수로 통제
```


## 2024.04.17
```
- HTTPS 적용 완료 !
- NGINX 설정 완료 !
- Docker: mysqlclient로 인한 빌드 이슈로 Dockerfile 수정 
```

## 2024.03
```
- 컨테이너에 가둬버리기 위해 SPLIT!
```
