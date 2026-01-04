CREATE (c1:Customer {id: "C1", name: "Alice"});
CREATE (c2:Customer {id: "C2", name: "Bob"});
CREATE (c3:Customer {id: "C3", name: "Charlie"});

CREATE (a1:Account {id: "A1"});
CREATE (a2:Account {id: "A2"});
CREATE (a3:Account {id: "A3"});

CREATE (d1:Device {id: "D1"});
CREATE (d2:Device {id: "D2"});

CREATE (m1:Merchant {id: "M1", name: "Electronics Hub"});
CREATE (m2:Merchant {id: "M2", name: "Luxury Goods"});

MATCH (c1:Customer {id: "C1"}), (a1:Account {id: "A1"})
MERGE (c1)-[:OWNS]->(a1);

MATCH (c2:Customer {id: "C2"}), (a2:Account {id: "A2"})
MERGE (c2)-[:OWNS]->(a2);

MATCH (c3:Customer {id: "C3"}), (a3:Account {id: "A3"})
MERGE (c3)-[:OWNS]->(a3);

MATCH (c1:Customer {id: "C1"}), (d1:Device {id: "D1"})
MERGE (c1)-[:USES]->(d1);

MATCH (c2:Customer {id: "C2"}), (d1:Device {id: "D1"})
MERGE (c2)-[:USES]->(d1);

MATCH (c3:Customer {id: "C3"}), (d2:Device {id: "D2"})
MERGE (c3)-[:USES]->(d2);

CREATE (t1:Transaction {id: "T1", amount: 500});
CREATE (t2:Transaction {id: "T2", amount: 5000});
CREATE (t3:Transaction {id: "T3", amount: 4500});

MATCH (a1:Account {id: "A1"}), (a2:Account {id: "A2"}), (t1:Transaction {id: "T1"})
MERGE (a1)-[:SENT]->(t1)-[:TO_ACCOUNT]->(a2);

MATCH (a2:Account {id: "A2"}), (a3:Account {id: "A3"}), (t2:Transaction {id: "T2"})
MERGE (a2)-[:SENT]->(t2)-[:TO_ACCOUNT]->(a3);

MATCH (a3:Account {id: "A3"}), (a1:Account {id: "A1"}), (t3:Transaction {id: "T3"})
MERGE (a3)-[:SENT]->(t3)-[:TO_ACCOUNT]->(a1);

MATCH (t2:Transaction {id: "T2"}), (m2:Merchant {id: "M2"})
MERGE (t2)-[:TO]->(m2);

MATCH (p1:Customer)-[:USES]->(d:Device)<-[:USES]-(p2:Customer)
WHERE p1 <> p2
RETURN p1.name AS Customer1, p2.name AS Customer2, d.id AS Device;

MATCH (p1:Customer)-[:USES]->(d:Device)<-[:USES]-(p2:Customer)
WHERE p1 <> p2
RETURN p1.name AS Customer1, p2.name AS Customer2, d.id AS Device;

MATCH p = (a1:Account)-[:SENT]->(:Transaction)-[:TO_ACCOUNT]->(a2)
WHERE a1 <> a2
RETURN p;