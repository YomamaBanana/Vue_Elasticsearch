from elasticsearch import Elasticsearch, helpers # bulkを使うために追加


# Elasticsearchインスタンスを作成
es = Elasticsearch("http://localhost:9200")

# es.indices.create(index='some-new-index')


mapping = {
    "mappings": {
        "properties": {
            "name": {"type": "text"},
            "birthday": {"type": "date"},
            "address": {"type": "text"},
            "email": {"type": "text"}
        }
    }
}

es.index(
 index='lord-of-the-rings',
 document={
  'character': 'Aragon',
  'quote': 'It is not this day.'
 })

# es.indices.create(index="create_test2", body=mapping)