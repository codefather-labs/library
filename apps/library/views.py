import datetime

from django.shortcuts import render
from django.core.paginator import Paginator

from apps.core.service_manager import service_manager
from apps.library.models import Author, Book
from apps.rent.models import Rent
from services.interfaces import ILibraryService, IRentService


def get_author_by_name(request, name):
    library: ILibraryService = service_manager.get_library_service()
    author: Author = library.get_author_by_name(name)
    return render(request, 'library/author.html', {'author': author})


def index(request):
    rent_service: IRentService = service_manager.get_rent_service()
    paginator: Paginator = Paginator(
        rent_service.get_all_rent(), per_page=25
    )

    page_number = request.GET.get("page", 1)
    page_obj = paginator.page(page_number)

    return render(request, 'library/index.html', {
        "page_obj": page_obj
    })
