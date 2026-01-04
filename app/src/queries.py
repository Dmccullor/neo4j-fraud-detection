from .db import get_session

GET_ACCOUNTS = """
MATCH (a:Account)
RETURN a.id AS id
"""

GET_TRANSACTIONS = """
MATCH (t:Transaction)
RETURN t.id AS id, t.amount AS amount
"""

GET_EDGES = """
MATCH (a1:Account)-[:SENT]->(t:Transaction)-[:TO_ACCOUNT]->(a2:Account)
RETURN a1.id AS from, a2.id AS to, t.amount AS amount
"""

DETECT_LOOPS = """
MATCH (a:Account)-[:SENT]->(:Transaction)-[:TO_ACCOUNT]->(b:Account)
MATCH (b)-[:SENT]->(:Transaction)-[:TO_ACCOUNT]->(c:Account)
MATCH (c)-[:SENT]->(:Transaction)-[:TO_ACCOUNT]->(a)
RETURN a.id AS a, b.id AS b, c.id AS c
"""