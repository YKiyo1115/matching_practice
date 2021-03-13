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

#メイン処理
class MyRoot(FloatLayout):
    pass

MatchingPracticeApp().run()#①処理の開始