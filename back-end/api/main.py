#!/usr/bin/env python>=3.10

from flask import Flask
from flask_cors import CORS
from flask import request
from db.db import DbMySql
from utils import format_database_response

app = Flask(__name__)

CORS(app)


@app.route("/products", methods=["GET"])
def get_products():
    conn, cur = DbMySql().db_connect()
    sql_query = "SELECT * FROM estoque"
    cur.execute(sql_query)
    records = cur.fetchall()
    data = format_database_response(records)
    cur.close()
    conn.close()
    return data


@app.route("/products", methods=["POST"])
def create_product():
    body = request.get_json()
    conn, cur = DbMySql().db_connect()
    try:
        sql_query = f"""INSERT INTO estoque (
            title, 
            price, 
            description, 
            category, 
            image
        ) VALUES (
            '{body["title"]}', 
            {float(body["price"])}, 
            '{body["description"]}', 
            '{body["category"]}', 
            '{body["image"]}'
        )"""
        cur.execute(sql_query)
        conn.commit()
        body["msg"] = "Record inserted successfully"
    except Exception as e:
        print("error", e)
        body["msg"] = "Record not inserted"
    finally:
        cur.close()
        conn.close()
        return body


@app.route("/admin/delete", methods=["DELETE"])
def remove_product_by_id():
    body = request.get_json()
    conn, cur = DbMySql().db_connect()
    try:
        sql_query = f"""DELETE FROM estoque WHERE id={body["id"]};"""
        cur.execute(sql_query)
        conn.commit()
        body["msg"] = "Record remove successfully"
    except Exception as e:
        print("error", e)
        body["msg"] = "Could not remove data"
    finally:
        cur.close()
        conn.close()
        return body


@app.route("/update/products", methods=["POST"])
def update_product():
    body = request.get_json()
    conn, cur = DbMySql().db_connect()
    print(body)
    try:
        sql_query = f"UPDATE estoque SET title = %s, price = %s, description = %s,	category = %s,	image = %s WHERE id = %s;"
        val = (
            body["title"],
            float(body["price"]),
            body["description"],
            body["category"],
            body["image"],
            body["id"]
        )
        cur.execute(sql_query, val)
        conn.commit()
        body["msg"] = "Record inserted successfully"
    except Exception as e:
        print("error", e)
        body["msg"] = "Record not inserted"
    finally:
        cur.close()
        conn.close()
        return body


@app.route("/payment", methods=["POST"])
def check_payment():
    # todas as compras são aprovadas
    return {"payment": False}


if __name__ == "__main__":
    app.run(port=8081)
