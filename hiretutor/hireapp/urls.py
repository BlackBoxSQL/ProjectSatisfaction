from django.urls import include, path

from .views import hireapp, tutor, guardian

urlpatterns = [
    path('', hireapp.index, name='home'),
    path('guardian/', include(([
                                   path('guardianhomepage/', guardian.GuardianHomepage.as_view(),
                                        name='guardian_homepage'),
                                   path('guardianprofile/', guardian.GuardianProfile.as_view(),
                                        name='guardian_profile'),
                               ], 'hireapp'), namespace='guardian')),
    path('tutor/', include(([
                                path('tutorhomepage/', tutor.TutorHomepage.as_view(),
                                     name='tutor_homepage'),
                                path('tutorprofile/', tutor.TutorProfile.as_view(),
                                     name='tutor_profile'),
                            ], 'hireapp'), namespace='tutor')),
]
