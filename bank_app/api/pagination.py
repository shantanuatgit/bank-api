from rest_framework.pagination import PageNumberPagination


class BankListPagination(PageNumberPagination):
    """List 10 objects per page"""
    page_size = 10
    page_query_param = 'page'

class BranchListPagination(PageNumberPagination):
    """List 20 objects per page"""
    page_size = 20
    page_query_param = 'page'