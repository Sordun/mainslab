from django.urls import path

from bills.views import BillsUpload, BillsList

urlpatterns = [
    path("upload/bills/", BillsUpload.as_view()),
    path("bills/", BillsList.as_view()),
]
