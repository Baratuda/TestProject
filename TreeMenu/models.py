from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', primary_key = True)
    slug = models.SlugField(max_length=150, verbose_name='URL')
    content = models.TextField(verbose_name='Содержание')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null = True) 
    main_menu = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null = True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Список меню'
        unique_together = (('title', 'parent'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #Данная конструкция позволяет определить главные меню и 
        # передает их менеджеру путей помечая как 'main'.
        if self.parent_id: 
            parent = self.parent_id
        else: 
            parent = 'main' 
        return reverse('view_menu_description', args=[parent, self.slug,])
        

@receiver(pre_save, sender=Menu)
def create_slug(sender, instance, *args, **kwargs):
    """
    Сигнал который заполняет поле main_menu перед созданием записи в БД. 
    """
    if instance.parent_id:
        parent = Menu.objects.get(pk=instance.parent_id)
        if parent.main_menu_id:
            instance.main_menu_id = parent.main_menu_id
        else:
            instance.main_menu_id = parent.title
            



      