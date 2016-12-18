from django.db import connection
from django.template import Template, Context
from django.utils.deprecation import MiddlewareMixin

class SQLMiddleware(MiddlewareMixin):
    def process_response ( self, request, response ):
        t = sum([ float(i['time']) for i in connection.queries])
        c = len(connection.queries)
        stng= '<p style="color:#0b0">timeSum: %s, queryAmount: %s</p></body>'

        if 'content="text/html;' in response.content:
            response.content = response.content.replace('</body>', stng%(t,c))
        return response

class HeadStrMiddleware(MiddlewareMixin):
    def process_response ( self, request, response ):
        hh = '<div style="background-color:#9df;border:2px solid #00f;'\
                           'padding-right: 30px; border-radius:5px;">'\
               '<div style="text-align:left">'\
                 '<h1 ><a href="/">Back to HOME </a></h1>'\
               '</div>'\
               '<div style="text-align:right">'\
                 '<h3><a href="/students/logout/">Log out</a></h3>'\
               '</div>'\
             '</div>'

        if 'admin' not  in request.path:
            response.content = '%s%s' % (hh, response.content)
        return response



