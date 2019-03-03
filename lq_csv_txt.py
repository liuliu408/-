import os
train_file = open('VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
test_file = open('VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
for _, _, train_files in os.walk('data/train_dataset'):
    continue
for _, _, test_files in os.walk('data/test_dataset'):
    continue
for file in train_files:
    train_file.write(file.split('.')[0] + '\n')

for file in test_files:
    test_file.write(file.split('.')[0] + '\n')
