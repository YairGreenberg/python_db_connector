import db.connection
import db.load_csv
import db.queries



def print_nenu()->None:
    print('='*50)
    print("Make a choice: \n"
          "1. load CSV into DB__\n"
          "2. Search records by institution name__\n"
          "3. Search records by course name__\n"
          "4. Find most/least common course__\n"
          "5. Show course count per district__\n"
          "6. Free SQL query__\n"
          "7. Exit__")
    print('=' * 50)


def main():
    connected= db.connection.get_connection()
    # add create a db
    db.connection.create_table()
    cursor = connected.cursor()
    while True:
        print_nenu()
        choice = int(input("Please entre a number choice: "))
        if choice == 1:
            db.load_csv.Load_CSV_info_DB(cursor)
            connected.commit()
        if choice == 2:
            db.queries.search_records_by_institution_name(cursor)
        if choice == 3:
            db.queries.search_records_by_course_name(cursor)
        if choice == 4:
            db.queries.find_most_Least_common_course(cursor)
        if choice == 5:
            db.queries.show_course_count_per_district(cursor)
        if choice == 6:
            db.queries.free_sql_query(cursor)
        if choice == 7:
            break
    cursor.close()
    connected.close()
if __name__ == '__main__':
    main()
