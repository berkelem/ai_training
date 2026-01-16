"""
INVENTORY MANAGER - Dictionary Practice Problem
Time: 5 minutes

PROBLEM:
You are building an inventory management system for a small store.
Complete the function `manage_inventory()` that performs the following tasks:

1. Create an inventory dictionary with these initial items:
   - "apple": 50
   - "banana": 30
   - "orange": 25

2. A customer buys 10 apples - update the inventory

3. Add a new item "grape" with quantity 40

4. A shipment arrives: add 20 to bananas and 15 to oranges

5. Remove any items with quantity less than 30

6. Return a dictionary containing:
   - "inventory": the final inventory dictionary
   - "total_items": total number of different item types
   - "total_quantity": sum of all quantities

EXAMPLE OUTPUT:
{
    "inventory": {"apple": 40, "banana": 50, "grape": 40, "orange": 40},
    "total_items": 4,
    "total_quantity": 170
}

Write your solution below:
"""

def manage_inventory():
    # initialize
    inventory = {"apple": 50,
                 "banana": 30,
                 "orange": 25}
    
    # customer buys 10 apples
    inventory["apple"] -= 40

    # add grape
    inventory["grape"] = 40

    # new shipment
    inventory["banana"] += 20
    inventory["orange"] += 15

    # remove items less than 30
    inventory = {k: v for k, v in inventory.items() if v >= 30}

    #summary
    total_items = len(inventory)
    total_quantity = sum(inventory.values())

    return {"inventory": inventory,
            "total_items": total_items,
            "total_quantity": total_quantity}


# Test your solution (DO NOT MODIFY)
if __name__ == "__main__":
    result = manage_inventory()
    print("Result:", result)
    
    # Expected output structure
    print("\nExpected keys: inventory, total_items, total_quantity")
    print(f"Your keys: {list(result.keys())}")
