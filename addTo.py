def addToInventory(inventory, addedItems):
    # your code goes here
    for k, v in inventory.items():
        if k in inventory:
            for i in addedItems:
                if i == k:
                   v += 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
