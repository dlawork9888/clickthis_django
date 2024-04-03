# 베이스 이미지는 Alpine Linux 기반으로 선택
FROM python:3.8-alpine

# 바이트 코드 캐싱 안하게 설정
ENV PYTHONDONTWRITEBYTECODE 1
# Python의 stdout과 stderr의 버퍼링 비활성화
ENV PYTHONUNBUFFERED 1

# 필요한 패키지 설치를 위해 build-base와 libressl-dev를 추가
RUN apk update \
    && apk add --no-cache build-base libressl-dev \
    && rm -rf /var/cache/apk/*

# 워크 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . /app/

# 정적 파일 수집 및 압축
RUN python manage.py collectstatic --noinput

# 포트 노출
EXPOSE 8002

# Gunicorn 실행
CMD ["sh", "-c", "python manage.py migrate && gunicorn clickthis_django.wsgi:application --bind 0.0.0.0:8002"]
