from django.contrib import admin

from catalog.models import History, InventoryCategory, InventoryItem, PClass, PClassSkill, Player, PlayerSkill, PlayerSpell, Race, Skill, Spell

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr', 'img')
    ordering = ('title',)
    search_fields = ('title', 'descr')


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr')
    ordering = ('title',)
    search_fields = ('title', 'descr')


@admin.register(PClass)
class PClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr')
    ordering = ('title',)
    search_fields = ('title', 'descr')


@admin.register(InventoryCategory)
class InventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr')
    ordering = ('title',)
    search_fields = ('title', 'descr')


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr', 'category')
    ordering = ('title',)
    search_fields = ('title', 'descr')


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr', 'level', 'cast_time', 'distance')
    ordering = ('title',)
    search_fields = ('title', 'descr')   


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'descr')
    ordering = ('title',)
    search_fields = ('title', )


#@admin.register(InventoryCategoryCharacteristic)
#class InventoryCategoryCharacteristicAdmin(admin.ModelAdmin):
    #list_display = ('title', )
    #ordering = ('title',)
    #search_fields = ('title', )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'pclass', 'race', 'exp', 'history', 'user', 'img', 'free_points')
    ordering = ('name', 'level')
    search_fields = ('title', 'pclass', 'race') 


@admin.register(PClassSkill)
class PClassSkillAdmin(admin.ModelAdmin):
    list_display = ('pclass', 'skill', 'svalue')
    ordering = ('pclass', )
    search_fields = ('pclass', 'skill') 


@admin.register(PlayerSkill)
class PlayerSkillAdmin(admin.ModelAdmin):
    list_display = ('player', 'skill', 'svalue')
    ordering = ('player', )
    search_fields = ('player', 'skill') 


@admin.register(PlayerSpell)
class PlayerSpellAdmin(admin.ModelAdmin):
    list_display = ('player', 'spell', 'bonus')
    ordering = ('player', )
    search_fields = ('player', 'spell')   