Yolo_mark_inverse_cropper
=========================

[English]
---------------

It was developed to recycle some learning data from the label portion of the dataset tagged for YOLO mark.

When image tagging is carried out with the Yolo mark, the coordinate value of the bounding box is as shown below.

Normalized and saved as a text file.


[ex]

0 0.400391 0.305556 0.357031 0.605556

2 0.523047 0.436806 0.042969 0.076389

3 0.246484 0.506944 0.044531 0.086111

1 0.375000 0.390972 0.050000 0.118056


This program reverses this coordinate value and uses opencv to cut only the tagged part of the original image.


*Input folder with jpg image and yolomark tagged txt file is created in output folder.

*The generated file is in the following format:

[Class number]_[Image file name]_[createnum].jpg


Thanks.

*2020.01.05
some bug is fixed 
1. in One Class id, Redundant Tagged Image is now saved as separate file properly 
2. Adds a code that creates a file only if there is a pair of text and image files





[한국어]
---------------

필요에 의해서 개발하게 되었습니다.

Yolo mark로 이미지 태깅을 진행하면, 아래와 같이 boundingbox의 좌표값이

정규화되어 텍스트 파일로 저장되게 됩니다.


[ex]

0 0.400391 0.305556 0.357031 0.605556

2 0.523047 0.436806 0.042969 0.076389

3 0.246484 0.506944 0.044531 0.086111

1 0.375000 0.390972 0.050000 0.118056


이 좌표값을 역변환하여 opencv를 이용해 원본 이미지에서 태깅한 부분만을 잘라내는 프로그램입니다.

YOLO mark 용으로 태깅된 데이터셋의 label 부분을 일부 학습 데이터로 재활용하기 위해서 개발되었습니다.

*input 폴더에 jpg이미지와 yolomark로 태깅한 txt파일을 함께넣고 실행하면 output폴더에 생성됩니다.

*생성된 파일의 형식은 아래와 같습니다.

[클래스번호][이미지파일이름].jpg

