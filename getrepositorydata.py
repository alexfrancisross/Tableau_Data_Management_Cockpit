import psycopg2

from psycopg2 import Error
from outputtohyper import insert_into_view_stats_tables, insert_into_hist_events_tables
from repository_queries import get_repo_queries_and_tables
from datetime import datetime


def connect_to_repository(settings):
    repository_connection = None
    repo_host = settings["REPOSITORY_HOST"]
    repo_port = settings["REPOSITORY_PORT"]
    repo_database = settings["REPOSITORY_DATABASE"]
    repo_user = settings["REPOSITORY_USER"]
    repo_password = settings["REPOSITORY_PASSWORD"]

    try:
        # Connect to the repository
        repository_connection = psycopg2.connect(user=repo_user,
                                                 password=repo_password,
                                                 host=repo_host,
                                                 port=repo_port,
                                                 database=repo_database)

        # Create a cursor to perform database operations
        cursor = repository_connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to Postgres", error)

    return repository_connection


def get_and_write_repo_data_to_hyper(hyper_connection, table_definitions, settings):
    # query settings
    pagination = int(settings['REPOSITORY_PAGINATION'])
    # Check to see if there is a limit on the number of rows returned per query. Usually here for testing.
    row_limit_str = settings["REPO_TABLE_ROW_LIMIT"]
    if row_limit_str != "":
        row_limit_str = " limit " + row_limit_str

    current_row = 0
    # Log into Tableau Repository
    repo_connection = connect_to_repository(settings)

    all_query_data = get_repo_queries_and_tables(table_definitions)

    for query_data in all_query_data.items():
        query_name = query_data[0]
        query_table_def = query_data[1].get('table')
        query = query_data[1].get('query') + row_limit_str

        # Create a cursor to perform database operations
        data_cursor = repo_connection.cursor(name='large_results')
        print("Got new query cursor")

        # run views statistic query
        data_cursor.execute(query)

        # fetch results
        while True:
            # consume result over a series of iterations
            # with each iteration fetching 2000 records
            records = data_cursor.fetchmany(size=pagination)

            if not records:
                break

            if query_name == "View Stats":
                insert_into_view_stats_tables(hyper_connection, records, query_table_def)
                current_row += len(records)
                print("Total rows {1} inserted in {0} table - {2}".format(query_name, current_row, datetime.now().time()))
            elif query_name == "Historic Events":
                insert_into_hist_events_tables(hyper_connection, records, query_table_def)
                current_row += len(records)
                print("Total rows {1} inserted in {0} table - {2}".format(query_name, current_row, datetime.now().time()))

        # Close the cursor
        if data_cursor:
            data_cursor.close()
            print("Closing query cursor\n")

    # Close the connection to Postgres
    if repo_connection:
        repo_connection.close()
        print("Postgres connection is closed")
