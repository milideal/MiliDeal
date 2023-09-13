from djongo import models


class TestModel(models.Model):
    _id = models.ObjectIdField()
    tkey = models.TextField(null=True, default='')

    class Meta:
        db_table = "test"
