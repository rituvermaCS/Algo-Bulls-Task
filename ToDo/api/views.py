from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)


"""
Below Function going to read all the todo items store in the data base.
"""


@api_view(['GET'])
def taskList():
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


"""
Below Function going to read one todo item store in the data base.
"""


@api_view(['GET'])
def taskDetail(pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


"""
Below Function going to update one todo item store in the data base.
"""


@api_view(['PUT'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
Below Function going to create one todo item at a time.
"""


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
Below Function going to delete one todo item at a time which store in the data base.
"""


@api_view(['DELETE'])
def taskDelete(pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted successfully.")
