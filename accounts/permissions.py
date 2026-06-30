from django.http import HttpResponse

# def check_admin(func):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             if request.user.role != 'admin':
#                 return HttpResponse('Access denied!')
#         else:
#             return HttpResponse('Access denied!')
#         return func(request, *args, **kwargs)
#     return wrapper
#
# def check_manager(func):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             if request.user.role != 'manager':
#                 return HttpResponse('Access denied!')
#         else:
#             return HttpResponse('Access denied!')
#         return func(request, *args, **kwargs)
#     return wrapper

def permit_creating(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.role in ['admin']:
                return HttpResponse('Access denied!')
        else:
            return HttpResponse('Access denied!')
        return func(request, *args, **kwargs)
    return wrapper

def permit_updating(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.role in ['admin', 'manager']:
                return HttpResponse('Access denied!')
        else:
            return HttpResponse('Access denied!')
        return func(request, *args, **kwargs)
    return wrapper

def permit_deleting(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.role in ['admin']:
                return HttpResponse('Access denied!')
        else:
            return HttpResponse('Access denied!')
        return func(request, *args, **kwargs)
    return wrapper