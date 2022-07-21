import sqlite3
from sqlite3 import Error


def create_connection(kumadb):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(kumadb)
    except Error as e:
        print(e)

    return conn


# def select_all_heartbeats(conn):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM heartbeat")

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)
def count_heartbeat_by_status(monitor_id, status):
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM heartbeat WHERE monitor_id=? AND status=?", (monitor_id, status))
    result = cur.fetchone()

    return result

def count_heartbeat_by_monitor_id(monitor_id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM heartbeat WHERE monitor_id=?", (monitor_id,))

    rows = cur.fetchone()

    return rows


# # def select_heartbeat_by_status(status):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM heartbeat WHERE status=?", (status,))

    
#     rows = cur.fetchall()

#     return rows
 

def main():
    global conn

    database = r"C:\Users\mehdipyw\Desktop\uptime-kuma-data\kuma.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        #print("1. Query task by monitor_id:")
        rows = count_heartbeat_by_monitor_id(35)
        #for row in rows:
        print(rows)

        # print("1. Query task by status:")
        # select_heartbeat_by_status(1)

    
        # print("2. Query all heartbeats")
        #select_heartbeat_by_status(1)
        result = count_heartbeat_by_status(96,1)
        print(result)



        percentage=(result[0]/rows[0])*100
        print(percentage)

        




if __name__ == '__main__':
    main()

