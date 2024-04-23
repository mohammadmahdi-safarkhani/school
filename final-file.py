from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class myapp(App):
    def build(self):
        # make layout 
        layout = BoxLayout(orientation='vertical')

        # make soal textinput 
        textinput1 = TextInput(text='hii',)

        #put soal text in soal variable
        soal = textinput1.text

        # make javab textinput to put javab in it
        textinput2 = TextInput(text=soal,)

        #make button to work
        button = Button(text='click',size_hint=(.2,.1),)

        # put all widgets in layout  
        layout.add_widget(textinput1)
        layout.add_widget(textinput2)
        layout.add_widget(button)

        # return lay out
        return layout
    
        # check and run
if __name__ == "__main__":
    myapp().run()