# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
  # * Rearrange models' order
  # * Make sure each model has one field with primary_key=True
  # * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
  # * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class TaipeiGrid(models.Model):
    # u_id = models.AutoField(db_column='U_ID', primary_key=True)  # Field name made lowercase.
    # codebase = models.CharField(db_column='CODEBASE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # code1 = models.CharField(db_column='CODE1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # code2 = models.CharField(db_column='CODE2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # town_id = models.IntegerField(db_column='TOWN_ID', blank=True, null=True)  # Field name made lowercase.
    # town = models.CharField(db_column='TOWN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # country_id = models.CharField(db_column='COUNTRY_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # country = models.CharField(db_column='COUNTRY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # x = models.CharField(db_column='X', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # y = models.CharField(db_column='Y', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # area = models.CharField(db_column='AREA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # geomertry = models.CharField(max_length=45, blank=True, null=True)

    # class Meta:
        # managed = False
        # db_table = 'Taipei_grid'


# class TaipeiGrid2(models.Model):
    # u_id = models.AutoField(db_column='U_ID', primary_key=True)  # Field name made lowercase.
    # codebase = models.CharField(db_column='CODEBASE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    # code1 = models.CharField(db_column='CODE1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # code2 = models.CharField(db_column='CODE2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # town_id = models.CharField(db_column='TOWN_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # town = models.CharField(db_column='TOWN', max_length=60, blank=True, null=True)  # Field name made lowercase.
    # country_id = models.FloatField(db_column='COUNTRY_ID', blank=True, null=True)  # Field name made lowercase.
    # country = models.CharField(db_column='COUNTRY', max_length=60, blank=True, null=True)  # Field name made lowercase.
    # x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    # y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    # area = models.FloatField(db_column='AREA', blank=True, null=True)  # Field name made lowercase.
    # geomertry = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'Taipei_grid2'


# class Taipei(models.Model):
    # u_id = models.AutoField(db_column='U_ID', primary_key=True)  # Field name made lowercase.
    # codebase = models.CharField(db_column='CODEBASE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    # code1 = models.CharField(db_column='CODE1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # code2 = models.CharField(db_column='CODE2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # town_id = models.CharField(db_column='TOWN_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # town = models.CharField(db_column='TOWN', max_length=60, blank=True, null=True)  # Field name made lowercase.
    # country_id = models.FloatField(db_column='COUNTRY_ID', blank=True, null=True)  # Field name made lowercase.
    # country = models.CharField(db_column='COUNTRY', max_length=60, blank=True, null=True)  # Field name made lowercase.
    # x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    # y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    # area = models.FloatField(db_column='AREA', blank=True, null=True)  # Field name made lowercase.
    # geomertry = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'taipei'


# class TaipeiGrid2(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # codebase = models.CharField(db_column='CODEBASE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # town_id = models.CharField(db_column='TOWN_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # geometry = models.CharField(max_length=45, blank=True, null=True)

    # class Meta:
        # managed = False
        # db_table = 'taipei_grid2'


# class TaipeiGridAscii(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # codebase = models.TextField(db_column='CODEBASE', blank=True, null=True)  # Field name made lowercase.
    # town_id = models.IntegerField(db_column='TOWN_ID', blank=True, null=True)  # Field name made lowercase.
    # geometry = models.TextField(blank=True, null=True)

    # class Meta:
        # managed = False
        # db_table = 'taipei_grid_ascii'


# class TaipeiGridAsciiFinal(models.Model):
    # id = models.IntegerField()
    # codebase = models.TextField(blank=True, null=True)
    # town_id = models.IntegerField(blank=True, null=True)
    # geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'taipei_grid_ascii_final'


# class TaipeiGridAsciiNewnew2(models.Model):
    # myunknowncolumn = models.IntegerField(db_column='MyUnknownColumn', blank=True, null=True)  # Field name made lowercase.
    # codebase = models.TextField(db_column='CODEBASE', blank=True, null=True)  # Field name made lowercase.
    # town_id = models.TextField(db_column='TOWN_ID', blank=True, null=True)  # Field name made lowercase.
    # geometry = models.TextField(blank=True, null=True)

    # class Meta:
        # managed = False
        # db_table = 'taipei_grid_ascii_newnew_2'


# class Test(models.Model):
    # geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'test'


# class Test1(models.Model):
    # test = models.TextField(blank=True, null=True)  # This field type is a guess.
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # basecode = models.CharField(db_column='BASECODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    # code1 = models.CharField(db_column='CODE1', max_length=45, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'test1'


# class Test2(models.Model):
    # test = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'test2'


# class Test3(models.Model):
    # test = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'test3'


# class Test4(models.Model):
    # test = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'test4'


# class Test5(models.Model):
    # test = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'test5'


# class Test6(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    # test = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'test6'


# class Test7(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    # geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'test7'


# class User1(models.Model):
    # test = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
        # managed = False
        # db_table = 'user1'
