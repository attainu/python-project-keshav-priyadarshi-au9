class Restaurant_C:

    def food_item(self):
        self.menu_C = {'biryani':'100','pizza':'150','pasta':'70','soup':'70','lassi':'40'}

    def update_menu(self, item, price):
        self.menu_C[item]=price
         

# res_C = Restaurant_C()
