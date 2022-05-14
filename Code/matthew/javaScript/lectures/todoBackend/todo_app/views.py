
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
# import decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import models
from .models import TodoItem
# import serializer
from .serializers import TodoSerializer

# Create your views here.
def index(request):
    return render(request, 'todo_app/index.html')

# for a GET request
@api_view(["GET"])
def todo_list(request):
    response= Response()
    
    todos=TodoItem.objects.all()           # many=True allows handling of multiple obj
    todo_serializer= TodoSerializer(todos, many=True) 

    response.data={
        'todos':todo_serializer.data
    }

    # calling rest api view 
    return response 

@api_view(["POST"])
def create_todo(request):
    response= Response() # instantiate/create empty response object

    # extracting new todo from request data
    new_todo_text= request.data.get('new_todo_text')

    # instantiate todo serializer with text from the request
    todo_serializer= TodoSerializer(data={'text':new_todo_text})

    # if serializer fields are valid 
    if todo_serializer.is_valid():
        # create a new todo object in our backend database:db
        todo_serializer.save()
    
    # get all todos from db 
    todos=TodoItem.objects.all()

    # serialize/convert objects to js friendly 
    todo_serializer=TodoSerializer(todos, many=True)

    # attach todo data to response object
    response.data={
        'todos':todo_serializer.data
    }
    return response 

@api_view(["POST"])
def toggle_complete(request, todo_id):
    # print(todo_id)
    response= Response()
    # pass the todoItem where the class id = id passed in view
    todo= get_object_or_404(TodoItem, id=todo_id)
    
    #flip the completed value 
    todo.completed = not todo.completed
    todo.save()

    # get all the todos from db
    todos= TodoItem.objects.all()

    # serialize all objects
    todo_serializer= TodoSerializer(todos, many=True)
    response.data={
        'todos':todo_serializer.data
    }
    return response

@api_view(["POST"])
def todo_delete(request, todo_id):
    response= Response()
    # get todo item
    todo= get_object_or_404(TodoItem, id=todo_id)
    # delete todo item
    todo.delete()

    # get all
    todos= TodoItem.objects.all()
    # serialize all
    todo_serializer= TodoSerializer(todos, many=True)

    response.data={
        'todos':todo_serializer.data
    }
    return response