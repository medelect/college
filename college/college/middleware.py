from django.db import connection
from django.template import Template, Context
from django.utils.deprecation import MiddlewareMixin

class SQLMiddleware(MiddlewareMixin):
    def process_response ( self, request, response ):
        t = sum([ float(i['time']) for i in connection.queries])
        c = len(connection.queries)
        stng= '<p style="color:#0b0">timeSum: %s, queryAmount: %s</p>'
        response.content = '%s%s' % ( response.content, stng%(t,c))

        return response


