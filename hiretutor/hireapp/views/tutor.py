from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import tutor_required
from ..models import User, TutorProfiles, GuardianProfiles
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView, DetailView
from ..forms import TutorSignUpForm, CreateTutorProfile


class TutorSignUpView(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Tutor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tutor:tutor_homepage')


@method_decorator([login_required, tutor_required], name='dispatch')
class TutorHomepage(ListView):
    context_object_name = 'guardians'
    template_name = 'hireapp/tutor/tutor_homepage.html'
    model = GuardianProfiles
    paginate_by = 10
    queryset = GuardianProfiles.objects.all()


@method_decorator([login_required, tutor_required], name='dispatch')
class TutorProfile(CreateView):
    model = TutorProfiles
    form_class = CreateTutorProfile

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('tutor:tutor_homepage')
