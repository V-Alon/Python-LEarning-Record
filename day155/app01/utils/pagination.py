"""
自定义的分页组件
"""
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self,request,pretty_mobile_queryset,page_size=10,step = 5,page_param="page"):
        page = int(request.GET.get(page_param,"1"))
        if "".isdecimal():
            page = int(page)
        else:
            page = 1
        self.page=page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = pretty_mobile_queryset[self.start:self.end]

        # 数据总条数
        total_count = pretty_mobile_queryset.count()

        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.step = step


    def html(self):

        # 计算出 当前显示的前五页后五页

        if self.total_page_count <= 2 * self.step + 1:
            start_page = 1
            end_page = self.total_page_count + 1
        else:
            if self.page <= self.step:
                start_page = 1
                end_page = 2 * self.step + 1
            else:
                if (self.page + self.step) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.step + 1
                    end_page = self.total_page_count + 1
                else:
                    start_page = self.page - self.step
                    end_page = self.page + self.step + 1

        # 页码
        # <li><a href="?page=1">1</a></li>
        page_str_list = []

        # 上一页
        if self.page > 1:
            prev = '<li><a href="?page={}">上一页</a></li>'.format(self.page - 1)
        else:
            prev = '<li class="disabled"><a href="?page={}">上一页</a></li>'.format(1)

        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page):
            if i == self.page:
                ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li><a  href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)

        # 下一页按钮
        if self.page < self.total_page_count:
            next_page = '<li><a href="?page={}">下一页</a></li>'.format(self.page + 1)
        else:
            next_page = '<li class="disabled"><a>下一页</a></li>'  # 禁用样式可选

        page_str_list.append(next_page)

        search_string = """<li>
        		<form style="float: left; margin-left: -1px;"  method="get">
        				<input type="text" name="page" class="form-control" placeholder="页码"
        				       style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0">
        					<button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
        		</form>
        	</li>"""
        page_str_list.append(search_string)

        page_string = mark_safe(''.join(page_str_list))


        return page_string