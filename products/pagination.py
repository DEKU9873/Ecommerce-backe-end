from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 8  
    page_size_query_param = 'limit'  
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'paginationResult': {
                'currentPage': self.page.number,
                'numberOfPages': self.page.paginator.num_pages,
                'limit': self.page.paginator.per_page,
            },
            'data': data
        })
