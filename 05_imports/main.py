import sys
print(sys.path)

# FIRST OPTION
import tea_business.recipes.flavours



print(tea_business.recipes.flavours.tea_one())

# SECOND OPTION
from tea_business.recipes.flavours import ginger_tea as aaa
print(aaa())

#THIRD OPTION
from tea_business.recipes.flavours import ginger_tea, tea_one
print(tea_one())


# OPTION 4
from .tea_business.recipes.flavours import ginger_tea