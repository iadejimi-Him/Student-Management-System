from database.db_connection import get_connection


def register_student(
    student_number, 
    first_name, 
    last_name, 
    email, 
    department_id, 
    gender, 
    date_of_birth
    
):
    
    
    connection = get_connection()
    
    if connection is None:
        return None
    
    try:
        cursor = connection.cursor()
        
        
        query = """
            INSERT INTO students(
                student_number,
                first_name,
                last_name,
                email,
                department_id,
                gender,
                date_of_birth
                )
                VALUES (%s, %s,  %s,  %s,  %s,  %s,  %s)
                RETURNING student_id;
            """
            
        cursor.execute(query,(
                student_number,
                first_name,
                last_name,
                email,
                department_id,
                gender,
                date_of_birth
            ))
            
        student_id = cursor.fetchone()[0]
            
            
        connection.commit()
            
        return student_id
        
    except Exception as error:
        connection.rollback()
        print("Student registration failed:", error)
        return None
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            
            
        
        
def get_all_students():
    
    
    connection = get_connection()
    
    if connection is None:
        return[]
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT *
        FROM public.students
        ORDER BY student_id;
        """
        
        cursor.execute(query)
        
        students = cursor.fetchall()
        
        return students
    except Exception as error:
        print("Unable to retrieve students:", error)
        return[]
    
    finally:
        if cursor is not None:
            cursor.close()
            
            connection.close()
        