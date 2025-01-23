import itertools

class Menu:
    def __init__(self):
        self.menu_list = [
            ('お刺身', 'おかず', 1300)
            , ('焼き魚', 'おかず', 1200)
            , ('焼肉', 'メイン', 1500)
            , ('寿司', 'メイン', 2000)
            , ('パスタ', 'メイン', 1800)
            , ('サラダ', 'サイド', 600)
            , ('スープ', 'サイド', 400)
        ]
    
    def main_only(self):
        main_only = [menu for menu in self.menu_list if menu[1] == 'メイン']
        print(main_only)
        print('----------end----------')
    
    def main_and_side(self):
        main_and_side = [(menu_a[0], menu_b[0]) for menu_a in self.menu_list for menu_b in self.menu_list if menu_a != menu_b and menu_a[1] == 'メイン' and menu_b[1] == 'サイド'] 
        print(main_and_side)
        print('----------end----------')

    def select_two_menu(self):
        # 単純な取得
        menu_set_iter = ((menu_a[0], menu_b[0]) for menu_a in self.menu_list for menu_b in self.menu_list if menu_a[0] != menu_b[0]) # ()で囲むとジェネレーター、[]で囲むとリストだお
        menu_set = list(menu_set_iter)
        print(menu_set)
        print('----------end----------')

        # モジュールを使う
        menu_set_iter = itertools.permutations([v[0] for v in self.menu_list], 2)
        menu_set = list(menu_set_iter)
        print(menu_set)
        print('----------end----------')
    
    def max_set(self):
        all_set = itertools.permutations(self.menu_list, 2)
        set_price = [(menu_a[0], menu_b[0], menu_a[2] + menu_b[2]) for (menu_a, menu_b) in all_set]
        max_set = ('', '', 0)
        for set in set_price:
            if max_set[2] < set[2]:
                max_set = set
        print(max_set)



    
if __name__ == "__main__":
    menu = Menu()
    menu.main_only()
    menu.select_two_menu()
    menu.main_and_side()
    menu.max_set()