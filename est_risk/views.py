from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import json

# from datetime import datetime
# def hello_world(request):
    # return render(request,"index.html",{
            # 'current_time': str(datetime.now())
        # })
		
def index(request):
# Render the HTML template index.html
	return render(request, 'index.html')
	
	
from django.db import connection

def query(request):
	with connection.cursor() as cursor:
		cursor.execute("CREATE table  userdata (uid int, point geometry)")
		cursor.execute("insert into userdata value(1,POINT({X},{Y}))".format(X = 310568.683521, Y = 2775512.7))
		cursor.execute(
			"""
			select s.*
			from `score` as s 
			INNER JOIN(
			SELECT CODEBASE FROM `userdata` p, `taipei_grid_ascii_final` a 
			where ST_Within(p.point,a.geom) = 1
			) as b
			on s.BASEID = b.CODEBASE
			"""
			)
		row = cursor.fetchall()
		cursor.execute("drop table userdata")

	return render(request, 
			'index.html',
			{'row': row}
			)

# def query(request):
	# from django.db import connection
	# with connection.cursor() as cursor:
		# query = """
		# SELECT *
		# FROM FID.taipei_grid_ascii_final
		# ;
		# """
		# cursor.execute(query)
		# row = cursor.fetchone()
	# print(row)
	# return render(request, 
			# 'index.html',
			# {'row': str(row)},
				# )


# def go(request):
	# if request.method == 'POST':
		# arr = request.POST.getlist('arr[]')



 
 
# def ajax_submit(request):
	# if request.method == 'POST':
		# if request.is_ajax():
			# print("**ajax post**")
			# data = request.POST['cor']
			# astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
			# return HttpResponse(astr)
		# return render(request)
    # print(list(request.POST.items()))
    # return  HttpResponse(request.POST.items())
	
	
# def ajax_jquery(request):
    # is_ajax = False
    # if request.is_ajax():
        # is_ajax = True
    # test = {'GET': 'GET',
            # 'array': [1, 2, 3, 4],
            # 'a': request.GET['a'],
            # "b": [1, 2, 3] in index.html,
            # 'b[]': request.GET.getlist('b[]'),
            # 'is_ajax': is_ajax,
            # }
    # return JsonResponse(test)
 
# def ajax_jquery(request):
	# if request.is_ajax():
		# POSTdata = request.POST
		# a = request.POST.get("a")
		# response = JsonResponse({"hello":"hello! AJAX!"})
		# print(POSTdata)
		# print(a)
		# return response

# def ajax_jquery(request):
	# if request.method == "POST":
		# if form.is_valid():
			# form.save
			# return JsonResponse({"message":"Successfully published"})
		# else:
			# response = JsonResponse({"error": "there was an error"})
			# response.status_code = 403 # To announce that the user isn't allowed to publish
			# return response
	# else:
		# return JsonResponse({"success": false, "error": "Request method is not post"})
		
		
# def ajax_dict(request):
    # name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    # return JsonResponse(name_dict)