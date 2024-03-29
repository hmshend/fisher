from flask import current_app

from app.libs.myhttp import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.books = []
        self.total = 0

    def search_by_isbn(self, number):
        url = self.isbn_url.format(number)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config["PRE_PAGE"], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.books = data
            self.total = 1

    def __fill_collection(self, data):
        if data:
            self.books = data['books']
            self.total = data['total']

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config["PRE_PAGE"]
