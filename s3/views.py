from django.shortcuts import render
from .forms import UploadForm
from django.views.generic.edit import FormView
from .models import Post


class UploadView(FormView):
    template_name = 's3/index.html'
    form_class = UploadForm
    success_url = '/'
    
    def get_context_data(self, *args,**kwargs) :
        context =  super().get_context_data(*args, **kwargs)
        posts = Post.objects.all()
        context.update({
            'posts':posts
        })

        return context

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
