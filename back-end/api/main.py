#!/usr/bin/env python3.10

from flask import Flask
from flask_cors import CORS
from flask import request
from flask import make_response
from db.db import DbMySql
from utils import format_database_response

app = Flask(__name__)

CORS(app)

ADMIN = "root"
SENHA = "root"


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
        sql_query = f"""INSERT INTO estoque (quantidade, preco, descricao, foto_base64, produto) VALUES ('{body["quantidade"]}', {float(body["preco"])}, '{body["descricao"]}', '{body["foto"]}', '{body["produto"]}')"""
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


@app.route("/admin", methods=["POST"])
def admin():
    body = request.get_json()
    if body["admin"] == ADMIN and body["senha"] == SENHA:
        default_body = {"message": "ok"}
        response = make_response(default_body)
        response.status_code = 200
        return response
    else:
        default_body = {"message": "unauthorized"}
        response = make_response(default_body)
        response.status_code = 404
        return response


if __name__ == "__main__":
    app.run(port=8080)
