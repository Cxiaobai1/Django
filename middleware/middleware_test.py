# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 14:39
# @Author  : Cxiaobai
# @Email   : 494158341@qq.com
# @File    : middleware_test.py
# @Software: PyCharm
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MiddleWareTest(MiddlewareMixin):
    url_list = {}
    forbidden_url = []

    def process_request(self, request):
        # print(request.META['REMOTE_ADDR'])
        # print(request.path_info)
        url = request.META['REMOTE_ADDR']
        if url in self.forbidden_url:
            return HttpResponse('访问次数达上限')
        if url not in self.url_list:
            times = self.url_list.get(url, 0)
            self.url_list[url] = times + 1
        else:
            self.url_list[url] += 1
        if self.url_list[url] > 5:
            self.forbidden_url.append(url)
            return HttpResponse('访问次数达上限')
        print(self.url_list)
        print(self.forbidden_url)
        return None


    def process_view(self, request, callback, callback_args, callback_kwargs):
        # print('view before')
        return None

    def process_response(self, request, response):
        # print('response back before')
        return response
