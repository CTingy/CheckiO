def bigger_price(limit: int, data: list) -> list:
    result = []
    for i in range(limit):
        max_price = 0
        max_item = None
        for item in data:
            if item["price"] > max_price:
                max_price = item["price"]
                max_item = item
        data.remove(max_item)
        result.append(max_item)
        print(max_item)
    return result       


if __name__ == '__main__':
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"
'''
return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]
---------------------------------------------------------------------
return sorted(data, key=lambda x: x.get("price"), reverse=True)[:limit]
--------------------------------------------------------------
# get the 'limit' highest prices, sorted by descending price
prices = sorted([elem['price'] for elem in data], reverse=True)[:limit]
# add each dictionary from 'data'  with highest prices
output = [elem for elem in data if elem['price'] in prices]
# sort the list (in place) by descending price
output.sort(key=lambda t: t['price'], reverse=True)
return output
--------------------------------------------------------
return sorted(data, key=lambda x: -x['price'])[:limit]
'''
