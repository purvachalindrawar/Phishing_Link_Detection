import streamlit as st
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Purv@19205',
    'database': 'phishing'
}

def check_url_in_database(url_to_check):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        my_First_Query = "SELECT * FROM phishing_dataset WHERE URL = %s"
        cursor.execute(my_First_Query, (url_to_check,))

        this_Is_Result = cursor.fetchone()

        if this_Is_Result:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        st.error(f"Database error: {error}")
        return None
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def add_url_to_database(url_to_add):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = "INSERT INTO phishing_dataset (URL) VALUES (%s)"
        cursor.execute(insert_query, (url_to_add,))
        connection.commit()

        st.success(f"The URL '{url_to_add}' has been added to the database.")
    except mysql.connector.Error as error:
        st.error(f"Database error: {error}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

            


# Streamlit app layout
st.title("Phishing URL Detection")

# Create a session state variable to track the number of URLs checked
if 'url_count' not in st.session_state:
    st.session_state.url_count = 0

url_to_check = st.text_input("Enter the URL you want to check:")

if st.button("Check URL"):
    if url_to_check:
        result = check_url_in_database(url_to_check)
        st.session_state.url_count += 1  # Increment the count of URLs checked
        if result is True:
            st.error(f"Warning: The URL '{url_to_check}' is found in the database and may be a phishing site.")
        elif result is False:
            st.warning(f"The URL '{url_to_check}' is not found in the database.")
            if st.button("Add URL to Database"):
                add_url_to_database(url_to_check)
    else:
        st.warning("Please enter a URL.")

# Display the count of URLs checked
st.write(f"Total URLs checked: {st.session_state.url_count}")
