from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import TodoSerializer

# Create your views here.


def index(request):
    return render(request, 'todo_app/index.html')


@api_view(["GET"])
def todo_list(request):
    response = Response()

    todos = TodoItem.objects.all()

    todo_serializer = TodoSerializer(todos, many=True)

    response.data = {
        'todos': todo_serializer.data
    }

    return response


@api_view(["POST"])
def create_todo(request):
    response = Response()

    # extract new todo from request data
    new_todo_text = request.data.get('new_todo_text')

    # instantiate TodoSerializer with text from the request
    todo_serialzer = TodoSerializer(data={'text': new_todo_text})

    # if serializer fields are valid
    if todo_serialzer.is_valid():
        # create new todo object in DB
        todo_serialzer.save()

    # pull all todos from DB
    todos = TodoItem.objects.all()

    # serialize
    todo_serialzer = TodoSerializer(todos, many=True)

    # attach data to response
    response.data = {
        'todos': todo_serialzer.data
    }

    return response


@api_view(["POST"])
def toggle_complete(request, todo_id):
    response = Response()

    # pass TodoItm class where classid = id passed in
    todo = get_object_or_404(TodoItem, id=todo_id)

    # flip boolean
    todo.completed = not todo.completed
    todo.save()

    # get all todos from DB
    todos = TodoItem.objects.all()

    # serialize
    todo_serialzier = TodoSerializer(todos, many=True)

    response.data = {
        'todos': todo_serialzier.data
    }

    return response


@api_view(["POST"])
def delete_todo(request, todo_id):
    response = Response()

    todo = get_object_or_404(TodoItem, id=todo_id)

    todo.delete()

    todos = TodoItem.objects.all()

    todo_serializer = TodoSerializer(todos, many=True)

    response.data = {
        'todos': todo_serializer.data
    }

    return response
