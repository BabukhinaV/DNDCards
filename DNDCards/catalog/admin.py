from django.contrib import admin

from catalog.models import History, InventoryCategory, InventoryCategoryCharacteristic, InventoryItem, PClass, Player, Race, Skill, Spell

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


@admin.register(InventoryCategoryCharacteristic)
class InventoryCategoryCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('title', )
    ordering = ('title',)
    search_fields = ('title', )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'pclass', 'race', 'exp', 'history', 'user', 'img')
    ordering = ('name', 'level')
    search_fields = ('title', 'pclass', 'race') 