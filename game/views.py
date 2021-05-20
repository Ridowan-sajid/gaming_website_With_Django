from urllib import request
from django.shortcuts import render
from game.models import Game,Comment
from game.forms import GameForm

def home(request):
    posts = Game.objects.all()
    context = {
        "posts": posts
    }

    return render(request, "game/home.html", context)

def gamingPost(request,pk):
    post=Game.objects.get(id=pk)
    # images=GameImage.objects.all()
    context={
        "post":post,
        # "images":images
    }

    return render(request,"game/game_details.html",context)

def gaming_comment(request):
    comment_form=GameForm()
    if request.method == "POST":
        comment_form = GameForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(**comment_form)

    context={
        "comment_form":comment_form,
    }

    return render(request,"game/game_details.html",context)


