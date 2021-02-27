from graphene import ObjectType, Field, Schema
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from importlib import import_module
from django.conf import settings


def getSessionStore():
    # Currently errors out with 
    #           module 'django.contrib.sessions.backends.db' has no attribute 'SesssionStore'
    currentSessionEngine = import_module(settings.SESSION_ENGINE)
    return currentSessionEngine.SesssionStore


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "first_name")

class Query(ObjectType):
    GetCurrentUser = Field(UserType)

    # TODO: Add a mutation for logging in the user
    # Probably calls the login() method
    # https://docs.djangoproject.com/en/3.1/topics/auth/default/#authenticating-users

    # TODO: Add a mutation for logging out the user

    def resolve_GetCurrentUser(root, info):
        session = getSessionStore()

        # TODO: Get the current User from the current Session
        # Check that the User.is_authenticated
        pass


schema = Schema(query=Query)