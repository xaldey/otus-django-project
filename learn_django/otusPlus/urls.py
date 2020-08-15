from django.urls import path


from learn_django.otusPlus.views.views import index_view
import learn_django.otusPlus.views.cb_views as class_based_views
# from .views.cb_views import

app_name = 'otusPlus'

urlpatterns = [
    path('', index_view, name='index'),
    # Class based views
    # path('cb_course_list/', class_based_views.CourseListView.as_view()),
    path('cb_course_create/', class_based_views.CreateCourseView.as_view()),
    # path('cb_course_detail/<int:pk>', class_based_views.CourseDetailView.as_view()),
    # path('cb_course_list/', class_based_views.CourseListView.as_view()),
]