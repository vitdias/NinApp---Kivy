# Import libraries
import time
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivy.uix.image import Image
import hashlib
import sqlite3

#Tela de Login
class LoginScreen(Screen):
    pass

class StartScreen(Screen):
    pass

# Tela de App
class AppScreen(Screen):
    pass

# Tela de usuário
class UserScreen(Screen):
    pass

# Tela de alterar senha
class ChangePwScreen(Screen):
    pass

# Tela de cadastro
class RegisterAccScreen(Screen):
    def register_acc(self):
        user=ObjectProperty(None)
        email=ObjectProperty(None)
        conf_email=ObjectProperty(None)
        password=ObjectProperty(None)
        conf_password=ObjectProperty(None)
        # lbl_out=ObjectProperty(None)
        return print(user)
        
    

# Screen Manager
sm = ScreenManager()
sm.add_widget(StartScreen(name="start"))
sm.add_widget(LoginScreen(name="menu"))
sm.add_widget(RegisterAccScreen(name="register"))

# Tela de login do usuário
class NinApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # self.theme_cls.primary_hue = "50" 
        self.title = "Login on NinaData"
        self.db = sqlite3.connect("acessos.db")
        self.db.execute("CREATE TABLE IF NOT EXISTS tb_usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, userLogin TEXT, userEmail TEXT, userPW TEXT, userSecretQuestion TEXT, userSecretAnswer TEXT)")
        self.cursor = self.db.cursor()
        Window.size = (300, 600)
        Window.clearcolor = (255,191,168,1)
        
        screen = Builder.load_file('gui.kv')
        return screen
    
        
NinApp().run()