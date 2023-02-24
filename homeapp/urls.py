from .views import (
    BlogListviews,
    BlogDelete,
    BlogEdit,
    BlogDetail,
    BlogNewView,
)
from django.urls import path


urlpatterns = [
    path('', BlogListviews.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('post/new/', BlogNewView.as_view(), name='post_new'),
    path('post/<int:pk>/delete/', BlogDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogEdit.as_view(), name='post_edit')

]
