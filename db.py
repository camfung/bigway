import psycopg2
import psycopg2.extras
import os
def get_db_connection_string():
    # Retrieve the database connection string from the environment variable
    db_url = os.getenv("DATABASE_URL")
    if db_url is None:
        raise EnvironmentError("DATABASE_URL environment variable is not set")
    return db_url


def execute_query_with_values(query, values):
    try:
        # Get the database connection string from the .env file
        db_url = get_db_connection_string()

        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(db_url)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute the query with the provided values
        cursor.execute(query, values)

        # If the query modifies the database (e.g., INSERT, UPDATE, DELETE), commit the changes
        conn.commit()

        # Fetch and return the results (if any) for SELECT queries
        if cursor.description:
            result = cursor.fetchall()
        else:
            result = None

        return result

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()


def execute_query_with_values_batch(query, values):
    try:
        # Get the database connection string from the .env file
        db_url = get_db_connection_string()

        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(db_url)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute the query with the provided values
        psycopg2.extras.execute_batch(cursor, query, values)

        # If the query modifies the database (e.g., INSERT, UPDATE, DELETE), commit the changes
        conn.commit()

        # Fetch and return the results (if any) for SELECT queries
        if cursor.description:
            result = cursor.fetchall()
        else:
            result = None

        return result

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        # Close the cursor and the database connection
        cursor.close()
        conn.close()
