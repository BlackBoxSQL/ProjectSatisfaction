from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import guardian_required
from ..models import User, GuardianProfiles, TutorProfiles
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from ..forms import GuardianSignUpForm, CreateGuardianProfile


class GuardianSignUpView(CreateView):
    model = User
    form_class = GuardianSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Guardian'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('guardian:guardian_homepage')


@method_decorator([login_required, guardian_required], name='dispatch')
class GuardianHomepage(ListView):
    context_object_name = 'tutors'
    template_name = 'hireapp/guardian/guardian_homepage.html'
    model = TutorProfiles
    paginate_by = 10
    queryset = TutorProfiles.objects.all()


@method_decorator([login_required, guardian_required], name='dispatch')
class GuardianProfile(CreateView):
    model = GuardianProfiles
    form_class = CreateGuardianProfile

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('guardian:guardian_homepage')
