# pip install sqlite3
import streamlit as st
import sqlite3

# Function to create a table if it doesn't exist
def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

# Function to insert a record into the database
def insert_record(name, age):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO records (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()
    conn.close()

# Function to display all records
def display_records():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM records''')
    records = c.fetchall()
    conn.close()
    return records

# Function to delete a record from the database
def delete_record(record_id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''DELETE FROM records WHERE id = ?''', (record_id,))
