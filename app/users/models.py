import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Coalesce, Concat, NullIf, Trim


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.GeneratedField(
        db_persist=True,
        expression=Coalesce(  # Use 'first_name' + 'last_name' if both are not empty, else use 'username'
            NullIf(Trim(Concat('first_name', models.Value(' '), 'last_name')), models.Value('')),
            'username',
        ),
        output_field=models.CharField(max_length=300),
        verbose_name=('Display Name'),
    )
