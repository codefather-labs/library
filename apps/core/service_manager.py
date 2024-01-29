import abc

from apps.library.services import DjangoInlineLibraryService
from apps.rent.services import DjangoInlineRentService
from services.interfaces import (
    IServiceManager, IRentService, ILibraryService
)


# For future scaling
class RemoveServiceManager(IServiceManager):

    def get_library_service(self) -> ILibraryService: ...

    def get_rent_service(self) -> IRentService: ...


class DjangoServiceManager(IServiceManager):
    def get_library_service(self) -> ILibraryService:
        return DjangoInlineLibraryService()

    def get_rent_service(self) -> IRentService:
        return DjangoInlineRentService()


service_manager: DjangoServiceManager = DjangoServiceManager()
