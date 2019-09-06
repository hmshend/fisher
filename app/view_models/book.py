class BookViewModel:
    def __init__(self, data):
        self.title = data['title']
        self.author = '、'.join(data['author'])
        self.binding = data['binding']
        self.publisher = data['publisher']
        self.image = data['image']
        self.price = '￥' + data['price'] if data['price'] else data['price']
        self.isbn = data['isbn']
        self.pubdate = data['pubdate']
        self.summary = data['summary']
        self.pages = data['pages']

    @property
    def intro(self):
        intro = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intro)


class BookCollection:

    def __init__(self):
        self.keyword = ''
        self.books = []
        self.total = 0

    def fill(self, yushubook, keyword):
        self.keyword = keyword
        self.total = yushubook.total
        self.books = [BookViewModel(book) for book in yushubook.books]
