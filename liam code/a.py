class Portfolio:
  def __init__(self):
      self.stocks = []

  def buy_stock(self, stock):
      self.stocks.append(stock)

  def sell_stock(self, stock):
      self.stocks.remove(stock)

class Stock:
  def __init__(self, quantity, buy_price):
    self.quantity = quantity
    self.average_buy_price = buy_price
    self.current_price = buy_price
    self.history = []

  def add_quantity(self, quantity, buy_price):
    total_cost = self.average_buy_price * self.quantity + buy_price * quantity
    self.quantity += quantity
    self.average_buy_price = total_cost / self.quantity

  def remove_quantity(self, quantity):
    if self.quantity >= quantity:
      self.quantity -= quantity

  def __str__(self):
    return f"{self.quantity}  {self.name} shares at {self.average_buy_price}"

apple = Stock(100, 3945)
google = Stock(200, 3244)
microsoft = Stock(50, 8129)
amazon = Stock(300, 3373)