from django.urls import path

import insta.views

urlpatterns = [
    path('test',insta.views.test,name='test'),
    path('selectAll',insta.views.selectAll,name='selectAll'),
    path('selectOne/<int:pk>',insta.views.SelectOne.as_view() ,name='selectOne'),
    path('upload',insta.views.PhotoUploadView.as_view() ,name='upload'),
]
