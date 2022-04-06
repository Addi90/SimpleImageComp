import cv2




def calc_psnr(orig_img_path :str,comp_img_path:str):
    orig_img = cv2.imread(orig_img_path)
    comp_img = cv2.imread(comp_img_path)
    return cv2.PSNR(orig_img,comp_img)