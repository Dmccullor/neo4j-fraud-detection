from db import get_session

def get_all_accounts():
    query = """
    MATCH (a:Account)
    RETURN a.id AS id
    """
    with get_session() as session:
        result = session.run(query)
        return result.data()