from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from insta.models import Photo


def test(request):
    return HttpResponse("i am test!!")

def selectAll(request):
    list = Photo.objects.all()
    return render(request, 'insta/list.html',{"list":list})
class SelectOne(DetailView):
    model = Photo
    template_name = "insta/selectOne.html"
class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'insta/upload.html'

    # 저장 시 자동호출
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id  # 저장 시 로그인 id 자동 저장
        if form.is_valid():
            form.instance.save()
            return redirect('/insta/selectAll')
        else:
            return self.render_to_response({'form':form})

