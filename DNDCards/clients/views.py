from django.shortcuts import render
from catalog.models import History, PClass, PClassSkill, Player, PlayerSkill, PlayerSpell, Race
from django.contrib import messages

def profile(request):
    players = Player.objects.filter(user_id=request.user.id).order_by('-level')
    return render(request, 'profile.html', {'players': players})


def show_history(request, p_id):
    player = Player.objects.get(pk=p_id)
    skills = PlayerSkill.objects.filter(player_id=player.id)
    spells = PlayerSpell.objects.filter(player_id=player.id)
    return render(request, 'player_history.html', {'player': player, 'skills': skills, 'spells': spells})


def delete_character(request, p_id):
    player = Player.objects.get(pk=p_id)
    p_skills = PlayerSkill.objects.filter(player_id=player.id)
    p_skills.delete()
    player.delete()    
    players = Player.objects.filter(user_id=request.user.id).order_by('-level')
    messages.success(request, ("Вы удалили персонажа."))
    return render(request, 'profile.html', {'players': players})


def create_player(request):
    if request.method == "POST":
        pname = request.POST['pname']
        race_id = request.POST['prace']
        pclass_id = request.POST['pcl']
        history_id = request.POST['phistory']
        img = request.POST.get('img', None)    #request.POST['img']  
        race = Race.objects.get(pk=race_id)
        pclass = PClass.objects.get(pk=pclass_id)
        history = History.objects.get(pk=history_id)
        player = Player(name=pname, level=1, pclass=pclass, race=race, exp=0, history=history, user=request.user, img = 'images/' + str(img))        
        player.save()

        base_skills = PClassSkill.objects.filter(pclass_id=pclass_id)
        for base_skill in base_skills:
            player_skill = PlayerSkill(skill=base_skill.skill, svalue=base_skill.svalue, player=player)
            player_skill.save()   

        messages.success(request, ("Персонаж добавлен."))  
        players = Player.objects.filter(user_id=request.user.id).order_by('-level')      
        return render(request, 'profile.html', {'players': players})    
    else:
        races = Race.objects.all()
        pclasses = PClass.objects.all()
        histories = History.objects.all()
        return render(request, 'create_character.html', {'races': races, 'pclasses': pclasses, 'histories': histories})


def edit_player(request, p_id):
    player = Player.objects.get(pk=p_id)
    if request.method == "POST":        
        pname = request.POST['pname']        
        history_id = request.POST['phistory']
        img = request.POST['img']          
        history = History.objects.get(pk=history_id)
        player.name=pname
        player.history=history         
        if img:
            player.img = 'images/' + img         
        player.save()
        messages.success(request, ("Данные персонажа изменены."))  
        players = Player.objects.filter(user_id=request.user.id).order_by('-level')      
        return render(request, 'profile.html', {'players': players})    
    else:        
        histories = History.objects.all()
        return render(request, 'edit_character.html', {'player': player, 'histories': histories})
    

def distribute_points(request, p_id):
    player = Player.objects.get(pk=p_id)
    p_skills = PlayerSkill.objects.filter(player_id=player.id)
    if request.method == "POST":
        charact_id = request.POST['charact'] 
        player_skill = PlayerSkill.objects.get(pk=charact_id)
        player_skill.svalue = player_skill.svalue + 1        
        player.free_points = player.free_points - 1    
        player_skill.save()
        player.save()
        messages.success(request, ("Характеристика изменена"))  
        players = Player.objects.filter(user_id=request.user.id).order_by('-level')      
        return render(request, 'profile.html', {'players': players})    
    else:                
        return render(request, 'distribute_points.html', {'player': player, 'p_skills': p_skills})
