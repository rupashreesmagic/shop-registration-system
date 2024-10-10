from django import forms
from .models import Shop

class ShopRegistrationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']

    def clean_latitude(self):
        lat = self.cleaned_data.get('latitude')
        if lat < -90 or lat > 90:
            raise forms.ValidationError("Invalid latitude")
        return lat

    def clean_longitude(self):
        lon = self.cleaned_data.get('longitude')
        if lon < -180 or lon > 180:
            raise forms.ValidationError("Invalid longitude")
        return lon
