from django.urls import path
from service.views import IndexView, FindRecipeView

app_name = 'service'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('find_recipe/', FindRecipeView.as_view(), name="find_recipe"),
]
