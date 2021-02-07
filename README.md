# 📌 MINONE / 부산광역시 온라인 민원 자동분류 사이트 📌

---------------------------------------------------------------------------


## 📌 개발배경 및 목적
현재 부산광역시(16개 구/군)에 민원을 작성할 수 있는 사이트는 두 개가 있는데, 서로 입력 형식이 다를 뿐만 아니라 명확한 카테고리 분류가 없기 때문에 
사용자는 민원 내용을 어느 부서에서 담당하는지와 같은 정보를 빠르게 얻을 수 없다는 단점이 있고,
민원을 처리하는 담당자(19명)는 각 부서의 업무 분장표를 보면서 수작업으로 민원을 분류하고 있어 효율성이 낮다는 단점이 있습니다.
따라서 민원 사이트를 하나로 통합하여, 카테고리 별로 분류 및 처리 할 수 있다면 사용자와 담당자 모두에게 편리할 것이라는 생각을 하였습니다.

온라인 민원을 자동으로 분류해주는 프로그램이 있다면, 불규칙적인 분류시간 및 업무량을 해소 할 수 있을 것 입니다.
현 민원 담당자에게 유선상 문의한 결과, 혼동되는 부서 이름과 복잡한 업무 분장표 떄문에 직접 부서로 전화 문의가 필요하여 민원 처리를 하는 데 최대 2일 정도가 소요된다고 합니다.

MINONE 프로젝트는 부산광역시 민원의 통합적 관리와 업무 간소화, 시간 비용 절약에 목표를 두고 있습니다.

---------------------------------------------------------------------------

## 📌 STACK
### - WEB : Django 
### - DATA CRAWLING & ML MODEL : Python
### - SERVER : AWS
### - DATABASE : sqlite

---------------------------------------------------------------------------

## 📌 INTRODUCE / Web 동작 및 기능 소개
## - DATA CRAWLING : 세올 민원 8만개 + 시청데이터 6만개 수집, 대략 14만개 민원 데이터 수집 🡪 BUT 시청데이터만 가지고 실시
## - DATA PREPROCESSING : 정규표현식과 불용어제거 및 형태소 제거와 같은 토큰화 작업을 거쳐 명사 형태의 단어들로 민원 내용 전처리 (LABEL : 민원 처리 부서)
## - ML MODEL : 관련 논문 참고 후 Random Forest, XGBoost, Naive Bayes, Lstm, Cnn 등 다양한 모델을 이용해보고 가장 정확도 높은 모델 선택 -> XGBoost

### - GET STARTED : 시작 화면

![스크린샷(32)](https://user-images.githubusercontent.com/46439700/107152151-99767980-69a9-11eb-9b38-bc2a2372ddd2.png)

### - INPUT CONTEXT : 일반 민원 사이트와 같이 거주지, 제목, 민원내용 입력

![스크린샷(90)](https://user-images.githubusercontent.com/46439700/107152227-0d188680-69aa-11eb-9548-44b1fbe409c7.png)

### - LOADING : ML을 사용하다보니 결과 값이 출력되는 시간이 걸려서 그동안 로딩 화면을 보여줌

![스크린샷(91)](https://user-images.githubusercontent.com/46439700/107152372-d55e0e80-69aa-11eb-9621-52ca2b3313a1.png)

### - OUTPUT : 사용자가 작성한 민원 내용을 기반으로 ML MODEL 의 예측 결과값을 보여줌: 민원 처리 부서

![스크린샷(101)](https://user-images.githubusercontent.com/46439700/107152751-f6bffa00-69ac-11eb-9670-9387975c10f1.png)

### - EXTRA : 앞의 결과 화면에서 조직도 보기 버튼 클릭 시 나타나는 화면. 민원 처리 부서의 상세 정보를 알고 싶은 경우 해당 아이콘을 선택하면 홈페이지로 이동 

![스크린샷(102)](https://user-images.githubusercontent.com/46439700/107152757-ff183500-69ac-11eb-837f-545521682a75.png)

-----------------------------------------------------------------------------------

## ROLE
### - KANG : DATA CRAWLING, DATA PREPROCESSING, DEVELOP ML MODEL
### - PARK : DATA CRAWLING, DATA PREPROCESSING, DEVELOP ML MODEL, FRONT-END
### - LEE : DATA CRAWLING, DATA PREPROCESSING, DEVELOP ML MODEL, MAKE MATERIALS
### - CHA : DATA CRAWLING, DATA PREPROCESSING, DEVELOP ML MODEL, BACK-END, PR(PRESENTER)
### - CHOI : DATA CRAWLING, DATA PREPROCESSING, DEVELOP ML MODEL, MAKE MATERIALS

--------------------------------------------------------------------------------------

## 📌 REVIEW 
### - ML MODEL : XGBoost
### - DATA LABELING : 16개 구/군 부서를 모아서 각 부서 업무분장표를 확인하여 업무가 유사한 부서들을 GROUPING
###  - 아쉬운 점
###  - ML MODEL 정확도 : 66.71%  🡪 높은 편 X
###  - 23개의 광범위한 민원 처리 부서 (구 별로 부서 이름 및 개수 다름), 현재 공개된 각 라벨 별 민원 숫자의 불균형 
###   🡪 일부 부서(업무)에 민원 밀집도 높음 (ex. 도로교통, 버스, 택시 관련 부서)
###   🡪 소수 라벨에 대한 데이터 보충 Or 분류 체계의 단순화 필요
###  - 형태소 분석기가 분류하지 못하는 단어사전 추가 구축 필요 (ex. 신조어, 민원 관련 단어 등)


