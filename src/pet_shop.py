import pdb
# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(dict):
         return dict["name"]

def get_total_cash(dict):
    return dict["admin"]["total_cash"]

def add_or_remove_cash(dict, cash_amount):
    dict["admin"]["total_cash"] += cash_amount

def get_pets_sold(dict):
    return dict["admin"]["pets_sold"]

def increase_pets_sold(dict, number_of_pets):
    dict["admin"]["pets_sold"] += number_of_pets

def get_stock_count(dict):
    return len(dict["pets"])
        
def get_pets_by_breed(dict, breed):
    return [pet for pet in dict["pets"] if pet["breed"] == breed]

def find_pet_by_name(dict, pet_name):
    for pet in dict["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

def remove_pet_by_name(dict, pet_name):
    for pet in dict["pets"]:
        if pet["name"] == pet_name:
            dict["pets"].remove(pet)

def add_pet_to_stock(dict, pet_dict):
    dict["pets"].append(pet_dict)

def get_customer_cash(customer_dict):
    return customer_dict["cash"]
            
def remove_customer_cash(customer_dict, cash_amount):
    customer_dict["cash"] -= cash_amount

def get_customer_pet_count(customer_dict):
    return len(customer_dict["pets"])
    
def add_pet_to_customer(customer_dict, new_pet_dict):
    customer_dict["pets"].append(new_pet_dict)


