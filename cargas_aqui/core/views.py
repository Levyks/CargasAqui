from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Cargo

def listCargoes(request):

    cargoes = Cargo.objects \
        .filter(status__code='EM_CONTRATACAO') \
        .select_related('state', 'status')

    page_number = request.GET.get('page', 1)

    try:
        page_size = int(request.GET.get('size', 10))
        if page_size < 1 or page_size > 50:
            page_size = 10
    except ValueError:
        page_size = 10

    paginator = Paginator(cargoes, page_size)
    page = paginator.get_page(page_number)

    return render(request, 'cargas/list.html', { 'cargoes': page })