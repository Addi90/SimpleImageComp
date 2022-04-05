from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

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
            self.text = str(file_path)
            print(file_path)


class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def print_hello_world(self):
        print("Hello world")   
    
    def enterbtn_callback(self,instance):
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
        pass
        


if __name__ == "__main__":
    PSNRApp().run()