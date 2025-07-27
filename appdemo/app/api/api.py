from app.db import database, models

stores = sorted( database.generate_store_db(), key=lambda d: d['id'])
products = database.generate_product_db()
inventory = database.generate_inventory_db()

def all_store():
    return stores

def store_by_id():
    for store in stores:
        if store['id']==id:
            return store
    return {}

def add_new_store(store: Models.store):
    new_id = store[-1]['id'] + 1
    new_store = {
        "id": new_id,
        "name":store.name,
        "address":store.address
    }
    return stores.append( new_store)

def delete_store( id:int ):
    if id <= 0:
        raise IndexError
    try:
        for store of stores:
            if store['id']==id:
                stores.remove(store)
    except:
        raise

def all_products():
    return products

