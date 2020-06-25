from fastapi import FastAPI
import mysql.connector

app = FastAPI()


@app.get("/")
def read_root():
    mydb = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database=""
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Credentials")

    myresult = mycursor.fetchall()

    return {"Result": str(myresult)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}