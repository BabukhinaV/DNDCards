from django.shortcuts import render

from catalog.models import Player

def profile(request):
    players = Player.objects.filter(user_id=request.user.id).order_by('-level')
    return render(request, 'profile.html', {'players': players})


def show_history(request, p_id):
    pass