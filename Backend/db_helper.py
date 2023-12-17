import mysql.connector

global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="banka"
)

def get_balance(account_number):
    try:
        cursor = cnx.cursor()
        sql = f"SELECT Account_Balance FROM custinfo WHERE Account_Number = {account_number}"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result['Account_Balance']
    except mysql.connector.Error as err:
        print("Error retrieving account balance: {}".format(err))
        return None
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None

def get_interest_rate(account_number):
    try:
        cursor = cnx.cursor()
        category = get_account_category(account_number)
        sql = f"SELECT Interest_rate FROM accinfo WHERE Account_Category = '{category}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result['Interest_rate']
    except mysql.connector.Error as err:
        print("Error retrieving interest rate: {}".format(err))
        return None
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None

def get_account_category(account_number):
    try:
        cursor = cnx.cursor()
        sql = f"SELECT Account_Category FROM custinfo WHERE Account_Number = {account_number}"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result['Account_Category']
    except mysql.connector.Error as err:
        print("Error retrieving account category: {}".format(err))
        return None
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
