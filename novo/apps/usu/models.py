from django.db import models
from django.contrib.auth.models import User

User.add_to_class('act', models.CharField(max_length=30,null=True))