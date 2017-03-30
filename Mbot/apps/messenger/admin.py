from django.contrib import admin
# from .models import SocialAccount, Session, Feedback

from apps.messenger.models import MessengerSession, MessengerInfo

@admin.register(MessengerSession)
class MessengerSession(admin.ModelAdmin):
	list_display = ['id', 'user', 'token','psid', 'page_id', 'expiration']

	class Meta:
		models = MessengerSession

@admin.register(MessengerInfo)
class MessengerInfo(admin.ModelAdmin):
	list_display = ['user', 'messenger_id','first_name', 'last_name', 'profile_pic', 'locale', 'timezone', 'gender']

	class Meta:
		models = MessengerInfo

