from django.db import models
from django.contrib.auth.models import User

class Race(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)
    img = models.ImageField(
        'Изображение', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Раса')
        verbose_name_plural = ('Расы')


class History(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Предыстория')
        verbose_name_plural = ('Предистории')


class PClass(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)
    img = models.ImageField(
        'Изображение', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Класс')
        verbose_name_plural = ('Классы')

class InventoryCategory(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Категория инвентаря')
        verbose_name_plural = ('Категории инвентаря')


class InventoryItem(models.Model):
    category = models.ForeignKey(
        InventoryCategory, verbose_name='Категория инвентаря', on_delete=models.DO_NOTHING)   
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Предмет инвентаря')
        verbose_name_plural = ('Предметы инвентаря')


class Player(models.Model):
    name = models.CharField('Имя', blank=True, null=True, max_length=255)
    level = models.IntegerField('Уровень')
    pclass = models.ForeignKey(
        PClass, verbose_name='Класс', null=True, blank=True, on_delete=models.DO_NOTHING)   
    race = models.ForeignKey(
        Race, verbose_name='Раса', null=True, blank=True, on_delete=models.DO_NOTHING)   
    exp = models.IntegerField('Опыт')
    history = models.ForeignKey(
        History, verbose_name='Предыстория', null=True, blank=True, on_delete=models.DO_NOTHING)  
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    img = models.ImageField(
        'Изображение', null=True, blank=True, upload_to="images/")
    free_points = models.IntegerField('Свободные очки', null=True, blank=True)
    inventory = models.ManyToManyField(InventoryItem, verbose_name='Предмет инвентаря')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Персонаж')
        verbose_name_plural = ('Персонажи')
   

class Spell(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)
    level = models.IntegerField('Уровень')
    cast_time = models.CharField('Время накладывания', max_length=255)
    distance = models.CharField('Дистанция', max_length=255)     

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Заклинание')
        verbose_name_plural = ('Заклинания')


class PlayerSpell(models.Model):
    player = models.ForeignKey(
        Player, verbose_name='Персонаж', on_delete=models.DO_NOTHING)  
    spell = models.ForeignKey(
        Spell, verbose_name='Заклинание', on_delete=models.DO_NOTHING)    
    bonus = models.IntegerField('Бонус')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = ('Заклинание персонажа')
        verbose_name_plural = ('Заклинания персонажа')


class Skill(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Навык')
        verbose_name_plural = ('Навыки')


class PClassSkill(models.Model): 
    skill = models.ForeignKey(
        Skill, verbose_name='Навык', on_delete=models.DO_NOTHING)  
    svalue = models.IntegerField('Значение')
    pclass = models.ForeignKey(
        PClass, verbose_name='Класс', on_delete=models.DO_NOTHING)  

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = ('Базовый навык класса')
        verbose_name_plural = ('Базовые навыки класса')


class PlayerSkill(models.Model):
    skill = models.ForeignKey(
        Skill, verbose_name='Навык', on_delete=models.DO_NOTHING)  
    svalue = models.IntegerField('Значение')
    player = models.ForeignKey(
        Player, verbose_name='Персонаж', on_delete=models.DO_NOTHING)  

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = ('Навык персонажа')
        verbose_name_plural = ('Навыки персонажа')