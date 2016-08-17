from django.db import models

# Create your models here.

class Join(models.Model):
	email = models.EmailField()
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now =False)
	updated = models.DateTimeField(auto_now_add = False, auto_now =True)

	def __unicode__(self):
		return "Hi %s" %(self.email) 
	 
#1) install south: pip install south, add south to settings.py in INSTALLED APPS
#2) ensure Model is in the synced in database
#3) convert the model to south with: python manage.py convert_to_south appname
#4) make changes to model (eg add new fields: ip_address = models.CharField(max_length=120, default='ABC'))
#5) run schemamigration: python manage.py schemamigration appname --auto
#6) run migrate : python manage.py migrate
