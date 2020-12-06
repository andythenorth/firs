registered_economies = []

# specify economies in the order that they should appear in parameter list in-game (and also in docs)
# economies have a numeric ID which maps parameter values and avoids breaking savegames when this list changes
# !! ^ that doesn't appear to work, action 14 param doesn't seem to be able to abstract name value from name orde??

from economies import mak_test #here I start my economy further information of it is in mak_test.pnmly
mak_test.economy.register()