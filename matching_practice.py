from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder


Label.font_size = 32#importしたLabelのフォントサイズを指定(ここで定義するとpyファイル内共通になる。インスタンス化したlabelに定義すればそのインスタンスにのみ適用。)

class MatchingPracticeApp(App):
    def build(self):
        return MyRoot()#②MyRootクラスのインスタンス化処理の結果をそのままリターン

#★ログイン画面
class LoginLayout(FloatLayout):
    def __init__(self,**kwargs):#③MyRootクラスのイニシャライズ関数(呼び出されると同時に処理が走る)に処理を定義
        super(LoginLayout,self).__init__(**kwargs)#kivyライブラリのBoxLayoutのイニシャライズ関数を呼び出し。
        userLayout = UserLayout(size_hint = [0.5,0.1] , pos_hint={'center_x':0.5, 'top':0.9})
        passLayout = PassLayout(size_hint = [0.5,0.1] , pos_hint={'center_x':0.5, 'top':0.8})
        self.add_widget(userLayout)
        self.add_widget(passLayout)
        loginButton = LoginButton(text = 'Login',size_hint = [0.4,0.1] , pos_hint={'center_x':0.5, 'top':0.4})
        newMemberButton = NewMemberButton(text = 'New member!!',size_hint = [0.4,0.1] , pos_hint={'center_x':0.5, 'top':0.3})
        self.add_widget(loginButton)
        self.add_widget(newMemberButton)

#ログインボタン
class LoginButton(Button):
    def on_press(self):
        pass

#新規会員登録ボタン
class NewMemberButton(Button):
    def on_press(self):
        pass

#ログイン画面(ユーザー入力部)
class UserLayout(BoxLayout):
    def __init__(self,**kwargs):#③MyRootクラスのイニシャライズ関数(呼び出されると同時に処理が走る)に処理を定義
        super(UserLayout,self).__init__(**kwargs)#kivyライブラリのBoxLayoutのイニシャライズ関数を呼び出し。
        orientation = 'horizontal'
        userLabel = Label(text='user:  ',size_hint_x=1,)
        userInput = UserInput(text = 'user',size_hint_x=3)
        self.add_widget(userLabel)
        self.add_widget(userInput)

class UserInput(TextInput):
    pass
#ログイン画面(PASS入力部)
class PassLayout(BoxLayout):
    def __init__(self,**kwargs):#③MyRootクラスのイニシャライズ関数(呼び出されると同時に処理が走る)に処理を定義
        super(PassLayout,self).__init__(**kwargs)#kivyライブラリのBoxLayoutのイニシャライズ関数を呼び出し。
        orientation = 'horizontal'
        passLabel = Label(text='pass:  ',size_hint_x=1)
        passInput = PassInput(text = 'password',size_hint_x=3)
        self.add_widget(passLabel)
        self.add_widget(passInput)

class PassInput(TextInput):
    pass

#メイン処理
class MyRoot(FloatLayout):
    def __init__(self,**kwargs):#③MyRootクラスのイニシャライズ関数(呼び出されると同時に処理が走る)に処理を定義
        super(MyRoot,self).__init__(**kwargs)#kivyライブラリのBoxLayoutのイニシャライズ関数を呼び出し。
        Builder.load_file('matching.kv')
        #ログイン画面のレイアウトを初期表示
        loginLayout = LoginLayout();
        self.add_widget(loginLayout)

MatchingPracticeApp().run()#①処理の開始