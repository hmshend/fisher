from flask import request, jsonify

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
    搜索书籍路由
    """
    # 实例化自定义的SearchForm需要传入一个字典作为要校验的参数
    form = SearchForm(request.args)
    if not form.validate():
        return jsonify(form.errors)
    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    result = YuShuBook.search_by_isbn(q) if isbn_or_key == 'isbn' else YuShuBook.search_by_keyword(q)
    print(result)
    return jsonify(result)
