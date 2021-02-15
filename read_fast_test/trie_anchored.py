#字典树后挂靠企业全名
import os 
import logging
import pickle
from pyArango.connection import Connection


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# PATH =# os.path.dirname(os.path.abspath(__file__))
f = open(r"D:\tmp\tmp.txt", 'r',encoding='utf-8')
# TRIE_FILE = os.path.join(PATH, 'trie.pkl')

## 字典树
class TreeNode(object):
    def __init__(self,data = '',word_end = -1):
        self.data = data
        self.children = {}
        self.word_end = -1
        
class Trie:
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word,fullname):
        curNode = self.root
        for c in word :
            if not c in curNode.children:
                curNode.children[c] = TreeNode()
            curNode = curNode.children[c]
        curNode.word_end = True
        curNode.data = fullname

    def startsWith(self, prefix):
        curNode = self.root
        for c in prefix:
            if not c in curNode.children:
                return False
            curNode = curNode.children[c]
        return True

    def search(self, word):
        curNode = self.root
        for c in word:
            if not c in curNode.children:
                return False
            curNode = curNode.children[c]   
        # Doesn't end here
        if not curNode.word_end :
            return False
        return True,curNode.data
    

# 字典树管理类
class Trie_Manager():

    def __init__(self):
        company_list = [line.strip().split("\t") for line in open(COMPANY_FILE).readlines()]
        self.trie = Trie()

        for companys in company_list:
            fullname = companys[0]
            for company in companys:
                self.trie.insert(company,fullname)
        logger.info("字典树建立完成, 共有 {} 个企业".format(len(companys)))

        ## dump
        output = open(TRIE_FILE, "wb")
        pickle.dump(self.trie, output)
        logger.info("字典树pkl文件存储完成")
     

    def search_company(self, news):
        i = 0
        companys = []

        while i < len(news):
            count = 0
            letter = news[i]
            if letter <= "z" and letter >= 'a':
                if len(news) > i + len(letter):
                    i = i + 1
                else:
                    break
            while self.trie.startsWith(letter):
                if count == 0:
                    startword = letter
                count += 1
                if len(news) > i + count :
                    letter = letter + news[i+count]
                    if self.trie.search(letter)[0]:
                        break
                else:
                    break
            if self.trie.search(letter)[0]:
                if letter not in companys:
                    companys.append(self.trie.search(letter)[1])
                if len(news) == i + len(letter):
                    break
                else:
                    i = i + len(letter)
            elif len(news) > i + 1:
                i = i + 1
            else:
                break
        return companys   


    def refresh(self):
        logger.info("trie_manager组件开始刷新")
        company_list = [line.strip().split("\t") for line in open(COMPANY_FILE).readlines()]
        self.trie = Trie()

        for companys in company_list:
            fullname = companys[0]
            for company in companys:
                self.trie.insert(company,fullname)
        logger.info("字典树重新建立完成, 共有{}个企业名".format(len(companys)))

        output = open(TRIE_FILE, "wb")
        pickle.dump(self.trie, output)
        logger.info("trie_manager刷新完成")
     

    