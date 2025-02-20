import pymongo
import streamlit as st

def init_connection():
    return pymongo.MongoClient("mongodb://root:example@localhost:27017/")


client = init_connection()

def get_student_data():
    print("inside get student")
    db = client["workshop"]
    print(db)
    items = db.stundets.find()
    items = list(items)
    print(items) 
    return items

def add_student_data(name, course):
    db = client["workshop"]
    print(db)
    items = db.stundets.insert_one({ "name": name, "course": course})
    return "student data inserted"
