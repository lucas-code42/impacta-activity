def format_database_response(data: list) -> list:
    payload = []
    for item in data:
        print(data)
        obj = {
            "id": item[0],
            "title": item[1],
            "price": float(item[2]),
            "description": item[3],
            "category": item[4],
            "image": item[5],
        }
        payload.append(obj)
    return payload










































#     return [
#         {
#         "id": 1,
#         "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
#         "price": 109.95,
#         "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
#         "category": "men's clothing",
#         "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
#         "rating": {
#             "rate": 3.9,
#             "count": 120
#         }
#     }
# ]


#   {
#     "id": 1,
#     "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
#     "price": 109.95,
#     "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
#     "category": "men's clothing",
#     "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
#     "rating": {
#       "rate": 3.9,
#       "count": 120
#     }
