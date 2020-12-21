import impala as ip
from impala.dbapi import connect
from sql_queries import create_views


def create_tables(cur, conn):
    """
    Discription:    
        Function that executes the create table queries.
    
    Arguments:
        cur and conn: cursor object and connector
    Return: 
        None
    """
    for query in create_views:
        cur.execute(query)
        conn.commit()

def main(host, port):
    """
    Discription:    
        Function that executes the drop table queries.
    
    Arguments:
        Endpoint: Endpoint object which locates the entrypoint to the database
    Return: 
        None
    """

    #Set up connections
    conn = connect(host, port)
    cursor = conn.cursor()

    create_tables(cursor, conn)

    conn.close()
    print("views created")

if __name__ == "__main__":
    main()