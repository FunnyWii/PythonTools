import cv2
import numpy as np
import os
import os.path as osp

# For COCO Dataset
color_dict = {
    0.0: (255, 000, 000),
    1.0: (255, 128, 000),
    2.0: (255, 255, 000),
    3.0: (000, 255, 000),
    4.0: (000, 255, 255),
    5.0: (000, 000, 255),
    6.0: (128, 000, 255),
    7.0: (255, 000, 255),
    8.0: (128, 000, 000),
    9.0: (000, 128, 000),
    10.0: (000, 000, 128)
}

color_dict2 = {
    0.0: (0, 250, 148),
    1.0: (255, 48, 48),
    2.0: (255, 255, 000),
    3.0: (0, 250, 148),
    4.0: (255, 48, 48),
    5.0: (255, 255, 000),
    6.0: (0, 250, 148),
    7.0: (255, 48, 48),
    8.0: (255, 255, 000),
    9.0: (000, 000, 255),
}

def run_watch_txts(img_dir, txt_dir, out_dir, color):
    IMAGEDIR = osp.abspath(img_dir)
    LABELDIR = osp.abspath(txt_dir)
    OUTDIR = osp.abspath(out_dir)

    png_names = set([name[:-4] for name in os.listdir(IMAGEDIR) if name.endswith('.jpg')])
    txt_names = set([name[:-4] for name in os.listdir(LABELDIR) if name.endswith('.txt')])
    intersection_names = png_names & txt_names

    for name in png_names:
        image = cv2.imread(osp.join(IMAGEDIR, name+".jpg"))

        if name not in intersection_names:
            cv2.imwrite(osp.join(OUTDIR, name+".jpg"), image)
            continue

        IMG_H, IMG_W, IMG_C = image.shape

        with open(osp.join(LABELDIR, name+".txt"), 'r') as fp:
            lines = fp.readlines()

        for line in lines:
            line = line.strip().split(" ")
            # print(line)
            label = float(line[0])
            cx = IMG_W * float(line[1])
            cy = IMG_H * float(line[2])
            w = IMG_W * float(line[3])
            h = IMG_H * float(line[4])
            angle = 0
            rect = ((cx, cy), (w, h), (angle))
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(image, [box], 0, color_dict[label][::-1], 2)
        #     print(cx)
        #     print(cy)    
            if label == 0.0:
                    labelText = "Green S"
            elif label == 1.0:
                    labelText = "Red S"
            elif label == 2.0:
                    labelText = "Yellow S"
            elif label == 3.0:
                    labelText = "Green L"
            elif label == 4.0:
                    labelText = "Red L"
            elif label == 5.0:
                    labelText = "Yellow L"
            elif label == 6.0:
                    labelText = "Green R"
            elif label == 7.0:
                    labelText = "Red R"
            elif label == 8.0:
                    labelText = "Yellow R"
            elif label == 9.0:
                    labelText = "UNKNOWN"  

            cv2.putText(image,labelText,(int(cx-50),int(cy+30)),cv2.FONT_ITALIC,0.6, color_dict2[label][::-1], 2)
            # cv2.imshow(" ", image)

        cv2.imwrite(osp.join(OUTDIR, name + ".tif"), image)
        print(name + ", done...")


if __name__ == '__main__':
    BASEDIR = "/home/funnywii/Documents/tsariDataset/"
    
    img_dir = osp.join(BASEDIR, 'copy')
    txt_dir = osp.join(BASEDIR, 'copy_txt')
    out_dir = osp.join(BASEDIR, 'copy_vis')
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    run_watch_txts(img_dir, txt_dir, out_dir, color=(250, 200, 250))
