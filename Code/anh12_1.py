from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='japan') # need to run only once to download and load model into memory
img_path = 'D:\\Downloads\\scene\\SceneTrialTest\\ryoungt_05.08.2002\\aPICT0034.JPG'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)


# draw result
from PIL import Image
import PIL
print(PIL.__version__)
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='D:\\Downloads\\ppocr_img\\fonts\\simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
