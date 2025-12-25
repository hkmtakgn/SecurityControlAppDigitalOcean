from django import forms
from django.db.models import fields
from django.forms import widgets
from securityControl.models import Ziyaretci, Taseron, yuk_arac, havuz_arac, Calısan


class ZiyaretciForm(forms.ModelForm):

    class Meta:
        model = Ziyaretci
        fields = "__all__"


class TaseronForm(forms.ModelForm):

    class Meta:
        model = Taseron
        fields = "__all__"

        exclude = ["is_inside", "is_outside"]


class yukAracForm(forms.ModelForm):

    class Meta:
        model = yuk_arac
        fields = "__all__"

        exclude = ["is_inside", "is_outside"]


class HavuzAracForm(forms.ModelForm):

    class Meta:
        model = havuz_arac
        fields = "__all__"

        exclude = [
            "is_inside",
        ]

        widgets = {
            "giris_tarihi_saati":
            forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control"
            }, ),
            "cikis_tarihi_saati":
            forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control"
            })
        }


class CalisanForm(forms.ModelForm):

    class Meta:
        model = Calısan
        fields = '__all__'

        exclude = [
            "is_active",
        ]
