from django.db import connection
from django.template import Template, Context
from django.utils.deprecation import MiddlewareMixin

class SQLMiddleware(MiddlewareMixin):
    def process_response ( self, request, response ):
        h = '<p style="background-color: #9df; border: 2px solid #00f;'\
                'border-radius: 5px;">' \
                '<a href="/">Back to HOME</a></p>'
        t = sum([ float(i['time']) for i in connection.queries])
        c = len(connection.queries)
        stng= '<p style="color:#0b0">timeSum: %s, queryAmount: %s</p>'
        response.content = '%s%s%s' % (h, response.content, stng%(t,c))

        return response


