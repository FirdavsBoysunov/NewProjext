from django.db.models import Manager

class CustomerManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type = 'customer')
    

class AdminManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type = 'admin')
    
    
class IndividualManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type = 'individual')
    

class MarketManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type = 'market')