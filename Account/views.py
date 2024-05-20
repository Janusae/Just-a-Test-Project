from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import User_plus , User
from .form import UserEditForm
# Create your views here.
def dashboard(request):
    user = User.objects.get(id=request.user.id)
    user_plus = User_plus.objects.get(user_id__exact=user.id)
    return render(request , "Dashboard.html" , {"user" : user, "user_plus" : user_plus})
class Edit_DashboardView(View):
    def get(self, request):
        form = UserEditForm()
        return render(request, "Edit.html", {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = UserEditForm(request.POST , request.FILES)
            user = User_plus.objects.get(user_id__exact=request.user.id)
            if form.is_valid():
                user.about_user = request.POST["about_user"]
                user.avatar = request.FILES["avatar"]
                user.save()
                return redirect(reverse("dashboard"))
        # If form is not valid, return to the same page with the form data
        return render(request, "Edit.html", {"form": form})

