import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = r'bolt://localhost:7687'
USER = os.getenv('NEO4J_USER')
PASSWORD = os.getenv('NEO4J_PASSWORD')
DATABASE = 'neo4j'

if not PASSWORD:
    raise RuntimeError('NEO4J_PASSWORD is not set in .env')

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def get_session():
    return driver.session(database=DATABASE)

def test_connection():
    with get_session() as session:
        result = session.run("RETURN 'connected' AS status")
        print(result.single()["status"])

def run_query(query, params=None):
    with get_session() as session:
        result = session.run(query, params or {})
        return [record.data() for record in result]