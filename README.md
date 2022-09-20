# Capstone_ElectricCar

|주차| 계획 | 세부사항|
|-----|---|---|
|~9/16| .| .|
|~9/23| .| .|
|~9/30| .| .|

---
#Image Objection
- 전기차 구별
---
- 충전시간 초과
---
- 충전구역 주변 물체 확인


9/20일
https://datacook.tistory.com/60 여기서 mask 예시 해본 다음에 roboflow 사이트에서 hardhat데이터 얻어서 실습해봄(mkdir로 폴더는 만들어 졌는데 그 안으로 데이터 저장이 안돼서 수작업으로 넣었음)

->%cd /content
!curl -L "dataset 링크 붙여넣기" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
%mkdir dataset/
%mv test dataset/
%mv train dataset/
%mv valid dataset/
%mv data.yaml dataset/
이런식으로 옮겨줘도 될듯


 코드 문제 예측한 사진 저장을 exp_num 돌릴때마다 num이 커져서 확인할려면 detect_img_path를 계속 수정해 줘야함

라벨은 ['head', 'helmet', 'person'] 3갠데 결과가 helmat에 대해서만 나옴 head나 person도 나오게 해봐야 함
