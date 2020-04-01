from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'transcendence/user_detail.html', {'user': user})
