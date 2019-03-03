from yolo import YOLO
from PIL import Image
from tqdm import *
import pandas as pd

yolo = YOLO()
f = open('VOCdevkit/VOC2007/ImageSets/Main/test.txt')
text = f.read()
text_list = text.split('\n')
del text_list[-1]

jpg_list = []
xmin_list = []
ymin_list = []
xmax_list = []
ymax_list = []

for i in tqdm(text_list):
    image_path = 'VOCdevkit/VOC2007/JPEGImages/' + i + '.jpg'
    image = Image.open(image_path)
    image, label_record, score_record, top_record, left_record, bottom_record, right_record = yolo.detect_image(image)
    xmin_list.extend(left_record)
    ymin_list.extend(top_record)
    xmax_list.extend(right_record)
    ymax_list.extend(bottom_record)
    jpg = [i + '.jpg'] * len(label_record)
    jpg_list.extend(jpg)


result = pd.DataFrame()
name_list = []
data_list = []
for i,value in enumerate(tqdm(jpg_list)):
    name_list.append(value)
    data_list.append(str(xmin_list[i]) + ' ' + str(ymin_list[i]) + ' ' + str(xmax_list[i]) + ' ' + str(ymax_list[i]))

result['id'] = name_list
result['pos'] = data_list
result.to_csv('result/baseline.csv', index=False, header=None)