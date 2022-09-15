from elasticsearch import Elasticsearch, helpers # bulkを使うために追加


# Elasticsearchインスタンスを作成
es = Elasticsearch("http://localhost:9200")

def gendata():
    # 登録したいドキュメント
    students = [
        {
            "name": "Jiro",
            "age": 25,
            "email": "jiro@example.com"
        },
        {
            "name": "Saburo",
            "age": 20,
            "email": "saburo@example.com"
        }
    ]

    # bulkで扱えるデータ構造に変換します
    for student in students:
        yield {
            "_op_type": "create",
            "_index": "students",
            "_source": student
        }

# 複数ドキュメント登録
helpers.bulk(es, gendata())