# coin_predict
황승원 교수님 텍스트 프로젝트( 정성호, 함석환, 오영택)

### Roadmap

1) 데이터 수집(due: 12/4)
- 네이버 기사(검색어: 가상화폐, 비트코인)
  - 데이터 스킴: (제목, 본문, 날짜(분단위까지))
  - 파일은 csv나 python 객체를 pickle 로 저장
  - 긁는법: 네이버 api or 브라우저 크롤링(selenium)
- 비트코인 시세
  - 24h거래이므로 특정시간(0:00)을 closed 로 정하여 종가 산정
  - bitflex, polonix등 사이트를 찾아 가져오기.

2) 데이터 클렌징(due: 12/8)
- 단어를 다양한 Vectorization 방법(TF-IDF, Doc2Vec ...)사용하여 벡터화.
  - gensim등 파이썬 프레임워크가 있음.

3) 데이터 분석(due: ~ end)
- **TODO:** 시계열 데이터를 이용하여 머신러닝 후 모델 만드는 방법 조사
- 모델은 python의 pickle로 저장, 

4) 모델 검증(due: ~ end)
- 알고리즘 모델 테스트 프레임워크인 zipline을 이용.

### Role

- 함석환: 데이터수집(네이버 기사)
- 오영택: 데이터수집(비트코인 시세), 데이터 분석 방법 조사, 모델 검증
- 정성호: 데이터 클렌징, 데이터 분석 방법 조사.