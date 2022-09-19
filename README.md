# Capstone_ElectricCar
---
1st_push (9/19)
1. pytesseract 이용 

    일반 자동차의 번호판은 흰색배경에 검은색글자라서 값을 처리하기 쉬웠지만, 동일한 방법을 전기차번호판(파란배경에 검은색글씨)에 적용하니 번호판 검출이 안됐다.

2. https://github.com/D-HongKim/LicencePlate_Project

    이 깃허브에 자동차 번호판 추출하는 방법이 나와있기는 하나 일반차, 전기차 구분하는 건 따로 만들어야 한다.
    
3.
```python
img_ori = cv2.imread('img2.png')
img = cv2.cvtColor(img_ori, cv2.COLOR_BGR2HSV)
# print(img.shape)
elec_range = cv2.inRange(img, (90, 0, 0), (120, 255, 255)) 
# 파란색을 나타내는 범위인데 모든 영상에서 적용이 되는 것 같지 않음
cv2.imwrite('test1.png', elec_range)
```


    - 문제점 1: 파란색 범위를 직접 지정해서 다른 영상에도 적용이 되는지 모름
    - 문제점 2: 따로 영상을 저장하는 방식
