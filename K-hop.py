from neo4j import GraphDatabase
import csv

# Neo4j Connection
uri = "bolt://localhost:7687"  # the port of Neo4j
user = "neo4j"
password = "neo4j"

# Neo4j data driver config
driver = GraphDatabase.driver(uri, auth=(user, password))

# Define K value and protein name
k_value = 2  # it can be setted by user
source_protein_name = "source protein name"
destination_protein_name = "destination protein name"

# Cypher query template
query_template = (
    "MATCH p=(n)-[:interaction*{}]-(m) "
    "WHERE n.name = $source AND m.name = $destination "
    "RETURN count(p) AS path_count"
)

# Establish a session with the driver to interact with the database
with driver.session() as session:
    # 执行Cypher查询
    result = session.run(
        query_template.format(k_value),
        source=source_protein_name,
        destination=destination_protein_name
    )

    # Check the query results
    for record in result:
        path_count = record["path_count"]
        print(f"Number of paths (K={k_value}): {path_count}")

# Save the results to a CSV file
with open("K-hop.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    # Create a table header
    writer.writerow(["K-Hop", "Path_Count"])

    # Assuming we are only interested in a single K value. write one line of data here 
    writer.writerow([k_value, path_count])

# Close the database driver
driver.close()
