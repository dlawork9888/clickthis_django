# 베이스 이미지로 Debian Buster Slim 기반의 Python 3.8 이미지 사용
FROM python:3.8-slim

# 파이썬 바이트 코드 생성 안 함
ENV PYTHONDONTWRITEBYTECODE 1
# 파이썬의 stdout과 stderr 버퍼링 비활성화
ENV PYTHONUNBUFFERED 1


# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    default-libmysqlclient-dev \
    libmariadb-dev \ 
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# pip 최신 버전으로 업그레이드
RUN pip install --upgrade pip

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 파일 복사 후 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . /app/

# 애플리케이션 포트 노출
EXPOSE 8002

# 컨테이너 실행 시 마이그레이션 실행 후 Gunicorn으로 애플리케이션 실행
CMD ["sh", "-c", "python manage.py migrate && gunicorn clickthis_django.wsgi:application --bind 0.0.0.0:8002"]
