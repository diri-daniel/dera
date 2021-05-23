from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


class WindowManager(ScreenManager):
    def stop(self):
        self.root_window.stop()
    pass


class LoadingScreen(Screen):
    i = 0

    def switch(self, *args):
        self.parent.current = "menu"

    def pbt(self, *args):
        self.i += 1
        self.ids.pb.value = self.i

    def on_enter(self, *args):
        # called when this Screen is displayed
        Clock.schedule_once(self.pbt, 1)
        Clock.schedule_once(self.pbt, 2)
        Clock.schedule_once(self.pbt, 3)
        Clock.schedule_once(self.pbt, 4)
        Clock.schedule_once(self.pbt, 5)
        Clock.schedule_once(self.switch, 7)


class MenuScreen(Screen):
    def close(self):
        self.get_root_window().close()
        Window.close()
    pass


class Ilay1(Screen):
    pass


class Ilay2(Screen):
    pass


class Ilay3(Screen):
    pass


class Ilay4(Screen):
    pass


class Ilay5(Screen):
    pass


class Ilay6(Screen):
    pass


class Ilay7(Screen):
    pass


class Ilay8(Screen):
    pass


class Ilay9(Screen):
    pass


class Ilay10(Screen):
    pass


class Ilay11(Screen):
    pass


class Ilay12(Screen):
    pass


class Ilay13(Screen):
    pass


class Ilay14(Screen):
    pass


class Ilay15(Screen):
    pass


class Ilay16(Screen):
    pass


class Ilay17(Screen):
    pass


class Ilay18(Screen):
    pass


class Iwytk1(Screen):
    pass


class Iwytk2(Screen):
    pass


class Iwytk3(Screen):
    pass


class Iwytk4(Screen):
    pass


class Iwytk5(Screen):
    pass


class Iwytk6(Screen):
    pass


class Iwytk7(Screen):
    pass


class Iwytk8(Screen):
    pass


class Iwytk9(Screen):
    pass


class Iwytk10(Screen):
    pass


class Iwytk11(Screen):
    pass


class Iwytk12(Screen):
    pass


class Iwytk13(Screen):
    pass


class Iwytk14(Screen):
    pass


class Iwytk15(Screen):
    pass


class Iwytk16(Screen):
    pass


class Iwytk17(Screen):
    pass


class Iwytk18(Screen):
    pass


class MenuLayout(BoxLayout):
    pass


class PageLayoutExample(PageLayout):
    pass


class EighteenThings(Screen):
    pass


class BirthdayCard(Screen):
    pass


class MainWidget(Widget):
    pass


class DeraApp(App):
    def build(self):
        Window.clearcolor = (192/255,192/255,192/255,0.5)


    App.icon = r'happy birthday.png'

    pass


DeraApp().run()
