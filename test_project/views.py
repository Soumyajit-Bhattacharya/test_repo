from django.http import JsonResponse
from .models import test
from .serializers import testserializers

def test_list(request):
    # get all the test lists
    # serialize them
    # return json
    tests = test.objects.all()
    serializer = testserializers(tests, many=True)
    return JsonResponse(serializer.data, safe=False)