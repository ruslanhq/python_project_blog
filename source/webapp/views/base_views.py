from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView


class ListView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_objects()
        return context

    def get_objects(self):
        return self.model.objects.all()


# class IndexView(ListView):
#     context_key = 'articles'
#     model = Article
#     template_name = 'article/index.html'
#
#     def get_objects(self):
#         return super().get_objects().order_by('-created_at')


class CreateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            self.object = self.model.objects.create(**form.cleaned_data)
            return redirect(self.get_redirect_url())
        else:
            return render(request, self.template_name, context={'form': form})

    def get_redirect_url(self):
        return self.redirect_url


class UpdateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None
    pk_kwargs_page = 'pk'
    context_object_name = None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instace=self.object)
        return render(request, self.template_name, context={'form': form, self.context_object_name: self.object})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.object =  get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance= self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return self.redirect_url

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})
