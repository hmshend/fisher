import json

from flask import request, jsonify, flash, render_template

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from . import web


@web.route('/book/search')
def search():
    """
    搜索书籍路由
    """
    # 实例化自定义的SearchForm需要传入一个字典作为要校验的参数
    books = BookCollection()
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushubook = YuShuBook()
        if isbn_or_key == 'isbn':
            yushubook.search_by_isbn(q)
        else:
            yushubook.search_by_keyword(q, page)
        books.fill(yushubook, q)
        # print(result)
        # return jsonify(result)
    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")
    # return json.dumps(books, default=lambda o: o.__dict__)
    return render_template('search_result.html', books=books)


@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    pass
