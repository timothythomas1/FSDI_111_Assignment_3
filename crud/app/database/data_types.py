from app.database import get_db

# The functions cursor(), execute(statement, ()), fetchall(), close()

def output_formatter(results): # Takes in a Tuple of Tuples and converts it into a mutable List of dictionaries
    out = []
    for result in results:
        entry = {
            "id": result[0],
            "name": result[1],
            "summary": result[2],
            "description": result[3]
        }
        out.append(entry)
    return out # Returns a List of Dictionaries

def scan(): 
    statement = "SELECT * FROM data_type"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, ())
    out = cursor.fetchall()
    cursor.close()
    return output_formatter(out) 

def select_by_type(name="Integer"):
    statement = "SELECT * FROM data_type WHERE name=?" # name is mapped to the question mark into a Tuple 
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, (name, )) # trailing comma is necessary even if there is only one data input
    out = cursor.fetchall()
    cursor.close()
    return output_formatter(out)

def create(raw_json): # The question marks are used to prevent SQL injections AKA sanatizing the data
    statement = """
        INSERT INTO data_type (
            name,
            summary,
            description
        ) VALUES (?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement,
            (
                raw_json["name"],
                raw_json["summary"],
                raw_json["description"]
            )
        )
    conn.commit()
    conn.close()

def update(raw_json, pk):
    statement = """
        UPDATE data_type
        SET name=?,
        SET summary=?,
        SET description=?
        WHERE id=?
    """
    conn = get_db()
    conn.execute(statement,
            (
                raw_json["name"],
                raw_json["summary"],
                raw_json["description"],
                pk
            )
        )
    conn.commit()
    conn.close()

def delete(pk):
    statement = "DELETE FROM data_type WHERE id?"
    conn = get_db()
    conn.execute(statement, (pk, ))
    conn.commit()
    conn.close()
