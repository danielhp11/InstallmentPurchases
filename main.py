from kivy.lang import Builder
from kivymd.app import MDApp

from kivymd.uix.navigationdrawer import (MDNavigationDrawerItem)
from kivy.uix.screenmanager import Screen

class BaseNavigationDrawerItem(MDNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DrawerLabelItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DrawerClickableItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class LikeU(Screen):
    pass

class Nu(Screen):
    pass

class Liverpool(Screen):
    pass




class InstallmentPurchases(MDApp):
    def build(self):
        self.title = "Installment Purchases"
        return Builder.load_file("Screens/main.kv")

    def on_start(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.theme_style = "Light"
        # self.fps_monitor_start()


if __name__ == '__main__':
    InstallmentPurchases().run()