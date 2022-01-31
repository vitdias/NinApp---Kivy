# Import libraries
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
import hashlib
import sqlite3

#Tela de Menu
class MenuScreen(Screen):
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
        pass

# Tela de login do usuário
class LoginScreen(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.title = "Login on NinaData"
        self.db = sqlite3.connect("acessos.db")
        self.db.execute("CREATE TABLE IF NOT EXISTS tb_usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, userLogin TEXT, userEmail TEXT, userPW TEXT, userSecretQuestion TEXT, userSecretAnswer TEXT)")
        Window.size = (300, 600)
        return Builder.load_file('gui.kv')
    
    def login(self):
        self.root.ids.welcome_label.text = f'Logged as {self.root.ids.user.text}'
        
    def register(self):
        pass
    
LoginScreen().run()