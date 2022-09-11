def handle_uploaded_file(f):  
    with open('content/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    ass ='content/static/upload/'+f.name
    print(ass)
    return ass 