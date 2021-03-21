from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    def get_paginated_response(self, data):
        return Response(
            {
                'data': data,
                'meta': {
                    'category': self.request.GET.get('category') or '',
                    'page': self.page.number,
                    'page_size': self.request.GET.get(
                        'page_size'
                    ) or self.page_size,
                    'page_count': self.page.paginator.num_pages,
                    'total': self.page.paginator.count,
                }
            }
        )