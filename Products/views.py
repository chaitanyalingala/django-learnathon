from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def list_products(request):
    return JsonResponse([{
        "name": "Jwellery",
        "date": "31-03-2022 2:50:47",
        "price": "35",
        "image": "https://tribalapp.s3.us-east-2.amazonaws.com/media/a3863345acdb99ed26405e82fc8cfb5f.png",
    },
    {
        "name": "Cow Metal Craf",
        "date": "31-03-2022 3:24:57",
        "price": "85",
        "image": "https://tribalapp.s3.us-east-2.amazonaws.com/media/download.jpeg",
    },
    ], safe = False)

