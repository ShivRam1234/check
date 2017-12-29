from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView, DetailView, ListView
from django.views.generic.edit import FormMixin
from filmitouch.forms import ContForm1, JoinForm
from filmitouch.models import Blog


class HomeView(ListView):
    model = Blog
    template_name = 'index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories1 = Blog.objects.all().filter(sub_cat__cat_name='Fitness Tips',
                                                     categories__cat_name='Health-Fitness')
        self.categories2 = Blog.objects.all().filter(sub_cat__cat_name='Workouts',
                                                     categories__cat_name='Health-Fitness')
        self.categories3 = Blog.objects.all().filter(sub_cat__cat_name='Nutrition',
                                                     categories__cat_name='Health-Fitness')
        self.categories4 = Blog.objects.all().filter(sub_cat__cat_name='Remedies',
                                                     categories__cat_name='Health-Fitness')
        self.categories5 = Blog.objects.all().filter(sub_cat__cat_name='Football',
                                                     categories__cat_name='Sports')
        self.categories6 = Blog.objects.all().filter(sub_cat__cat_name='Cricket',
                                                     categories__cat_name='Sports')
        self.categories7 = Blog.objects.all().filter(sub_cat__cat_name='IPL',
                                                     categories__cat_name='Sports')
        self.categories8 = Blog.objects.all().filter(sub_cat__cat_name='Olympics',
                                                     categories__cat_name='Sports')
        self.categories9 = Blog.objects.all().filter(sub_cat__cat_name='Other',
                                                     categories__cat_name='Sports')
        self.categories10 = Blog.objects.all().filter(sub_cat__cat_name='Computer',
                                                      categories__cat_name='Technology')
        self.categories11 = Blog.objects.all().filter(sub_cat__cat_name='Smart Phone',
                                                      categories__cat_name='Technology')
        self.categories12 = Blog.objects.all().filter(sub_cat__cat_name='Camera',
                                                      categories__cat_name='Technology')
        self.categories13 = Blog.objects.all().filter(sub_cat__cat_name='Laptop',
                                                      categories__cat_name='Technology')
        self.categories14 = Blog.objects.all().filter(sub_cat__cat_name='Action',
                                                      categories__cat_name='Bollywood')
        self.categories15 = Blog.objects.all().filter(sub_cat__cat_name='Comedy',
                                                      categories__cat_name='Bollywood')
        self.categories16 = Blog.objects.all().filter(sub_cat__cat_name='Drama',
                                                      categories__cat_name='Bollywood')
        self.categories17 = Blog.objects.all().filter(sub_cat__cat_name='Action',
                                                      categories__cat_name='Hollywood')
        self.categories18 = Blog.objects.all().filter(sub_cat__cat_name='Comedy',
                                                      categories__cat_name='Hollywood')
        self.categories19 = Blog.objects.all().filter(sub_cat__cat_name='Animation',
                                                      categories__cat_name='Hollywood')
        self.categories20 = Blog.objects.all().filter(sub_cat__cat_name='Sci-Fi',
                                                      categories__cat_name='Hollywood')
        self.categories21 = Blog.objects.all().filter(sub_cat__cat_name='Destination',
                                                      categories__cat_name='Travel')
        self.categories22 = Blog.objects.all().filter(sub_cat__cat_name='Collection',
                                                      categories__cat_name='Fashion')
        self.categories23 = Blog.objects.all().filter(sub_cat__cat_name='Stars',
                                                      categories__cat_name='Fashion')
        self.categories24 = Blog.objects.all().filter(sub_cat__cat_name='Cars',
                                                      categories__cat_name='Cars')
        self.categories25 = Blog.objects.all().filter(sub_cat__cat_name='Nature',
                                                      categories__cat_name='Nature Beauty'
                                                      )

    def get_queryset(self):
        context = {
            self.categories1,
            self.categories2,
            self.categories3,
            self.categories4,
            self.categories5,
            self.categories6,
            self.categories7,
            self.categories8,
            self.categories9,
            self.categories10,
            self.categories11,
            self.categories12,
            self.categories13,
            self.categories14,
            self.categories15,
            self.categories16,
            self.categories17,
            self.categories18,
            self.categories19,
            self.categories20,
            self.categories21,
            self.categories22,
            self.categories23,
            self.categories24,
            self.categories25,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['articles'] = Blog.objects.all()[:8]
        context['articles1'] = self.categories1
        context['articles2'] = self.categories2
        context['articles3'] = self.categories3
        context['articles4'] = self.categories4
        context['articles5'] = self.categories5
        context['articles6'] = self.categories6
        context['articles7'] = self.categories7
        context['articles8'] = self.categories8
        context['articles9'] = self.categories9
        context['articles10'] = self.categories10
        context['articles11'] = self.categories11
        context['articles12'] = self.categories12
        context['articles13'] = self.categories13
        context['articles14'] = self.categories14
        context['articles15'] = self.categories15
        context['articles16'] = self.categories16
        context['articles17'] = self.categories17
        context['articles18'] = self.categories18
        context['articles19'] = self.categories19
        context['articles20'] = self.categories20
        context['articles21'] = self.categories21
        context['articles22'] = self.categories22
        context['articles23'] = self.categories23
        context['articles24'] = self.categories24
        context['articles25'] = self.categories25
        return context


class BlogDetailView(FormMixin, DetailView):
    form_class = JoinForm
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'slug': self.object.slug})

    def get_object(self):
        try:
            my_object = Blog.objects.get(slug=self.kwargs.get('slug'))
            return my_object
        except self.model.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['articles1'] = Blog.objects.all().filter(sub_cat__cat_name='Fitness Tips',
                                                         categories__cat_name='Health-Fitness').order_by('-datetime')[:1]
        context['articles2'] = Blog.objects.all().filter(sub_cat__cat_name='Workouts',
                                                         categories__cat_name='Health-Fitness').order_by('-datetime')[:1]
        context['articles3'] = Blog.objects.all().filter(sub_cat__cat_name='Nutrition',
                                                         categories__cat_name='Health-Fitness').order_by('-datetime')[:1]
        context['articles4'] = Blog.objects.all().filter(sub_cat__cat_name='Remedies',
                                                         categories__cat_name='Health-Fitness').order_by('-datetime')[:1]
        context['articles5'] = Blog.objects.all().filter(sub_cat__cat_name='Football',
                                                         categories__cat_name='Sports').order_by('-datetime')[:1]
        context['articles6'] = Blog.objects.all().filter(sub_cat__cat_name='Cricket',
                                                         categories__cat_name='Sports').order_by('-datetime')[:1]
        context['articles7'] = Blog.objects.all().filter(sub_cat__cat_name='IPL',
                                                         categories__cat_name='Sports').order_by('-datetime')[:1]
        context['articles8'] = Blog.objects.all().filter(sub_cat__cat_name='Olympics',
                                                         categories__cat_name='Sports').order_by('-datetime')[:1]
        context['articles9'] = Blog.objects.all().filter(sub_cat__cat_name='Other',
                                                         categories__cat_name='Sports').order_by('-datetime')[:1]
        context['articles10'] = Blog.objects.all().filter(sub_cat__cat_name='Computer',
                                                          categories__cat_name='Technology').order_by('-datetime')[:1]
        context['articles11'] = Blog.objects.all().filter(sub_cat__cat_name='Smart Phone',
                                                          categories__cat_name='Technology').order_by('-datetime')[:1]
        context['articles12'] = Blog.objects.all().filter(sub_cat__cat_name='Camera',
                                                          categories__cat_name='Technology').order_by('-datetime')[:1]
        context['articles13'] = Blog.objects.all().filter(sub_cat__cat_name='Laptop',
                                                          categories__cat_name='Technology').order_by('-datetime')[:1]
        context['articles14'] = Blog.objects.all().filter(sub_cat__cat_name='Action',
                                                          categories__cat_name='Bollywood').order_by('-datetime')[:1]
        context['articles15'] = Blog.objects.all().filter(sub_cat__cat_name='Comedy',
                                                          categories__cat_name='Bollywood').order_by('-datetime')[:1]
        context['articles16'] = Blog.objects.all().filter(sub_cat__cat_name='Drama',
                                                          categories__cat_name='Bollywood').order_by('-datetime')[:1]
        context['articles17'] = Blog.objects.all().filter(sub_cat__cat_name='Action',
                                                          categories__cat_name='Hollywood').order_by('-datetime')[:1]
        context['articles18'] = Blog.objects.all().filter(sub_cat__cat_name='Comedy',
                                                          categories__cat_name='Hollywood').order_by('-datetime')[:1]
        context['articles19'] = Blog.objects.all().filter(sub_cat__cat_name='Animation',
                                                          categories__cat_name='Hollywood').order_by('-datetime')[:1]
        context['articles20'] = Blog.objects.all().filter(sub_cat__cat_name='Sci-Fi',
                                                          categories__cat_name='Hollywood').order_by('-datetime')[:1]
        context['articles21'] = Blog.objects.all().filter(sub_cat__cat_name='Destination',
                                                          categories__cat_name='Travel').order_by('-datetime')[:1]
        context['articles22'] = Blog.objects.all().filter(sub_cat__cat_name='Collection',
                                                          categories__cat_name='Fashion').order_by('-datetime')[:1]
        context['articles23'] = Blog.objects.all().filter(sub_cat__cat_name='Stars',
                                                          categories__cat_name='Fashion').order_by('-datetime')[:1]
        context['articles24'] = Blog.objects.all().filter(sub_cat__cat_name='Cars',
                                                          categories__cat_name='Cars').order_by('-datetime')[:1]
        context['articles25'] = Blog.objects.all().filter(sub_cat__cat_name='Nature',
                                                          categories__cat_name='Nature Beauty').order_by('-datetime')[:1]
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super(BlogDetailView, self).form_valid(form)

    def form_invalid(self, form):
        # put logic here
        return super(BlogDetailView, self).form_invalid(form)


class ContactView1(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContForm1
    success_url = '/contact'

    def form_valid(self, form):
        form.save()
        return super(ContactView1, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return "Thank You For Contacting Us"


def search_status(request):
    if request.method == "GET":
        search_text = request.GET['search_text']
        if search_text is not None and search_text != " ":
            search_text = request.GET['search_text']
            statuss = Blog.objects.filter(title__contains=search_text)
        return render(request, 'ajax_search.html', {'statuss': statuss})


def mobi_search(request):
    if request.method == "GET":
        search_text1 = request.GET['search_text1']
        if search_text1 is not None and search_text1 != " ":
            search_text1 = request.GET['search_text1']
            statuss1 = Blog.objects.filter(title__contains=search_text1)
        return render(request, 'mobile_search.html', {'statuss1': statuss1})


class HealthView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories1 = Blog.objects.all().filter(sub_cat__cat_name='Fitness Tips',
                                                     categories__cat_name='Health-Fitness')
        self.categories2 = Blog.objects.all().filter(sub_cat__cat_name='Workouts',
                                                     categories__cat_name='Health-Fitness')
        self.categories3 = Blog.objects.all().filter(sub_cat__cat_name='Nutrition',
                                                     categories__cat_name='Health-Fitness')
        self.categories4 = Blog.objects.all().filter(sub_cat__cat_name='Remedies',
                                                     categories__cat_name='Health-Fitness')

    def get_queryset(self):
        context = {
            self.categories1,
            self.categories2,
            self.categories3,
            self.categories4,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(HealthView, self).get_context_data(**kwargs)
        context['articles1'] = self.categories1
        context['articles2'] = self.categories2
        context['articles3'] = self.categories3
        context['articles4'] = self.categories4
        return context


class SportView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories5 = Blog.objects.all().filter(sub_cat__cat_name='Football',
                                                     categories__cat_name='Sports')
        self.categories6 = Blog.objects.all().filter(sub_cat__cat_name='Cricket',
                                                     categories__cat_name='Sports')
        self.categories7 = Blog.objects.all().filter(sub_cat__cat_name='IPL',
                                                     categories__cat_name='Sports')
        self.categories8 = Blog.objects.all().filter(sub_cat__cat_name='Olympics',
                                                     categories__cat_name='Sports')
        self.categories9 = Blog.objects.all().filter(sub_cat__cat_name='Other',
                                                     categories__cat_name='Sports')

    def get_queryset(self):
        context = {
            self.categories5,
            self.categories6,
            self.categories7,
            self.categories8,
            self.categories9,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(SportView, self).get_context_data(**kwargs)
        context['articles5'] = self.categories5
        context['articles6'] = self.categories6
        context['articles7'] = self.categories7
        context['articles8'] = self.categories8
        context['articles9'] = self.categories9
        return context


class TechnologyView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories10 = Blog.objects.all().filter(sub_cat__cat_name='Computer',
                                                      categories__cat_name='Technology')
        self.categories11 = Blog.objects.all().filter(sub_cat__cat_name='Smart Phone',
                                                      categories__cat_name='Technology')
        self.categories12 = Blog.objects.all().filter(sub_cat__cat_name='Camera',
                                                      categories__cat_name='Technology')
        self.categories13 = Blog.objects.all().filter(sub_cat__cat_name='Laptop',
                                                      categories__cat_name='Technology')

    def get_queryset(self):
        context = {
            self.categories10,
            self.categories11,
            self.categories12,
            self.categories13,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(TechnologyView, self).get_context_data(**kwargs)
        context['articles10'] = self.categories10
        context['articles11'] = self.categories11
        context['articles12'] = self.categories12
        context['articles13'] = self.categories13
        return context


class BolView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories14 = Blog.objects.all().filter(sub_cat__cat_name='Action',
                                                      categories__cat_name='Bollywood')
        self.categories15 = Blog.objects.all().filter(sub_cat__cat_name='Comedy',
                                                      categories__cat_name='Bollywood')
        self.categories16 = Blog.objects.all().filter(sub_cat__cat_name='Drama',
                                                      categories__cat_name='Bollywood')

    def get_queryset(self):
        context = {
            self.categories14,
            self.categories15,
            self.categories16,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(BolView, self).get_context_data(**kwargs)
        context['articles14'] = self.categories14
        context['articles15'] = self.categories15
        context['articles16'] = self.categories16
        return context


class HolView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories17 = Blog.objects.all().filter(sub_cat__cat_name='Action',
                                                      categories__cat_name='Hollywood')
        self.categories18 = Blog.objects.all().filter(sub_cat__cat_name='Comedy',
                                                      categories__cat_name='Hollywood')
        self.categories19 = Blog.objects.all().filter(sub_cat__cat_name='Animation',
                                                      categories__cat_name='Hollywood')
        self.categories20 = Blog.objects.all().filter(sub_cat__cat_name='Sci-Fi',
                                                      categories__cat_name='Hollywood')

    def get_queryset(self):
        context = {
            self.categories17,
            self.categories18,
            self.categories19,
            self.categories20,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(HolView, self).get_context_data(**kwargs)
        context['articles17'] = self.categories17
        context['articles18'] = self.categories18
        context['articles19'] = self.categories19
        context['articles20'] = self.categories20
        return context


class TravelView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories21 = Blog.objects.all().filter(sub_cat__cat_name='Destination',
                                                      categories__cat_name='Travel')

    def get_queryset(self):
        context = {
            self.categories21,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(TravelView, self).get_context_data(**kwargs)
        context['articles21'] = self.categories21
        return context


class FashionView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories22 = Blog.objects.all().filter(sub_cat__cat_name='Collection',
                                                      categories__cat_name='Fashion')
        self.categories23 = Blog.objects.all().filter(sub_cat__cat_name='Stars',
                                                      categories__cat_name='Fashion')

    def get_queryset(self):
        context = {
            self.categories22,
            self.categories23,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(FashionView, self).get_context_data(**kwargs)
        context['articles22'] = self.categories22
        context['articles23'] = self.categories23
        return context


class CarView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories24 = Blog.objects.all().filter(sub_cat__cat_name='Cars',
                                                      categories__cat_name='Cars')

    def get_queryset(self):
        context = {
            self.categories24,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(CarView, self).get_context_data(**kwargs)
        context['articles24'] = self.categories24
        return context


class NatureView(ListView):
    model = Blog
    template_name = 'categories.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categories25 = Blog.objects.all().filter(sub_cat__cat_name='Nature',
                                                      categories__cat_name='Nature Beauty')

    def get_queryset(self):
        context = {
            self.categories25,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super(NatureView, self).get_context_data(**kwargs)
        context['articles25'] = self.categories25
        return context