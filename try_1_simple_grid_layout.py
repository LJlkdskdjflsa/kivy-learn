import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # init all keyword
    def __init__(self, **kwargs):
        # call grid layout constructot
        super(MyGridLayout, self).__init__(**kwargs)

        #set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 160
        self.col_force_default = True
        self.col_default_width = 100

        # create a second gridlayout
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height = 40,
            col_force_default = True,
            col_default_width = 100,
        )
        self.top_grid.cols = 2

        #add widget
        self.top_grid.add_widget(Label(text="Title"))
        #add input box
        self.title = TextInput(multiline=False)
        self.top_grid.add_widget(self.title)

        self.top_grid.add_widget(Label(text="Description"))
        self.description = TextInput(multiline=False)
        self.top_grid.add_widget(self.description)

        self.top_grid.add_widget(Label(text="Category"))
        self.category = TextInput(multiline=False)
        self.top_grid.add_widget(self.category)

        self.top_grid.add_widget(Label(text="Tags"))
        self.tags = TextInput(multiline=True)
        self.top_grid.add_widget(self.tags)

        self.top_grid.add_widget(Label(text="Estimated time"))
        self.estimated_time = TextInput(multiline=False)
        self.top_grid.add_widget(self.estimated_time)

        # add new top_grid to app
        self.add_widget(self.top_grid)

        # Create button
        self.submit = Button(
            text="Submit",
            font_size=32,
            size_hint_x=None,
            size_hint_y = None,
            width=200,
            height=50,
        )
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)


    def press(self, instance):
        title = self.title.text
        description = self.description.text
        category = self.category.text
        tags = self.tags.text
        estimated_time = self.estimated_time.text

        print(title)
        print(description)
        print(category)
        print(tags)
        print(estimated_time)

        # Print to screen
        #self.add_widget(Label(text=title))

        #clear text
        self.title.text = ""
        self.description.text = ""
        self.category.text = ""
        self.tags.text = ""
        self.estimated_time.text = ""


class MyApp(App):
    def build(self):
        MyGridLayout().title = "USER_FREE_AS"
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()