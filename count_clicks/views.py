# count_clicks/views.py

from django.shortcuts import render
# for API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ClickModel # Click 모델 import
from .serializers import ClickSerializer #Click 시리얼라이저 import

# logger
import logging
logger = logging.getLogger(__name__)


class ClickAPIView(APIView):


    
    ### GET
    # 페이지가 처음 로드될 때, count_id을 기준으로 DESC 정렬을 했을 때 가장 처음 레코드의 count_id를 반환
    # SELECT COUNT_ID FROM CLICK ORDER BY DESC 
    def get(self, request, *args, **kwargs):
        print('Click - GET requset')
        # 로그 반환 GET 요청 추가
        # GET /api/clicks/?top100=true 요청이면 아래 수행
        # 쿼리 파라미터로 top100 요청인지 확인
        top100 = request.query_params.get('top100', 'false').lower() == 'true'
        print(f'top100 request: {top100}')
        if top100:
            top_clicks = ClickModel.objects.order_by('-count_id')[:100]
            if top_clicks.exists():  # 있으면
                serializer = ClickSerializer(top_clicks, many=True)
                response_data = serializer.data
                return Response(response_data, status=status.HTTP_200_OK)
            else:  # 없으면
                return Response({'message': 'No clicks found.'}, status=status.HTTP_404_NOT_FOUND)
        # GET /api/clicks/이면 아래 수행
        else:
            # SQL QUERY ?
            # SELECT * FROM ClickModel ORDER BY count_id DESC LIMIT 1;
            # To Queryset ! 
            latest_click = ClickModel.objects.order_by('-count_id').first()
            # 테이블이 비어있을 수도 있으니까
            if latest_click: # 있으면
                serializer = ClickSerializer(latest_click)
                reponse_data = {'count_id': serializer.data.get('count_id')}
                return Response(reponse_data, status=status.HTTP_200_OK)
            else: # 없으면
                return Response({'message': 'No clicks found.'}, status=status.HTTP_404_NOT_FOUND)
        


    ### POST
    # 이 POST요청 body에는 아무 데이터도 포함되어 있지 않음 !
    def post(self, request, *args, **kwargs):
        # ClickModel의 인스턴스 생성
        click = ClickModel()
        # POST 처리 => AUTO INCREMENT, auto_now_add 로 자동으로 POST를 처리함
        # 사실 시리얼라이저는 필요없었던 것!
        click.save()
        # 그래도 Response에 담아서 주면 좋으니까 써주자
        # 사실 담아서 줘야하긴 함! (이렇게 안담아도 되지만)
        serializer = ClickSerializer(click)
        reponse_data = {'count_id': serializer.data.get('count_id')}
        return Response(reponse_data, status=status.HTTP_201_CREATED)