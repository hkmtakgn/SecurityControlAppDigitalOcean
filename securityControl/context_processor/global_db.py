from securityControl.models import Page


def global_sc_pages(request):
  g_sc_pages = Page.objects.filter(is_active=True)
  context = dict(g_sc_pages=g_sc_pages, )
  return context
