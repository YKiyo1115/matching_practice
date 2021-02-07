from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Label.font_size = 32#importしたLabelのフォントサイズを指定(ここで定義するとpyファイル内共通になる。インスタンス化したlabelに定義すればそのインスタンスにのみ適用。)

class SampleApp(App):
    def build(self):
        return MyRoot()#②MyRootクラスのインスタンス化処理の結果をそのままリターン

class IncreaseButton(Button):
    def on_press(self):#④
        lbl = self.parent.parent.lbl#調べても出てこないからよくわからんが、呼び出し元のMyRootクラス内の変数lblを当クラス内でも使用するための代入かと思われる。
        lbl.value = lbl.value + 1
        lbl.text = str(lbl.value)

class ResetButton(Button):
    def on_press(self):#⑤
        lbl = self.parent.parent.lbl#調べても出てこないからよくわからんが、呼び出し元のMyRootクラス内の変数lblを当クラス内でも使用するための代入かと思われる。
        lbl.value = 0
        lbl.text = str(lbl.value)

class MyRoot(BoxLayout):
    orientation = 'horizontal'
    def __init__(self,**kwargs):#③MyRootクラスのイニシャライズ関数に処理を定義
        super(MyRoot,self).__init__(**kwargs)#kivyライブラリのBoxLayoutのイニシャライズ関数を呼び出し。
        self.lbl = Label(text='0')
        self.lbl.value = 0
        self.add_widget(self.lbl)
        box = BoxLayout(orientation='vertical')
        btn1 = IncreaseButton(text = 'Increasehoge')#インクリメント機能を持つボタンをインスタンス化
        btn2 = ResetButton(text = 'Reset')#リセット機能を持つボタンをインスタンス化
        box.add_widget(btn1)#④インクリメント機能を持つボタンをBoxLayoutのwidgetに追加する。
        box.add_widget(btn2)#⑤リセット機能を持つボタンをBoxLayoutのwidgetに追加する。
        self.add_widget(box)

SampleApp().run()#①処理の開始