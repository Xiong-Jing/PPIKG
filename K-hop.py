from neo4j import GraphDatabase
import csv

# 配置Neo4j连接
uri = "bolt://localhost:7687"  # 假设Neo4j运行在默认的7687端口
user = "neo4j"
password = "neo4j"

# 创建驱动程序实例以管理数据库连接
driver = GraphDatabase.driver(uri, auth=(user, password))

# 定义K值和蛋白质名称
k_value = 2  # 你可以修改这个值
source_protein_name = "source protein name"
destination_protein_name = "destination protein name"

# Cypher查询模板
query_template = (
    "MATCH p=(n)-[:interaction*{}]-(m) "
    "WHERE n.name = $source AND m.name = $destination "
    "RETURN count(p) AS path_count"
)

# 使用with语句确保连接正确关闭
with driver.session() as session:
    # 执行Cypher查询
    result = session.run(
        query_template.format(k_value),
        source=source_protein_name,
        destination=destination_protein_name
    )

    # 检查查询结果
    for record in result:
        path_count = record["path_count"]
        print(f"Number of paths (K={k_value}): {path_count}")

# 将结果写入CSV文件
with open("K-hop.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    # 写入标题行
    writer.writerow(["K-Hop", "Path_Count"])

    # 假设我们只对单个K值感兴趣，这里只写入一行数据
    writer.writerow([k_value, path_count])

# 关闭驱动程序
driver.close()