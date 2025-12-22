from django.shortcuts import render

from catalog.models import History, InventoryItem, PClass, Race, Skill, Spell

def home(request):
    return render(request, 'home.html', {})


def races(request):
    races = Race.objects.all()
    return render(request, 'races.html', {'races': races})


def race_info(request, r_id):
    race = Race.objects.get(pk=r_id)
    return render(request, 'race_info.html', {'race': race})


def pclasses(request):
    pclasses = PClass.objects.all()
    return render(request, 'pclasses.html', {'pclasses': pclasses})


def pclass_info(request, p_id):
    pclass = PClass.objects.get(pk=p_id)
    return render(request, 'pclass_info.html', {'pclass': pclass})


def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})


def items(request): 
    items = InventoryItem.objects.all().order_by("category") 
    return render(request, 'items.html', {'items': items})


def histories(request): 
    histories = History.objects.all()
    return render(request, 'histories.html', {'histories': histories})


def spells(request): 
    spells = Spell.objects.all()
    return render(request, 'spells.html', {'spells': spells})