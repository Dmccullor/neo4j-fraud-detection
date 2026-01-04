from .db import run_query
from . import queries

def get_accounts():
    return run_query(queries.GET_ACCOUNTS)

def get_transactions():
    return run_query(queries.GET_TRANSACTIONS)

def get_edges():
    return run_query(queries.GET_EDGES)

def detect_loops():
    return run_query(queries.DETECT_LOOPS)