import phonenumbers as p
from phonenumbers import carrier
print("For EX: +917409*****")
mno = input("Enter Phone NO:")
spro = p.parse(mno)
pname = carrier.name_for_number(spro,"en")
print(pname)


