

#2
def search_records_by_institution_name(cursor):
    search_name = input("Please enter the name of the institution: ")
    cursor.execute("SELECT institution, city, course, district, telephone, email "
                   " FROM courses "
                   "WHERE institution LIKE CONCAT('%', %s, '%') "
                   "LIMIT 50 ",
                   (search_name,))
    data = cursor.fetchall()
    print(data)
#3
def search_records_by_course_name(cursor):
    search_name_course = input("Please enter the name of the course: ")
    cursor.execute("SELECT institution, city, course, district, telephone, email "
                   "FROM courses "
                   "WHERE course LIKE CONCAT('%', %s,'%') "
                   "LIMIT 50; ",
                   (search_name_course,) )
    data = cursor.fetchall()
    print(data)
#4
def find_most_Least_common_course(cursor):
    cursor.execute("SELECT course, COUNT(*) AS num "
                   "FROM courses "
                   "GROUP BY course "
                   "ORDER BY num DESC "
                   "LIMIT 1;")
    cont_result = cursor.fetchone()
    name_most_course= cont_result[0]
    print(f"The course that appeared the most times: {name_most_course}")

    cursor.execute("SELECT course, COUNT(*) AS num "
                   "FROM courses "
                   "GROUP BY course "
                   "ORDER BY num ASC "
                   "LIMIT 1;")
    cont_result = cursor.fetchone()
    name_few_course = cont_result[0]
    print(f"The course that appeared the fewest times: {name_few_course}")

#5
def show_course_count_per_district(cursor):
    cursor.execute("SELECT district, COUNT(*) AS num_courses "
                   "FROM courses "
                   "GROUP BY district "
                   "ORDER BY num_courses DESC;")
    print(cursor.fetchall())


#6
def free_sql_query(cursor):
    query_sql = input("please enter a query in sql: ")
    if query_sql.strip().upper().startswith("SELECT"):
            cursor.execute(query_sql)
            print(cursor.fetchall())
    else:
        print("ERROR_Invalid query:")


