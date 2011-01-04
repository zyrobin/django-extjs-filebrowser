
from django.utils.functional import wraps
import utils

__all__ = ['ajax_request']


def ajax_request(func):
    """
    If view returned serializable dict, returns JsonResponse with this dict as content.

    example:
        
        @ajax_request
        def my_view(request):
            news = News.objects.all()
            news_titles = [entry.title for entry in news]
            return {'news_titles': news_titles}
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, dict):
            return utils.JsonResponse(response)
        elif isinstance(response, list):
            return utils.JsonResponse(response)
        else:
            return response
    return wrapper  