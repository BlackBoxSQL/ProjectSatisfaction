from django.contrib.auth.forms import UserCreationForm
from hireapp.models import User, TutorProfiles
from django import forms
from . import models


class GuardianSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_guardian = True
        if commit:
            user.save()
        return user


class TutorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
        return user


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateTutorProfile(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['week'].widget.attrs.update({'placeholder': 'Example: 4'})
        self.fields['fees_per_subject'].widget.attrs.update({'placeholder': 'Example: 8000'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Example: +880XXXXXXXXXX'})
        self.fields['age'].widget.attrs.update({'placeholder': 'Example: 23'})
        self.fields['tution_you_give_to_class'].widget.attrs.update({'placeholder': 'Example: 8'})
        self.fields['subjects_you_teach'].widget.attrs.update(
            {'placeholder': 'Example: Bangla, Accounting, Higher-math'})
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Example:\nBarishal, Bhola, Lalmohan, Badarpur \n\nor\n\nDhanmondi. 32\nDhaka-1209\nBangladesh'})
        self.fields['nid_No'].widget.attrs.update({'placeholder': 'Example: 19956712231000890'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Why do you need this tuition & What you have to offer to the client (guardian)?'})
        self.fields['tution_hour'].widget.attrs.update(
            {'placeholder': 'Example: 1.5 hours'})

    class Meta:
        model = models.TutorProfiles
        fields = [
            'Your_Full_Name',
            'gender',
            'age',
            'Date_of_Birth',
            'image',
            'address',
            'nid_No',
            'tution_you_give_to_class',
            'subjects_you_teach',
            'phone_number',
            'need_tution_from',
            'week',
            'description',
            'fees_per_subject',
            'tution_hour',
        ]
        widgets = {
            'Date_of_Birth': DateInput(),
            'need_tution_from': DateInput(),

        }


class CreateGuardianProfile(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nid_No'].widget.attrs.update({'placeholder': 'Example: 19956712231000890'})
        self.fields['occupation'].widget.attrs.update({'placeholder': 'Example: Doctor, Businessman, Engineer'})
        self.fields['s_class'].widget.attrs.update({'placeholder': 'Example: 9'})
        self.fields['school'].widget.attrs.update({'placeholder': 'Example: I.E.T. Govt. High School'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Example: Biology, Economics, Physics'})
        self.fields['payment'].widget.attrs.update({'placeholder': 'Example: 1200'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Example: Dhaka, Narayanaganj'})
        self.fields['tution_hour'].widget.attrs.update({'placeholder': 'Example: 2'})
        self.fields['guardian_contact'].widget.attrs.update({'placeholder': 'Example: +880XXXXXXXXXX'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': "Tell us about student's weakness in subjects, how to treat the student?"})

    class Meta:
        model = models.GuardianProfiles
        fields = [
            'Guardians_name',
            'gender',
            'nid_No',
            'occupation',
            'students_name',
            's_class',
            'school',
            'subject',
            'payment',
            'tution_hour',
            'guardian_contact',
            'need_tutor_from',
            'description',
            'address',
        ]
        widgets = {
            'need_tutor_from': DateInput(),
        }
