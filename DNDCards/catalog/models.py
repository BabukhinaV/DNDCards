from django.db import models

class Race(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Раса')
        verbose_name_plural = ('Расы')


class PClass(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Класс')
        verbose_name_plural = ('Классы')


class Trait(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Черта')
        verbose_name_plural = ('Черты')


class SpellComponent(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Компонента заклинания')
        verbose_name_plural = ('Компоненты заклинания')


class Spell(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)
    level = models.IntegerField('Уровень')
    cast_time = models.CharField('Время накладывания')
    distance = models.CharField('Дистанция')
    components = models.ManyToManyField(SpellComponent, verbose_name='Компоненты')   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Заклинание')
        verbose_name_plural = ('Заклинания')


#class MagicItem(models.Model):
    #title = models.CharField('Название', max_length=255)
    #descr = models.TextField('Описание', max_length=10000)    
    #rarity = models.CharField('Редкость', max_length=255)    
    #rec_price_min = models.IntegerField('Рекомендованая стоимость, мин.')
    #rec_price_max = models.IntegerField('Рекомендованая стоимость, макс.')
    #def __str__(self):
        #return self.title

    #class Meta:
        #verbose_name = ('Магический предмет')
        #verbose_name_plural = ('Магические предметы')


#class MagicItemVariant(models.Model):
    #parent_item = models.ForeignKey(
        #MagicItem, verbose_name='Вариант магического предмета', on_delete=models.DO_NOTHING)
    #title = models.CharField('Название', max_length=255)
    #descr = models.TextField('Описание', max_length=10000)    
    #rarity = models.CharField('Редкость', max_length=255)    
    #rec_price_min = models.IntegerField('Рекомендованая стоимость, мин.')
    #rec_price_max = models.IntegerField('Рекомендованая стоимость, макс.')
    #def __str__(self):
        #return self.title

    #class Meta:
        #verbose_name = ('Вариант магического предмета')
        #verbose_name_plural = ('Варианты магического предмета')



class InventoryCategory(models.Model):
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Категория инвентаря')
        verbose_name_plural = ('Категории инвентаря')


class InventorySubCategory(models.Model):
    
    title = models.CharField('Название', max_length=255)
    descr = models.TextField('Описание', max_length=7000)
    category = models.ForeignKey(
        InventoryCategory, verbose_name='Категория инвентаря', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Подкатегория инвентаря')
        verbose_name_plural = ('Подкатегории инвентаря')


class InventoryCategoryCharacteristic(models.Model):
    title = models.CharField('Название', max_length=255)    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Характеристика предмета инвентаря')
        verbose_name_plural = ('Характеристики предмета инвентаря')


class InventoryItem(models.Model):
    category = models.ForeignKey(
        InventorySubCategory, verbose_name='Подкатегория инвентаря', on_delete=models.DO_NOTHING)   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Предмет инвентаря')
        verbose_name_plural = ('Предметы инвентаря')


class ItemCharact(models.Model):
    item = models.ForeignKey(
        InventoryItem, verbose_name='Предмет инвентаря', on_delete=models.DO_NOTHING)   
    charact = models.ForeignKey(
        InventoryCategoryCharacteristic, verbose_name='Характеристика предмета инвентаря', on_delete=models.DO_NOTHING)   
    ch_value = models.CharField('Значение', max_length=255)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = ('Значение характеристики')
        verbose_name_plural = ('Значения характеристики')
