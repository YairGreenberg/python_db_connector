
import csv
import data





def Load_CSV_info_DB(cursor):
    counter = 0
    with open(r"C:\Users\t570\PycharmProjects\PythonProjectArmy\python_db_connector\data\courses.csv",encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            cursor.execute("INSERT INTO courses VALUES (%s,%s,%s,%s,%s,%s,%s)",row)
            counter += 1
    print("The number of rows loaded successfully: ",counter)
