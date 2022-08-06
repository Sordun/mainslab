import openpyxl
from rest_framework.response import Response
from rest_framework.views import APIView

from bills.models import Bill
from bills.serializers import FileUploadSerializer, BillSerializer, BillFilterSerializer


class BillsUpload(APIView):
    serializer_class = FileUploadSerializer

    def post(self, request):
        review = FileUploadSerializer(data=request.data)
        if not review.is_valid():
            return Response({"error": "file upload error"}, status=400)
        try:
            excel_file = openpyxl.load_workbook(request.FILES["file"])
            file = excel_file.active
            for row in file.rows:
                if row[0].row == 1 or row[0].value is None:
                    continue
                row_data = {
                    "client_name": row[0].value,
                    "client_org": row[1].value,
                    "number": row[2].value,
                    "sum": row[3].value,
                    "date": row[4].value.strftime("%Y-%m-%d"),
                    "service": row[5].value,
                }
                serializer = BillSerializer(data=row_data)
                if serializer.is_valid():
                    print("valid")
                    serializer.save()
                else:
                    print(serializer.errors)
        except Exception as e:
            return Response({f"error: {e}": "file parse error"}, status=400)
        return Response({"message": "successfully"}, status=200)


class BillsList(APIView):
    serializer_class = BillFilterSerializer

    def get(self, request):
        serialize = Bill.objects.all()
        result = BillSerializer(serialize, many=True).data
        return Response(result)

    def post(self, request):
        review = BillFilterSerializer(data=request.data)
        if not review.is_valid():
            return Response({"error": "error"}, status=400)
        if review.data.get("organization") and review.data.get("client"):
            serialize = Bill.objects.filter(
                client_org=review.data.get("organization"), client_name=review.data.get("client")
            )
        elif review.data.get("client"):
            serialize = Bill.objects.filter(client_name=review.data.get("client"))
        elif review.data.get("organization"):
            serialize = Bill.objects.filter(client_org=review.data.get("organization"))
        else:
            serialize = Bill.objects.all()
        result = BillSerializer(serialize, many=True).data
        return Response(result)
