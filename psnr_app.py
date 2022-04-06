from sys import orig_argv
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

import os.path
import psnr_funs

orig_fpath =''
comp_fpath =''

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
            
            if(self.id == 'orig_fda'):
                orig_fpath = self.text
            elif(self.id == 'comp_fda'):
                comp_fpath = self.text




class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enterbtn_pressed(self,instance):
        app = App.get_running_app()
        psnr_funs.calc_psnr(orig_fpath,comp_fpath)
        print("Clicked")




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