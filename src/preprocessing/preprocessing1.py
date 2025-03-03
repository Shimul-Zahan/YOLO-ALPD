import cv2
import numpy as np
import pandas as pd
import seaborn as sns

dirs = r'E:\YOLO-ALPD\Notebook\data\images_labeled'

labeled_data = pd.read_csv('../../Notebook/data/labeled_data.csv')
image_path = dirs + "\\" + labeled_data.iloc[1]['filename']
print(f"Loading image from: {image_path}")
image = cv2.imread(image_path)


xmin=labeled_data.iloc[1]['xmin']
ymin=labeled_data.iloc[1]['ymin']
xmax=labeled_data.iloc[1]['xmax']
ymax=labeled_data.iloc[1]['ymax']

if image is not None:
    # cv2.imshow('image1', image)
    # cv2.namedWindow('example', cv2.WINDOW_NORMAL)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    cv2.rectangle(
        img=image,
        pt1=(xmin, ymin), 
        pt2=(xmax, ymax),
        color=(0, 255, 0),
        thickness=3 # for rthickness
    )
    cv2.imshow('image1', image)
    cv2.namedWindow('example', cv2.WINDOW_NORMAL)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Failed to load image: {image_path}")
