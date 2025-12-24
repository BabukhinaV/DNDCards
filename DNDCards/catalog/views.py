from django.shortcuts import render
from django.http import HttpResponse
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from catalog.models import History, InventoryCategory, InventoryItem, PClass, PClassSkill, Player, PlayerSkill, PlayerSpell, Race, Skill, Spell

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


def make_copy_txt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=data.txt'
    lines = []
    lines.append("-- Race\n")
    races = Race.objects.all()
    for race in races:
        lines.append("insert into catalog_race values (" + str(race.id) + ", " + race.title + ", " + race.descr + ", " + race.img.url + ")\n")
    lines.append("\n")
    lines.append("-- History\n")
    histories = History.objects.all()
    for his in histories:
        lines.append("insert into catalog_history values (" + str(his.id) + ", " + his.title + ", " + his.descr + ")\n")
    lines.append("\n")
    lines.append("-- PClass\n")
    pclasses = PClass.objects.all()
    for pcl in pclasses:
        lines.append("insert into catalog_pclass values (" + str(pcl.id) + ", " + pcl.title + ", " + pcl.descr + ", " + pcl.img.url + ")\n")    
    lines.append("\n")
    lines.append("-- InventoryCategory\n")
    invcats = InventoryCategory.objects.all()
    for invcat in invcats:
        lines.append("insert into catalog_inventorycategory values (" + str(invcat.id) + ", " + invcat.title + ", " + invcat.descr + ")\n")
    lines.append("\n")
    lines.append("-- InventoryItem\n")
    invitems = InventoryItem.objects.all()
    for invitem in invitems:
        lines.append("insert into catalog_inventoryitem values (" + str(invitem.id) + ", "  + str(invitem.category.id) + ", " + invitem.title + ", " + invitem.descr + ")\n")
    lines.append("\n")
    lines.append("-- Player\n")
    players = Player.objects.all()
    for player in players:
        if player.name != None:
            lines.append("insert into catalog_player values (" + str(player.id) + ", " + player.name + ", "  + str(player.level) + ", " + str(player.pclass.id) + ", " 
                     + str(player.race.id) + ", " + str(player.exp) + ", " + str(player.history.id) + ", " + str(player.user.id) + ", " +
                     player.img.url + ", " + str(player.free_points) + ")\n")    
    lines.append("\n")
    lines.append("-- Spell\n")
    spells = Spell.objects.all()
    for spell in spells:
        lines.append("insert into catalog_spell values (" + str(spell.id) + ", " + spell.title + ", "  + spell.descr + ", " + str(spell.level) + ", " 
                     + spell.cast_time + ", " + spell.distance  + ")\n")        
    lines.append("\n")
    lines.append("-- Spell\n")
    spells = Spell.objects.all()
    for spell in spells:
        lines.append("insert into catalog_spell values (" + str(spell.id) + ", " + spell.title + ", "  + spell.descr + ", " + str(spell.level) + ", " 
                     + spell.cast_time + ", " + spell.distance  + ")\n")   
    lines.append("\n")
    lines.append("-- PlayerSpell\n")
    pspells = PlayerSpell.objects.all()
    for pspell in pspells:
        lines.append("insert into catalog_playerspell values (" + str(pspell.id) + ", " + str(pspell.player.id) + ", "  + str(pspell.spell.id) + ", " + str(pspell.bonus) +  ")\n")
    lines.append("\n")
    lines.append("-- Skill\n")
    skills = Skill.objects.all()
    for skill in skills:
        lines.append("insert into catalog_skill values (" + str(skill.id) + ", " + skill.title + ", "  + skill.descr +  ")\n")    
    lines.append("\n")
    lines.append("-- PClassSkill\n")    
    pskills = PClassSkill.objects.all()
    for pskill in pskills:
        lines.append("insert into catalog_pclassskill values (" + str(pskill.id) + ", " + str(pskill.skill.id) + ", "  + str(pskill.svalue) + ", " + str(pskill.pclass.id) +  ")\n")     
    lines.append("\n")
    lines.append("-- PlayerSkill\n")    
    plskills = PlayerSkill.objects.all()
    for plskill in plskills:
        lines.append("insert into catalog_playerskill values (" + str(plskill.id) + ", " + str(plskill.skill.id) + ", "  + str(plskill.svalue) + ", " + str(plskill.player.id) +  ")\n")                        
    lines.append("\n")
    lines.append("-- Player Inventory\n")   
    for player in players:
        if player.name != None:
            for itm in player.inventory.all():
                lines.append("insert into catalog_player_inventory values (" + str(player.id) + ", " + str(itm.id) + ")\n")      
    response.writelines(lines)
    return response    



def make_copy_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'

    writer = csv.writer(response)
    writer.writerow(['Расы'])
    writer.writerow(['Название расы', 'Описание', 'Изображение'])
    races = Race.objects.all()
    for race in races:
        writer.writerow([race.title, race.descr, race.img.url])

    writer.writerow([''])
    writer.writerow(['Предыстории'])
    writer.writerow(['Название', 'Описание'])
    histories = History.objects.all()
    for his in histories:
        writer.writerow([his.title, his.descr])
    
    writer.writerow([''])
    writer.writerow(['Классы'])
    writer.writerow(['Название', 'Описание', 'Изображение'])
    pclasses = PClass.objects.all()    
    for pcl in pclasses:
        writer.writerow([pcl.title, pcl.descr, pcl.img.url])   

    writer.writerow([''])
    writer.writerow(['Категории'])
    writer.writerow(['Название', 'Описание'])
    invcats = InventoryCategory.objects.all()  
    for invcat in invcats:
        writer.writerow([invcat.title, invcat.descr])       
    
    writer.writerow([''])
    writer.writerow(['Предметы'])
    writer.writerow(['Категория', 'Название', 'Описание'])
    invitems = InventoryItem.objects.all()
    for invitem in invitems:
        writer.writerow([invitem.category.title, invitem.title, invitem.descr])
        
    writer.writerow([''])
    writer.writerow(['Игроки'])
    writer.writerow(['Имя', 'Уровень', 'Класс', 'Раса', 'Опыт', 'Предыстория', 'Логин', 'Аватар', 'Свободные очки'])
    players = Player.objects.all()
    for player in players:
        if player.name != None:
            writer.writerow([player.name, player.level, player.pclass.title, player.race.title, str(player.exp), player.history.title, player.user.username, 
                             player.img.url,str(player.free_points)])   
    
    writer.writerow([''])
    writer.writerow(['Заклинания'])
    writer.writerow(['Название', 'Описание', 'Уровень', 'Время', 'Дистанция'])
    spells = Spell.objects.all()
    for spell in spells:
        writer.writerow([spell.title, spell.descr, str(spell.level), spell.cast_time, spell.distance])    
    
    writer.writerow([''])
    writer.writerow(['Заклинания игроков'])
    writer.writerow(['ID', 'Игрок', 'Заклинание', 'Бонус'])
    pspells = PlayerSpell.objects.all()
    for pspell in pspells:
        writer.writerow([str(pspell.player.id), pspell.player.name, pspell.spell.title, str(pspell.bonus)])    
          
    writer.writerow([''])
    writer.writerow(['Навыки'])
    writer.writerow(['Название', 'Описание'])
    skills = Skill.objects.all()
    for skill in skills:
        writer.writerow([skill.title, skill.descr])   
    
    writer.writerow([''])
    writer.writerow(['Базовые навыки классов'])
    writer.writerow(['Навык', 'Класс', 'Значение'])
    pskills = PClassSkill.objects.all()
    for pskill in pskills:
        writer.writerow([pskill.skill.title, pskill.pclass.title, str(pskill.svalue)])     
    
    writer.writerow([''])
    writer.writerow(['Навыки игроков'])
    writer.writerow(['Навык', 'Игрок', 'Значение'])    
    plskills = PlayerSkill.objects.all()
    for plskill in plskills:
        writer.writerow([plskill.skill.title, plskill.player.name, str(plskill.svalue)])       
    
    writer.writerow([''])
    writer.writerow(['Инвентарь игроков'])
    writer.writerow(['ID игрока', 'Имя игрока', 'Предмет'])
    for player in players:
        if player.name != None:
            for itm in player.inventory.all():
                writer.writerow([str(player.id), player.name, itm.title])          
    
    return response      



def make_copy_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    lines = []    

    lines.append('Имя\t Уровень\t Класс\t Раса\t Опыт\t Предыстория\t Логин\t Свободные очки\n')    
    players = Player.objects.all()
    for player in players:
        if player.name != None:
            lines.append(player.name + '\t' + str(player.level) + '\t' + player.pclass.title + '\t' + str(player.exp) + '\t' + player.history.title + '\t' 
                         + player.user.username+ '\t' + str(player.free_points))     
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='data.pdf')