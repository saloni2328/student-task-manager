import mysql.connector

def get_database_connection():
    
    connection=mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="3LNe7smiMPb9ETu.root",
        password="7Nvwri1dWK6e4Wa7",
        database="student_task_manager",
        port=4000
    )
    return connection
    