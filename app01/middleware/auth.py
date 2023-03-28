
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

"""定义中间件"""


class M1(MiddlewareMixin):
    def process_request(self, req):
        #req.path_info获取当前用户请求的url
        if req.path_info in['/login/','/image/code/']:
            return
        #读取session信息
        info = req.session.get('info')
        if info:
            return
        #没有登陆过
        return redirect('/login/')
    # 如果没有返回值就继续往后走
    # 返回值 httpresponse，render，rediret

    def process_response(self, req, res):
        return res
