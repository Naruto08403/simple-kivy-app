from kivy.app import App


class TestApp(App):
    def build(self):
        return Label(text= "It Works")


if __name__ == "__main__":
    TestApp().run()