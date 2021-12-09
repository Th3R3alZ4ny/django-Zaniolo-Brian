from django.shortcuts import render

# Create your views here.
def chessGame(request):
    return render(request, "chessGame.html")

