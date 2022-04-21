import cv2
import imutils
import os.path
from skimage import metrics


def calc_psnr(orig_img_path :str,comp_img_path:str,callback_func):

    if(os.path.exists(orig_img_path) and os.path.exists(comp_img_path)):
        callback_func('Thread PSNR start: calculating...')
        orig_img = cv2.imread(orig_img_path)
        comp_img = cv2.imread(comp_img_path)
        #TODO: Compare x,y size of images

        score = cv2.PSNR(orig_img,comp_img)
        print(f'Thread PSNR: {round(score,10):.10f}')
        callback_func(str(f'Thread PSNR: {round(score,5):.5f}') + ' dB')
    else: 
        callback_func(-1)


def calc_ssim(orig_img_path :str,comp_img_path:str,callback_func):
    if(os.path.exists(orig_img_path) and os.path.exists(comp_img_path)):
        callback_func('Thread SSIM start: calculating...')
        orig_img = cv2.imread(orig_img_path)
        comp_img = cv2.imread(comp_img_path)
        #TODO: Compare x,y size of images

        orig_img_gray = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
        comp_img_gray = cv2.cvtColor(comp_img, cv2.COLOR_BGR2GRAY)

        score = metrics.structural_similarity(orig_img_gray,comp_img_gray,full=False)
        print(f'Thread SSIM: {round(score,10):.10f}')
        callback_func(f'{round(score,10):.10f}')
    else: 
        callback_func(-1)


def calc_mse(orig_img_path :str,comp_img_path:str,callback_func):

    if(os.path.exists(orig_img_path) and os.path.exists(comp_img_path)):
        callback_func('Thread MSE start: calculating...')
        orig_img = cv2.imread(orig_img_path)
        comp_img = cv2.imread(comp_img_path)
        #TODO: Compare x,y size of images

        score = metrics.mean_squared_error(orig_img,comp_img)
        print(f'Thread MSE: {round(score,10):.10f}')
        callback_func(f'Thread MSE: {round(score,5):.5f}')
    else: 
        callback_func(-1)