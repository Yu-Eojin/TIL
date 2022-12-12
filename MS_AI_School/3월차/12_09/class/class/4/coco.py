import json
import cv2
import os

import numpy as np

import matplotlib.patches as patches

import matplotlib.pyplot as plt

'''
http://images.cocodataset.org/zips/val2017.zip
http://images.cocodataset.org/annotations/annotations_trainval2017.zip
cocodataset
'''


json_file = '/home/bong08/mskim/infinyx/pythonProject/4/cocodataset/annotations/instances_val2017.json'
img_dir = '/home/bong08/mskim/infinyx/pythonProject/4/cocodataset/val2017'

with open(json_file, 'r') as f:
    annotation_file = json.load(f)

for image in annotation_file['images']:
    img = cv2.imread(os.path.join(img_dir, image['file_name']))
    img_id = image['id']
    annotations = [i for i in annotation_file['annotations'] if i['image_id'] == img_id]
    fig, ax = plt.subplots()

    for annotation in annotations:
        c = (np.random.random((1, 3)) * 0.6 + 0.4).tolist()[0]
        for seg in annotation['segmentation']:
            poly = np.array(seg).reshape((int(len(seg) / 2), 2))

            shp = patches.Polygon(poly, color=c, alpha=0.8)
            ax.add_patch(shp)

        [bbox_x, bbox_y, bbox_w, bbox_h] = annotation['bbox']
        poly = [[bbox_x, bbox_y], [bbox_x, bbox_y + bbox_h], [bbox_x + bbox_w, bbox_y + bbox_h],
                [bbox_x + bbox_w, bbox_y]]
        np_poly = np.array(poly).reshape((4, 2))
        shp = patches.Polygon(np_poly, edgecolor=c, fill=None)
        ax.add_patch(shp)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('scaled')
    plt.show()
