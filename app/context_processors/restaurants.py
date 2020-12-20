def restaurants(request):
    from app.models import Restaurant
    return {'restaurants': Restaurant.objects.all()}

