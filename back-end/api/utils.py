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

