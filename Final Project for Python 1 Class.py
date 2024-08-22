def shelve(inventory, product_list):
    # Here you iterate through the product_list.
    for p in product_list:
        # The product_list contains pairs (tuples), e.g. ('apple', 20) and you
        # check if the first element of the pair, i.e. p[0] exists as a key
        # in the dictionary.
        if p[0] in inventory:
            # You use try-except to raise and then handle the exception
            try:
                # If key p[0] exists in the dictionary then you add the value from the pair, i.e. p[1] to existing key's value in the dictionary
                inventory[p[0]] += p[1]
                # If the value of the key p[0] is negative you raise an exception with the message in the parentheses
                if inventory[p[0]] < 0:
                    raise ValueError('negative amount for product')
            # Here you handle the exception. You print the message and subtract the value you added.
            except ValueError as ve:
                print(ve)
                inventory[p[0]] -= p[1]
        # If the key p[0] does not exist in the dictionary, then you add it to the dictionary and assign value p[1] to it.
        else:
            inventory[p[0]] = p[1]
    #Here you just print the contents of inventory
    print(inventory)

# These are just examples to test the code.
d = {"apple":50, "pear":30, "orange":25}
ps = [("apple",20),("pear",-10),("grape",18)]

shelve(d, ps)
shelve(d,[("apple",-1000)])