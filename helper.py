from paddleocr import PaddleOCR

def get_model(lang):
    if lang == 'English':
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        return ocr, 'simfang.ttf'
    elif lang == 'Chinese':
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        return ocr, 'simfang.ttf'
    elif lang == 'Japan':
        ocr = PaddleOCR(use_angle_cls=True, lang='jp')
        return ocr, 'japan.ttc'
    elif lang == 'Korean':
        ocr = PaddleOCR(use_angle_cls=True, lang='kr')
        return ocr, 'korean.ttf'