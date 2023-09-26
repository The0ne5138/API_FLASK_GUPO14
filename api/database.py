# Podria (o deberia llamarse CONECCTION.py)

import mysql.connector


class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host='127.0.0.1',
                user='grupo14',
                port="3306",
                password='1234',
                database='DB_TIF_Grupo_14'
            )
        return cls._connection

    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor

    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None