

from django import forms
from django.contrib.auth.forms import AuthenticationForm as LoginForm, UserCreationForm
from webapp.models import Flight, House, User


class Create_Flight(forms.ModelForm):
    flight_number = forms.CharField(required=True)
    date = forms.DateTimeField(required=True)

    class Meta:
        model = Flight
        fields = ('flight_number', 'date')


class Edit_Flight(forms.ModelForm):
    flight_number = forms.CharField(required=True)
    date = forms.DateTimeField(required=True)

    class Meta:
        model = Flight
        fields = ('flight_number', 'date')


class Create_House(forms.ModelForm):
    address = forms.CharField(required=True)
    size = forms.FloatField(required=True)

    class Meta:
        model = House
        fields = ('address', 'size')


class ShortSignupForm(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=20, required=True)

    def clean_email(self):
        existing = User.objects.filter(
            email__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(
                "A user with that email already exists.")
        else:
            return self.cleaned_data['email']

    def save(self):
        """
        If you call this on a valid bound form, it will create and return a user with the bound data.
        """

        user = User.objects.create_user(self.cleaned_data['email'].split(
            "@")[0], self.cleaned_data['email'], self.cleaned_data['password'])
        name_tokens = [t.strip()
                       for t in self.cleaned_data['name'].split() if t.strip() != ""]
        if len(name_tokens) == 1:
            name_tokens.append("")
        user.first_name, user.last_name = name_tokens[
            0], " ".join(name_tokens[1:])
        user.save()
        return user
