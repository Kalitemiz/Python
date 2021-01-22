from kivy.app import App
from kivy.uix.button import Button

class Testapp(App):
	def build(self):
		return Button(text='Selamün Aleyküm')
		

testApp().run()
