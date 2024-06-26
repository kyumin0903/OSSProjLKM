# A4.3 OSS 프로젝트 제품 구성, 배포 및 운영 자료  

- *자료 내용이 길어지는 경우 별도 문서로 작성하고 링크로 연결*

## 1. 프로젝트 제품 구성

[제품 Overview](https://github.com/CSID-DGU/2024-1-OSSProj-JCL-08/blob/main/Src/Overview.md)
  
## 2. 프로젝트 제품 배포 방법  

- 로컬환경에서 진행

- 백엔드

**1. cd Src -> cd backend**

**2. Create and activate the virtual environment**

```
python -m venv venv
venv\Scripts\activate
```

**3. Install required packages**

```
pip install -r requirements.txt
```

**4. Run the server**

`python manage.py migrate
python manage.py runserver`

- 프론트엔드
1. cd Src -> cd frontend
2. `npm install`
3. `npm start`


## 3. 프로젝트 제품 운영 방법  

1. 프로젝트 제품의 시연을 위한 환경구성 및 운영방법 

2. 시연 시나리오
    1. 회원가입 및 로그인
    2. (정치/경제/사회) 카테고리별 뉴스 요약본 조회 
    3. 북마크 기능: 
       북마크 버튼 클릭-> 북마크 페이지 확인 -> 북마크 삭제

3. [시연영상](https://github.com/CSID-DGU/2024-1-OSSProj-JCL-08/blob/main/Doc/%EC%8B%9C%EC%97%B0%EC%98%81%EC%83%81.mp4)
