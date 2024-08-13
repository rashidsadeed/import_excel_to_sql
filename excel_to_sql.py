import mysql.connector
import pandas as pd
import numpy as np


def db_insert(curser, table, cols, values):
    placeholders = ", ".join(['%s'] * len(values))
    query = f"""INSERT INTO {table} ({cols}) VALUES ({placeholders})"""
    #print(query)
    curser.execute(query, values)


def import_sql(curser, db, df, table, cols):
    for i in range(len(df)):
        data = df.loc[i].values
        temp = []
        for j in data:
            if str(j) == "nan":
                temp.append(None)
            else:
                temp.append(str(j))

        temp = tuple(temp)
        db_insert(curser, table, cols, temp)
    db.commit()


_
def import_data(filename, password, database, table,  host="localhost", user="root"):
    df = pd.read_csv(filename)
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    mycursor = mydb.cursor()
    import_sql(mycursor, mydb, df, table, cols)

if __name__ == "__main__":
    #replace the filename, password, database and table accordingly
    import_data("data.csv", "password", "database", "table")
