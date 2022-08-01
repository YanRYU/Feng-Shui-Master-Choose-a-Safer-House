from django.db import connection

cursor = connection.cursor()
cursor.execute('''SELECT count(*) FROM taipei_grid_ascii_final''')

row = cursor.fetchone()

# def my_custom_sql(self):
    # with connection.cursor() as cursor:
        # cursor.execute("SELECT * FROM taipei_grid_ascii_final")
        # row = cursor.fetchone()

    # return row
	
# my_custom_sql