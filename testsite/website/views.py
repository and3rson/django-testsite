from django.shortcuts import render, get_object_or_404
from models import Page


def view_page(request, page_slug):
    if not page_slug:
        page = get_object_or_404(Page, is_main_page=True)
    else:
        page = get_object_or_404(Page, slug=page_slug)
    pages = Page.objects.order_by('name')
    return render(request, 'templates/page.html', dict(
        page=page,
        pages=pages
    ))
