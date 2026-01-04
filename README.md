## Fraud Detection Demo (Neo4j + Python)

This project is a small, self‑contained demo showing how to model financial transactions in Neo4j and detect simple fraud patterns using Python. It focuses on clarity, reproducibility, and a clean end‑to‑end workflow rather than production‑scale complexity.

The goal of this project is to demonstrate:
- How to model accounts, customers, devices, merchants, and transactions in Neo4j
- How to query the graph using Cypher
- How to run those queries from Python
- How to detect a basic fraud pattern (transaction loops)
- How to structure a small Python project cleanly

## Graph Schema

The Neo4j graph uses the following node labels:
- Account
- Customer
- Device
- Merchant
- Transaction
And the following relationship types:
- (:Customer)-[:OWNS]->(:Account)
- (:Customer)-[:USES]->(:Device)
- (:Account)-[:SENT]->(:Transaction)
- (:Transaction)-[:TO_ACCOUNT]->(:Account)
- (:Transaction)-[:TO]->(:Merchant)
This structure supports modeling money movement, customer behavior, and device/merchant interactions.

## Project Structure
app/
  app.py
  src/
    __init__.py
    db.py
    queries.py
    analysis.py

- db.py — Neo4j driver + helper to run Cypher queries
- queries.py — Cypher queries used by the project
- analysis.py — Python functions that wrap the queries
- app.py — Main script that runs the demo
