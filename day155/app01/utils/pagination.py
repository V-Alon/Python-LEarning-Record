# app01/utils/pagination.py
from django.utils.safestring import mark_safe
from urllib.parse import urlencode


class Pagination:
    """
    request      : Django 的 request 对象
    queryset     : 要分页的数据集（未切片）
    page_size    : 每页条数，默认 10
    step         : 当前页左右各显示多少页码，默认 5
    page_param   : url 中页码的参数名，默认 "page"
    """

    def __init__(self, request, queryset,
                 page_size=10, step=5, page_param='page'):
        self.page_param = page_param
        self.page_size = page_size
        self.step = step
        self.queryset = queryset

        # 拿到当前页码
        try:
            self.page = int(request.GET.get(page_param, 1))
            if self.page < 1:
                self.page = 1
        except ValueError:
            self.page = 1

        # 计算总记录数 / 总页数
        total_count = self.queryset.count()
        total_page, remainder = divmod(total_count, self.page_size)
        if remainder:
            total_page += 1
        self.total_page = total_page or 1  # 至少 1 页

        # 切片
        start = (self.page - 1) * self.page_size
        end = start + self.page_size
        self.page_queryset = self.queryset[start:end]

        # 保存其它 get 参数，便于翻页后仍然保留搜索条件
        query_dict = request.GET.copy()
        query_dict.pop(page_param, None)  # 去掉 page 参数
        self.base_query = query_dict.urlencode()

    def html(self):
        """返回可直接渲染的 ul > li 字符串"""
        if self.total_page <= 1:
            return ''

        # 计算页码范围
        left = max(self.page - self.step, 1)
        right = min(self.page + self.step, self.total_page)
        if self.total_page <= 2 * self.step + 1:
            left, right = 1, self.total_page

        page_links = []

        # 上一页
        if self.page > 1:
            page_links.append(
                f'<li><a href="?{self._href(self.page - 1)}">上一页</a></li>'
            )
        else:
            page_links.append('<li class="disabled"><span>上一页</span></li>')

        # 数字页码
        for i in range(left, right + 1):
            active = ' class="active"' if i == self.page else ''
            page_links.append(
                f'<li{active}><a href="?{self._href(i)}">{i}</a></li>'
            )

        # 下一页
        if self.page < self.total_page:
            page_links.append(
                f'<li><a href="?{self._href(self.page + 1)}">下一页</a></li>'
            )
        else:
            page_links.append('<li class="disabled"><span>下一页</span></li>')

        # 跳转输入框
        jump_box = (
            '<li>'
            '<form style="display:inline-block;margin-left:10px;" method="get">'
            f'<input type="hidden" name="q" value="{self.base_query}">'
            '<input type="number" name="page" min="1" '
            f'max="{self.total_page}" style="width:60px;" '
            'class="form-control input-sm" required>'
            '<button class="btn btn-default btn-sm" type="submit">跳转</button>'
            '</form>'
            '</li>'
        )
        page_links.append(jump_box)

        return mark_safe(''.join(page_links))

    def _href(self, page):
        """生成带 page 以及其它 get 参数的 querystring"""
        base = f'{self.page_param}={page}'
        if self.base_query:
            base += '&' + self.base_query
        return base