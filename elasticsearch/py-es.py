# coding=utf-8
from elasticsearch import Elasticsearch


class ElasticObi:
    def __init__(self, index_name, index_type, ip='192.168.20.100'):
        """
        :param index_name: 索引名称
        :param index_type: 索引类型
        :param ip: es_server IP
        """
        self.index_name = index_name
        self.index_type = index_type
        self.es = Elasticsearch([ip], port=9200)

    def create_index(self, index_name='ott', index_type='ott_type'):
        """
        :param index_name: 创建索引ott
        :param index_type: 创建类型 ott_type
        :return:
        """
        # 创建映射
        _index_mappings = {
            "mappings": {
                self.index_type: {
                    "properties": {
                        "title": {
                            "type": "text",
                            "index": True,
                            "analyzer": 'ik_max_word',
                            "search_analyzer": "ik_max_word"
                        },
                        "date": {
                            "type": "text",
                            "index": True
                        },
                        "keyword": {
                            "type": "string",
                            "index": "not_analyzer"
                        },
                        "source": {
                            "type": "string",
                            "index": "not_analyzer"
                        },
                        "link": {
                            "type": "string",
                            "index": "not_analyzer"
                        }
                    }
                }
            }
        }
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index_name=self.index_name, body=_index_mappings)
            print res

obj = ElasticObi("ott", "ott_type", ip="192.168.20.100:9200")
obj.create_index()
