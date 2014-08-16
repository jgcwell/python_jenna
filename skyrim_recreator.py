out = open("skyrim_recreator.txt",mode = 'w')

## skills
for i in range(100-25):
    out.write("player.incPCS Marksman\n")
for i in range(100-20):
    out.write("player.incPCS Sneak\n")
for i in range(100-15):
    out.write("player.incPCS Smithing\n")
for i in range(100-15):
    out.write("player.incPCS Enchanting\n")
for i in range(75-20):
    out.write("player.incPCS OneHanded\n")
for i in range(75-20):
    out.write("player.incPCS Lockpicking\n")
for i in range(75-20):
    out.write("player.incPCS Pickpocket\n")
for i in range(75-20):
    out.write("player.incPCS LightArmor\n")
for i in range(65-15):
    out.write("player.incPCS Speechcraft\n")
for i in range(100-20):
    out.write("player.incPCS Alchemy\n")
for i in range(50-15):
    out.write("player.incPCS Block\n")
for i in range(50-15):
    out.write("player.incPCS Restoration\n")


## armor
## dragonscale:
for itemID in ['0001393e','0001393d','0001393f','00013940','00013941']:
    out.write("player.additem "+itemID+" 1\n")
## arrows
for itemID in ['000139b3','0001397f','000139c0']:
    out.write("player.additem "+itemID+" 100\n")
## generic weapons
for itemID in ['000139b5','000139b9','000139b9','000139b6']:
    out.write("player.additem "+itemID+" 1\n")

## gold
out.write('player.additem f 20000')

out.close()
