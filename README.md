## Django Tutorial 4 Project

## **프로젝트 소개**

리뷰와 블로그 기능을 구현한 Django 웹 애플리케이션입니다. 

## **주요 기능**

### **리뷰 기능**

- 리뷰 작성/조회
- 리뷰 목록 페이지
- 리뷰 상세 페이지

### **블로그 기능**

- 카테고리 관리
- 게시글 작성/조회
- 카테고리별 게시글 필터링

### **기술 스택**

- Django 5.1.3
- PostgreSQL
- Bootstrap 5
- Google Fonts (Noto Sans KR)

### **데이터베이스 설정**
```sql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testdb_zmo',
    }
}
```

### **설치 및 실행**

1. 저장소 클론

```bash 
git clone https://github.com/2zm00/django_tut4_project.git
cd django_tut4_project
```


2. 가상환경 설정
```bash 
conda create -n dj python=3.11
conda activate dj
```
3. 의존성 설치

```bash 
pip install django psycopg2
```
4. 데이터베이스 마이그레이션

```bash 
python manage.py makemigrations
python manage.py migrate
```
5. 서버 실행

```bash 
python manage.py runserver
```

### **프로젝트 구조**

```text 
django_tut4_project/
├── blog/
│   ├── templates/
│   │   └── blog/
│   │       ├── blog_base.html
│   │       ├── index.html
│   │       ├── category_list.html
│   │       └── category_form.html
├── review/
│   ├── templates/
│   │   └── review/
│   │       ├── index.html
│   │       ├── review_create.html
│   │       └── review_detail.html
└── templates/
    ├── base.html
    └── home.html```
    