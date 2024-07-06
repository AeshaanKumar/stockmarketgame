from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.properties import ObjectProperty

money1 = 10000
ALREADYSEENSTOCKLIST : bool
costbana = 230
costc2 = 69
costc3 = 3289
stockdict = {"BanaS1": "Bana Stock Company"}


class StartScreen(Screen):
    def __init__(self, **kwargs):
        global alreadyseenstocklist
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.layout.add_widget(Label(text="Welcome to Stock Market Simulation"))

        self.start_button = Button(text="Start Game", size_hint=(None, None), size=(150, 50))
        self.start_button.bind(on_press=self.go_to_stock_list)
        self.start_button.bind(on_press=self.go_to_stockgame)
        self.layout.add_widget(self.start_button)
        self.layout.bind(size=self.on_layout_size)

    def on_layout_size(self, instance, value):
        self.start_button.pos_hint = {'center_x': 0.5, 'center_y': 0.2}

    def go_to_stock_list(self, instance):
        self.manager.current = "stock_list_screen"

    def go_to_stockgame(self, instance):
        self.manager.current = "stock_list"


class StockListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        self.layout.add_widget(Label(text="You will start with 10000 rupees", font_size="35sp", size_hint=(None, None),
                                    size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.7}))
        Clock.schedule_once(self.show_wisdom, 3)
        Clock.schedule_once(self.showbuttontoplay, 6)

    def go_to_stockgame(self, instance):
        global money1
        money1 = 10000
        self.manager.current = "stock_list"

    def show_wisdom(self, dt):
        self.layout.add_widget(Label(text="Spend it wisely.", font_size="35sp", color=(0, 0, 1, 1), size_hint=(None, None),
                                     size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.6}))

    def showbuttontoplay(self, dt):
        self.start_button = Button(text="Play!", font_size="50sp", size_hint=(None, None), size=(300, 150),
                                   pos_hint={'center_x': 0.5, 'y': 0})
        self.start_button.bind(on_press=self.go_to_stockgame)
        self.layout.add_widget(self.start_button)


class Investstocklist(Screen):
    content_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        top_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(200))
        top_layout.add_widget(Label(text=f"Money: {money1}", font_name="Verdana", font_size=dp(21)))
        top_layout.add_widget(Label(text="Stocks", font_name="Verdana", font_size=dp(41)))

        self.content_layout = GridLayout(cols=1, size_hint_y=None, spacing=dp(10))

        self.add_stock_button("Bana Company", "₹" + str(costbana))
        self.add_stock_button("Bsdadana Company", "₹" + str(costc2))
        self.add_stock_button("Badffna Company", "₹" + str(costc3))

        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(top_layout)
        scroll_view = ScrollView()
        scroll_view.add_widget(self.content_layout)
        main_layout.add_widget(scroll_view)

        self.add_widget(main_layout)

    def add_stock_button(self, stock_name, text1):
        stock_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50))
        small_label = Label(text=text1, size_hint_x=None, width=dp(150), height=dp(50), color=(0, 1, 1, 1))
        stock_button = Button(text=stock_name, font_size="35sp", size_hint_x=0.8)
        stock_button.bind(on_press=self.go_to_stock_list)
        stock_layout.add_widget(small_label)
        stock_layout.add_widget(stock_button)
        self.content_layout.add_widget(stock_layout)

    def go_to_stock_list(self, instance):
        self.manager.current = "s1banascreen"

    def go_to_buyscreen(self, instance, stock):
        self.manager.current = "buythescreen"


class StockMarketGame(App):
    def build(self):
        sm = ScreenManager()
        stock_listthing = Investstocklist(name="stock_list")
        start_screen = StartScreen(name="start")
        stock_list_screen = StockListScreen(name="stock_list_screen")
        s1banascreen = BanaStock(name="s1banascreen")
        buythescreen = BuyScreen(name="buythescreen", stock="BanaS1")
        sm.add_widget(start_screen)
        sm.add_widget(stock_list_screen)
        sm.add_widget(stock_listthing)
        sm.add_widget(s1banascreen)
        sm.add_widget(buythescreen)
        return sm


class BanaStock(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        k = "BanaS1"
        self.banatitle = Label(text='Bana Stock Company', font_size='45sp', size_hint=(None, None), size=(300, 50),
                               pos_hint={'center_x': 0.5, 'top': 0.95})
        self.banatitlemoney = Label(text='₹' + str(costbana), font_size='45sp', size_hint=(None, None), size=(300, 50),
                                    pos_hint={'center_x': 0.5, 'top': 0.8}, color=(0, 1, 0, 1))
        self.buybuttonbana = Button(text="Buy Stock", font_size="30sp", size_hint=(None, None), size=(200, 50),
                                    pos_hint={'center_x': 0.5, 'top': 0.2})
        layout.add_widget(self.banatitle)
        layout.add_widget(self.banatitlemoney)
        layout.add_widget(self.buybuttonbana)
        self.add_widget(layout)
        self.buybuttonbana.bind(on_press=lambda instance: self.go_to_buyscreen(k))

    def go_to_buyscreen(self, stock):
        self.manager.current = "buythescreen"
        self.manager.get_screen("buythescreen").set_stock(stock)


class BuyScreen(Screen):
    def __init__(self, stock="", **kwargs):
        super().__init__(**kwargs)
        self.stock = stock
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        self.buytitle = Label(font_size="45sp", pos_hint={'center_x': 0.5, 'top': 0.3}, color=(1, 0, 0, 1))
        self.buytitlenumber = Label(text="0", font_size="45sp", pos_hint={'center_x': 0.5, 'top': 0.5}, color=(1, 0, 1, 1))
        self.buybutton = Button(text="Buy Stock", font_size="30sp", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'top': 0.8})
        self.layout.add_widget(self.buytitle)
        self.layout.add_widget(self.buytitlenumber)
        self.layout.add_widget(self.buybutton)

    def on_enter(self):
        titlestock = stockdict.get(self.stock)
        self.buytitle.text = f"How many stocks of {titlestock} do you want?"

    def set_stock(self, stock):
        self.stock = stock


if __name__ == "__main__":
    StockMarketGame().run()
