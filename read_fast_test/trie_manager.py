#建立企业的字典树
import os 
import logging
import pickle
from pyArango.connection import Connection
from ..register import Register

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PATH = os.path.dirname(os.path.abspath(__file__))
COMPANY_FILE = os.path.join(PATH, 'company.txt')
TRIE_FILE = os.path.join(PATH, 'trie.pkl')

class Trie:
    def __init__(self):
        self.root = {}
        self.word_end = -1

    def insert(self,word):
        curNode = self.root
        for c in word :
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.word_end] = True

    def startsWith(self,prefix):
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]
        return True

    def search(self, word):
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]   
        # Doesn't end here
        if self.word_end not in curNode:
            return False
        return True
    
    


class Trie_Manager():

    def __init__(self, TRIE_FILE):
        if os.path.exists(TRIE_FILE):
            self.trie = pickle.loads(TRIE_FILE, "rb")
            logger.info("字典树pkl文件加载完成")
        else:
            companys = [line.strip() for line in open(COMPANY_FILE).readlines()]
            self.trie = Trie()

            for company in companys:
                self.trie.insert(company)
            logger.info("字典树建立完成, 共有{}个企业名".format(len(companys)))

            output = open(TRIE_FILE, "wb")
            pickle.dump(self.trie, output)
            logger.info("字典树pkl文件存储完成")
     

    def search_company_name(self,news):
        i = 0
        company = []
        # trie = Trie()
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
                    if self.trie.search(letter):
                        break
                else:
                    break
            if self.trie.search(letter):
                if letter not in company:
                    company.append(letter)
                if len(news) == i + len(letter):
                    break
                else:
                    i = i + len(letter)
            elif len(news) > i + 1:
                i = i + 1
            else:
                break
        return company    

    def refresh(self):
        logger.info("trie_manager组件开始刷新")
        companys = [line.strip() for line in open(COMPANY_FILE).readlines()]
        self.trie = Trie()

        for company in companys:
            self.trie.insert(company)
        logger.info("字典树重新建立完成, 共有{}个企业名".format(len(companys)))

        output = open(TRIE_FILE, "wb")
        pickle.dump(self.trie, output)
        logger.info("trie_manager刷新完成")
        pass

