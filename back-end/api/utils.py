def format_database_response(data: list) -> list:
    payload = []
    for item in data:
        obj = {
            "id": item[0],
            "quantidade": item[1],
            "preco": float(item[2]),
            "descricao": item[3],
            "foto": item[4],
            "produto": item[5],
        }
        payload.append(obj)
    return payload
