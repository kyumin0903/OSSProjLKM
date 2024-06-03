# [2024-1 오픈소스소프트웨어프로젝트] 8팀 JCL

### 바쁜 현대인들을 위한 뉴스 요약 서비스 "Snap News"

<br>

## 👨🏼‍💻 프로젝트 소개

- 매일 쏟아지는 뉴스 속에서 중요한 내용만을 빠르게 제공해줍니다.
- AI 기술을 활용한 정확한 요약으로, 매일 필요한 정보를 간편하게 받을 수 있습니다.
  <br> </br>

## 🧑‍🤝‍🧑 팀 구성

<div align=center>
    
| <img src="https://avatars.githubusercontent.com/u/162105423?v=4" width="160"> | <img src="https://avatars.githubusercontent.com/u/162091845?v=4" width="160"> | <img src="https://avatars.githubusercontent.com/u/43908014?v=4" width="160"> |
| :---------------------------------------------------------------------------: | :---------------------------------------------------------------------------: | :--------------------------------------------------------------------------: |
|                    [이규민](https://github.com/kyumin0903)                    |                   [정영균](https://github.com/okchangheeok)                   |                    [최지안](https://github.com/choijian)                     |
|                               팀장, 프론트엔드                                |                                    백엔드                                     |                                디자인, 인프라                                |
</div>
<br>

## 📜 커밋 규칙

- feat : 새로운 기능에 대한 커밋
- fix : 버그 수정에 대한 커밋
- build : 빌드 관련 파일 수정에 대한 커밋
- chore : 그 외 자잘한 수정에 대한 커밋
- docs : 문서 수정에 대한 커밋
- style : 코드 스타일 혹은 포맷 등에 관한 커밋
- refactor : 코드 리팩토링에 대한 커밋

<br>
 
## 🎨 시스템 다이어그램
<img src="Doc\images\블록다이어그램.png" width="600" height="400"> <br>

## 📱 화면 설계

<div style="display: flex; justify-content: center; gap: 40px;">
  <img src="Doc/images/onboarding.png" width="200" height="400">
  <img src="Doc/images/signup.png" width="200" height="400">
  <img src="Doc/images/main.png" width="200" height="400">
</div>

<br>
    
## 🐱 기존 시스템과의 차별점 및 개선점

네이버 뉴스와 비교

| 기존                                 | 우리 프로젝트                   |
| ------------------------------------ | ------------------------------- |
| 기사별로 요약하기 버튼 클릭해서 요약 | 실시간 요약된 헤드라인 기사 5개 |
| 북마크 기능 X                        | 북마크 기능 O                   |

<br>

참고 프로젝트와 비교

| 기존                                 | 우리 프로젝트                 |
| ------------------------------------ | ----------------------------- |
| 기사별로 요약하기 버튼 클릭해서 요약 | 실시간 헤드라인 기사 5개 요약 |
| 북마크 기능 X                        | 북마크 기능 O                 |
| 카테고리 구분 X                      | 카테고리 구분 O               |

<br>
<div>
    
1. **메인페이지 변경**: 뉴스 기사 하나의 요약을 위해 직접 요약 버튼을 누르는 것이 아니라 메인 페이지에서 카테고리별 **헤드라인 기사 5개**를 **요약해서 한 눈에 확인**할 수 있다. 사용자는 주요 뉴스를 **빠르게 파악**할 수 있어 편리하다.
2. **로그인/ 회원가입 기능 추가**: 사용자가 북마크 저장과 같은 **개인화된 기능을 이용**하기 위해 로그인 및 회원가입 기능을 추가한다.
3. **북마크 기능 추가**: 요약한 뉴스 중 사용자가 **관심 있는 기사를 북마크**하여 나중에 다시 확인할 수 있도록 하는 기능이다. 사용자는 **북마크한 기사들**을 한 곳에 모아서 **효율적으로 관리**할 수 있다.
   
</div>
<br>

## 기술 스택

### Collaboration

<div>
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=GitHub&logoColor=white"/> 
  <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=Notion&logoColor=white">
    <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white">
    <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white"/>
</div> <br>

### Backend

<div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/> 
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=Django&logoColor=white">
    <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
    <img src="https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"/>

</div> <br>

### Frontend

<div>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"/>
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white"/>
</div> <br>

### Datebase

<div>
    <img src="https://img.shields.io/badge/amazonrds-527FFF?style=for-the-badge&logo=AmazonRDS&logoColor=white">   
      <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">
</div>  <br>

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
<br>

## 일정 관리

<img src="Doc\images\gantt.png" width="1000" height="400">
<br>

## 이슈 관리

<img src="Doc\images\이슈관리1.png" width="700" height="300">  
https://github.com/CSID-DGU/2024-1-OSSProj-JCL-08/issues

<br></br>

## 기대효과 및 활용방안

### ⌛ **효율적인 시간 활용**

현대인들의 바쁜 일상 속에서 뉴스를 신속하게 습득할 수 있는 기회를 제공할 것으로 기대된다. 출퇴근 시간이나 짧은 여유 시간에도 뉴스를 확인할 수 있어, 개인의 시간 활용에 대한 효율성이 증가할 것으로 보인다.

### 😊 **인지적 부담 완화**

긴 글을 읽는 것에 대한 부담을 감소시킴으로써, 뉴스를 소비하는 데 있어 인지적 부담이 덜어져 사용자들이 더욱 적극적으로 정보를 습득할 수 있게 될 것이다.

### 📒 **효율적인 정보 관리**

마이페이지와 스크랩 기능 제공으로, 사용자는 원하는 요약된 뉴스를 모아서 관리할 수 있다.
