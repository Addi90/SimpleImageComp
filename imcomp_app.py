from sys import orig_argv
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

import threading
import os.path
import imcomp_funs

fpaths = []

class FileDropArea(Label):

    # Add every FileDropArea to a list in main app, so that main app can call 
    # all on_filedrop functions of all instances of FileDropArea. 

    # In on_filedrop, check Mouse position on a file drop to find out which 
    # instance a file was dropped on
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        app = App.get_running_app()
        app.file_drops.append(self.on_filedrop)


    def on_filedrop(self,widget,file_path):
        if self.collide_point(*Window.mouse_pos):
            app = App.get_running_app()
            fpath = os.path.abspath(file_path)
            self.text = fpath.decode('utf-8')
            fpaths.append(self.text)
            img = Image(source= self.text)
            self.parent.add_widget(img)



class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enterbtn_pressed(self,instance):
        self.background_color=(1,0,0,1)
        app = App.get_running_app()
        psnr_thread = threading.Thread(
            target=imcomp_funs.calc_psnr,
            args=(self.ids['orig_fda'].text,self.ids['comp_fda'].text,self.set_psnr_lb)
            )
        ssim_thread = threading.Thread(
            target=imcomp_funs.calc_ssim, 
            args=(self.ids['orig_fda'].text,self.ids['comp_fda'].text,self.set_ssim_lb)
            )
        psnr_thread.start()
        ssim_thread.start()
     
    def set_psnr_lb(self, psnr):
        print(psnr)
        if(psnr != -1):
            self.ids['psnr_lb'].text = 'Peak Signal-Noise Ratio (PSNR): ' + str(psnr) + ' dB'
        else:
            self.ids['psnr_lb'].text = 'Peak Signal-Noise Ratio (PSNR): ERROR'

    def set_ssim_lb(self, ssim):
        print(ssim)
        if(ssim != -1):
            self.ids['ssim_lb'].text = 'Structural Similarity Index (SSIM): ' + str(ssim)
        else:
            self.ids['ssim_lb'].text = 'Structural Similarity Index (SSIM): ERROR'
        


class PSNRApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_drops =[]

    def build(self):

        self.window = AppLayout()
        Window.bind(on_dropfile=self.handle_filedrop)

        return self.window

    def handle_filedrop(self,*args):
        for f in self.file_drops:
            f(*args)
        
    def get_img_paths(self):
        return self.orig_path,self.comp_path
        


if __name__ == "__main__":
    PSNRApp().run()