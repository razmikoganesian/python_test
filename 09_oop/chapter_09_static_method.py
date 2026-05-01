class TeaUlits:
    def clean_ingredients(self, text):
        a = [item.strip() for item in text.split(',')]
        return a

raw = "water , lemon   , tea.    , nnn.    , 1"

obj = TeaUlits()
print(obj.clean_ingredients(raw))


# using static method allow direct use of class
class TeaUlits1:

    @staticmethod
    def clean_ingredients(text):
        a = [item.strip() for item in text.split(',')]
        return a

raw1 = "aaa , bbb   , ccc    , dddd    , 4r5t"
b = TeaUlits1.clean_ingredients(raw1)
print(b)