from django.contrib import admin
from securityControl.models import Ziyaretci, Page, Taseron, yuk_arac, Calısan, havuz_arac

# Register your models here.


@admin.register(Ziyaretci)
class ZiyaretciAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "tc_kimlik_no",
    ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
    ]


@admin.register(Taseron)
class TaseronAdmin(admin.ModelAdmin):
    list_display = [
        "firma_adi",
        "is_inside",
    ]


@admin.register(yuk_arac)
class YukAracAdmin(admin.ModelAdmin):
    list_display = [
        "sofor",
        "cekici_plaka",
        "dorse_plaka",
        "firma_adi",
        "arac_turu",
        "is_inside",
        "created_at",
        "updated_at",
    ]


@admin.register(Calısan)
class CalisanAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "departman",
        "is_active",
    ]


@admin.register(havuz_arac)
class HavuzAdmin(admin.ModelAdmin):
    list_display = [
        "calisan",
        "plaka",
        "baslangic_km",
        "son_km",
        "net_km",
        "is_inside",
        "cikis_tarihi_saati",
        "giris_tarihi_saati",
    ]
