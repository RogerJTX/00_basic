from elasticsearch import Elasticsearch

# elasticsearch集群服务器的地址
ES = [
    'xxx'
]

# 创建elasticsearch客户端
es = Elasticsearch(
    ES
    # 启动前嗅探es集群服务器
    #sniff_on_start=True,
    # es集群服务器结点连接异常时是否刷新es节点信息
    #sniff_on_connection_fail=True
    # 每60秒刷新节点信息
    #sniffer_timeout=60
)
print(es)

# ret = es.search(index='industry_center_company')
# print(ret)

# res = es.get(index='industry_center_company', doc_type='company', id='5f853bac2514970234ee9a46')
# print(res)

query = {"query":{"match":{"industrys.name":"人工智能"}}}
ret = es.search(index='industry_center_company', doc_type='company', body=query)
# print(ret)
print(type(ret))

total = ret['hits']['total']
print(total)

hits = ret['hits']['hits']
for num, i in enumerate(hits):

    # print(i)
    name = i['_source']['name']
    website = i['_source']['website']
    industrys = i['_source']['industrys']
    print(name)
    # print(website)
    # print(industrys)
    flag = 0
    for i2 in industrys:
        if i2['name'] == '人工智能':
            flag = 1
    if flag == 1:
        with open('company_product_website.txt', 'r', encoding='utf-8') as f1:
            f1.write(name +'\t' + website + '\n')

