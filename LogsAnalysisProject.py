# Python 2 - Logs Analysis Project - Udacity - Chris Fiorino

import psycopg2


DBNAME = "news"


# Question1
def question1():
    # Question 1: What are the most popular three articles of all time?

    # Connect to database and scan with cursor
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    """
    Run sql command to find three most popular articles of all time based
    on successful views
    """

    c.execute("""
        select title, count(path) as views
        from articles
        join log on log.path like CONCAT('%',articles.slug,'%')
        where status like '%200%'
        group by articles.title
        order by count(path) desc
        limit 3""")

    # Use fetchall to store the results of the sql query
    results = c.fetchall()

    # Print out the three most popular articles of all time
    print("What are the most popular three articles of all time? \n")

    # Loop through sql results, print according to example format
    for result in results:
        print(u'\u2022' + ' "' + str.title(result[0]) + '" - ' +
              str(result[1]) + " views")

    # Close the database
    db.close()


# Question 2
def question2():
    # Question 2: Who are the most popular article authors of all time?

    # Connect to database and scan with cursor
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    """
    Run sql command to show authors popularity based on all time
    successful views
    """
    c.execute("""
        select authors.name, count(path) as views
        from articles
        join log on log.path like CONCAT('%',articles.slug,'%')
        join authors on authors.id = articles.author
        where status like '%200%'
        group by authors.name
        order by count(path) desc""")

    # Use fetchall to store the results of the sql query
    results = c.fetchall()

    # Print out the three most popular articles of all time
    print("Who are the most popular article authors of all time? \n")

    # Loop through sql results, print according to example format
    for result in results:
        print(
            u'\u2022' + " " + str(result[0]) +
            " - " + str(result[1]) + " views")

    # Close the database
    db.close()


# Question 3
def question3():
    # Question 3: On which days did more than 1% of requests lead to errors?

    # Connect to database and scan with cursor
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Run sql command to show days where the % of error requests exceeded 1%
    c.execute("""
        with error_calc as (
        select date(time),
        100*(SUM(CASE WHEN status not like '%200%'
        THEN 1 ELSE 0 END)/count(status)::float) as error_rate
        from log
        group by date
        )
        select date, error_rate from error_calc
        where error_rate > 1""")

    # Use fetchall to store the results of the sql query
    results = c.fetchall()

    # Print out the three most popular articles of all time
    print("On which days did more than 1'%' of requests lead to errors? \n")

    # Loop through sql results, print according to example format
    for result in results:
        print(
            u'\u2022' + " " + "{:%b %d, %Y}".format(result[0]) +
            " - " + '{:.1f}'.format(result[1]) + '%' + " errors")

    # Close the database
    db.close()


# Run the three methods
question1()
print('\n')
question2()
print('\n')
question3()
