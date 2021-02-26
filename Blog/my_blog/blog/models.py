
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

# Le mot clef spécial class permet d'indiquer que nous sommes en train de définir un objet.
''' 
 -- Post est le nom de notre modèle. Vous pouvez lui donner un autre nom (mais vous ne pouvez pas utiliser des
 caractères spéciaux ou accentués et insérer des espaces). Le nom d'une classe commence toujours par une majuscule.

 --models.Model signifie que Post est un modèle Django. Comme ça,
  Django sait qu'il doit l'enregistrer dans la base de données.
'''
class Post(models.Model):
    
    '''
    Maintenant, nous allons pouvoir définir les propriétés dont nous parlions au début de ce chapitre :
     title (titre), text (texte), created_date (date de création), published_date (date de publication) et author (auteur). Pour cela, nous allons avoir besoin de définir le type de chaque champ (Est-ce que 
    c'est du texte? Un nombre ? Une date ? Une relation à un autre objet, comme un objet utilisateur par exemple ?)
     '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #models.ForeignKey - C'est un lien vers un autre modèle.
    title = models.CharField(max_length=200)  #models.CharField champ texte avec un nombre limité de caractères.
    text = models.TextField() #models.TextField - Cela nous permet de définir un champ text sans limite de caractères
    created_date = models.DateTimeField(default=timezone.now) #Définit que le champ en question est une date ou une heure.
    published_date = models.DateTimeField(blank=True, null=True)
    '''
    def publish(self): ? Il s'agit de notre méthode publish dont nous parlions tout à l'heure. 
    def signifie que nous créons une fonction/méthode qui porte le nom publish. Vous pouvez changer
    le nom de la méthode si vous le souhaitez.
    La règle de nommage est d'utiliser des minuscules et des tirets bas à la place des espaces. Par exemple :calcul_prix_moyen 
    '''
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    '''
    lorsque nous appellerons la méthode __str__(), nous allons obtenir du texte (string) avec un titre de Post.
    '''
    def __str__(self):
        return self.title
