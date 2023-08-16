# import os
# import pandas as pd
from paddleocr import PaddleOCR

class OCRmodel:

    def __init__(self, use_angle_cls=True, lang='en'):
        self.ocr = PaddleOCR(use_angle_cls=use_angle_cls, lang=lang)  # 모델 객체 생성

    def recognize(self, image_path):
        """
        paddleOCR 모델을 이용해 이미지에서 텍스트를 추출하는 메소드
        """
        self.result = self.ocr.ocr(image_path, cls=True)  # 모델 실행
        self.result_ = self.result[0]
        return self.result_  # 결과값 반환
    
    # def len(self):  # 찾은 문자 개수 출력
    #     return len(self.result_)


