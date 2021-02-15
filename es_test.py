from elasticsearch import Elasticsearch

es = Elasticsearch(["xxx:1"])

# 方式1：
es.search(index="index_name", doc_type="type_name")

# 方式2：
body = {
    "query": {
        "match_all": {}
    }
}
es.search(index="index_name", doc_type="type_name", body=body)


# term: 查询 xx = “xx”
body = {
    "query": {
        "term": {
            "name": "python"
        }
    }
}
# 查询name="python"的所有数据
es.search(index="index_name", doc_type="type_name", body=body)