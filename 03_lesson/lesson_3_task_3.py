from address import Address
from mailing import Mailing

to_address = Address(index "156234", city "Москва", street "Новая", home "56", flat "456")
from_address = Address(index "145834", city "Орел", street "Южная", home "66", flat "4")

mailing = Mailing(to_address, from_address, cost: 1000, trask: 45874524879)

print(mailing)