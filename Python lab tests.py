#1
class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = dict()

    def add_item(self, item_name, quantity, price):
        if item_name != None and quantity >= 1:
            self.items.update({item_name: quantity})
        if quantity and price >= 1:
            self.total += (quantity * price)

    def remove_item(self, item_name, quantity, price):
        self.total -= (quantity * price)
        try:
            if quantity >= self.items[item_name]:
                self.items.pop(item_name, None)
            self.items[item_name] -= quantity
        except(KeyError, RuntimeError):
            pass


def checkout(self, cash_paid):
        balance = 0
        if cash_paid < self.total:
            return "Cash paid not enough"
        balance = cash_paid - self.total
        return balance



#2
def remove_duplicates(string):
    unique_string = []
    new_string = []
    diff = []
    for x in range(0, len(string)):
        if string[x] not in unique_string:
             unique_string += string[x]
    unique_string = "".join(sorted(unique_string))
    diff = len(string) - len(unique_string)
    new_string.append(unique_string)
    new_string.append(diff)
    new_string = tuple(new_string)
    return new_string


#3
def is_isogram(word):
    if type(word) != str: 
        raise TypeError("Argument should be a string")
    if len(word) < 1:
        return (word, False)
    word = word.lower()

    for char in word:
        if word.count(char) > 1 or \
        char not in "abcdefghijklmnopqrstuvwxyz":
            return (word, False)
    return (word, True)



#4
def power(a, b):
    if a and b == int or float:
        return pow(a, b)
    else:
        raise TypeError('Argument must be integer or float')



#5
def my_sort(numbers):
    odd = [n for n in numbers if n % 2 != 0]
    even = [n for n in numbers if n % 2 == 0]
    return sorted(odd) + sorted(even)


