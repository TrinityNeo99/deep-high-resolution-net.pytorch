import pandas as pd
import numpy as np
import cv2


KEYPOINT = {
    0: 'nose',
    1: 'left_eye',
    2: 'right_eye',
    3: 'left_ear',
    4: 'right_ear',
    5: 'left_shoulder',
    6: 'right_shoulder',
    7: 'left_elbow',
    8: 'right_elbow',
    9: 'left_wrist',
    10: 'right_wrist',
    11: 'left_hip',
    12: 'right_hip',
    13: 'left_knee',
    14: 'right_knee',
    15: 'left_ankle',
    16: 'right_ankle'
}

SKELETON = [
    [0,6],[6,8],[8,10],[6,12],[12,14],[14,16]
]

COLORS = [[255, 0, 0], [0, 255, 255], [0,255,255], [127, 127, 127], [0, 0, 255], [0,0,255]]

if __name__ == "__main__":
    df = pd.read_excel("C:/Users/neo/Downloads/正手模型1.xlsx", )
    print(df.head())
    for j, r in df.iterrows():
        img = np.zeros((720,1280,3), np.uint8)
        r = r.to_dict()
        for i in range(len(SKELETON)):
            kpt_a, kpt_b = KEYPOINT[SKELETON[i][0]], KEYPOINT[SKELETON[i][1]]
            x_a, y_a = r[kpt_a + "_x"] + 330, r[kpt_a + "_y"] + 410
            x_b, y_b = r[kpt_b + "_x"] + 330, r[kpt_b + "_y"] + 410
            cv2.circle(img, (int(x_a), int(y_a)), 6, COLORS[i], -1)
            cv2.circle(img, (int(x_b), int(y_b)), 6, COLORS[i], -1)
            cv2.line(img, (int(x_a), int(y_a)), (int(x_b), int(y_b)), COLORS[i], 2)
        cv2.imwrite("../output/img_{}.jpg".format(j+1), img)
        print("finish")

