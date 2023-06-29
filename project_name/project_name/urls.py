from django.urls import path
from app_name.views import members, save_all_results, show_best_result
from app_name.views import save_all_results
urlpatterns = [
    path('', members, name='members'),
    path('save-all-results/', save_all_results, name='save_all_results'),
    path('show-best-result/', show_best_result, name='show_best_result'),
    # Add other URL patterns if needed
]
