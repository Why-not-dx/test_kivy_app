import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# goal = make 2 screens to showcase a welcome page then go into a page with images to vote for. 
# Showcase the like count, dislike count, ratio. 

# Widgets are user interface elements that you add to your program to 
# provide some kind of functionality. They may or may not be visible. 
#Examples would be a file browser, buttons, sliders, lists and so on. 
#Widgets receive MotionEvents.

# You use layouts to arrange widgets. 
#It is of course possible to calculate your widgets’ positions yourself, 
# but often it is more convenient to use one of our ready made layouts. 
# Examples would be Grid Layouts or Box Layouts. You can also nest layouts.

class LoginScreen(GridLayout):

	def __init__(self, **kwargs):
		
		# In order to add widgets to the GridLayout object, we override the init method
		# But you then have to call the super to be sure that you keep the functionnlity of the original class
		# They recommand calling **kwargs as they are used internally
		
		
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2
		#Label = widget showcasing something
		self.add_widget(Label(text= "User Name")) 
		#generate the username variable that is a textinput
		#Then create a widget with that variable to place a textinpu box
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text= "Password"))
		self.password = TextInput(multiline=False)
		self.add_widget(self.password)
		self.add_widget(Image(source="bear.jpg"))
		self.button = Button(text="Send everything")
		self.add_widget(self.button)

class RoundAbout(App):

	def build(self):
		return LoginScreen()

if __name__ == "__main__":
	test = RoundAbout()
	test.run()