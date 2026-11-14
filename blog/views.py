from django.shortcuts import redirect, render

from .models import Review


def home(request):
    return render(request, "blog/home.html")


def about(request):
    return render(request, "blog/about.html")


def post(request):
    return render(request, "blog/post.html")


def reviews(request):
    if request.method == "POST":
        Review.objects.create(
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            text=request.POST["text"],
        )
        return redirect("blog:reviews")

    data = {"reviews": Review.objects.filter(approved=True)}
    return render(request, "blog/reviews.html", data)
