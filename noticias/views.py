from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
import json
import os
import re
import subprocess
from django.core.paginator import Paginator
from django.http import Http404

#path_folder = (os.getcwd())+ '/noticias/data/'
path_folder = os.getcwd() + '/noticias/data/'
name = 'items_history'
workname = name + '.json'
list_item = ['date','title','description','link','history','image','author','link_author','dominio','category','language','news_body','views']

def insert_json(request):
    print("path_folder",path_folder)
    # insertar a DB
    with open(os.path.join(path_folder, workname)) as file:
        data_json = json.load(file)
    
    # separar cada dato en cada columna de la DB e insertar
    for lista in data_json:
        print("lista",len(lista.items()))
        for key,value in lista.items():
            if key == list_item[0]:
                date_news = value
                
            elif key == list_item[1]:
                titulo = value
                
            elif key == list_item[2]:
                descripcion = value
                
            elif key == list_item[3]:
                link = value
                
            elif key == list_item[4]:
                historial = value
            
            elif key == list_item[5]:
                image = value
            
            elif key == list_item[6]:
                author = value
            
            elif key == list_item[7]:
                link_author = value
            
            elif key == list_item[8]:
                dominio = value
            
            elif key == list_item[9]:
                category = value
            
            elif key == list_item[10]:
                language = value
            
            elif key == list_item[11]:
                news_body = value
            
            elif key == list_item[12]:
                view = value

        param = (historial,titulo,descripcion,link,date_news,language,category,image,author,link_author,dominio,news_body,view)
        print("param",param)
        # Verificar noticia
        data = News.objects.filter(link=str(link))
        if data:
            print("existe", data[0].id)
        else:
            News.objects.create(date=date_news,title=titulo,category=category,autor=author,image=image,description=descripcion,views=view,language=language,history=historial,dominio=dominio,link=link,link_autor=link_author,body_news=news_body)
    
    print("Insertado el JSon")
    return HttpResponseRedirect('/')

# Create your views here.
def main(request):
    #insert_json()
    data = News.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(data,10)
        data = paginator.page(page)
    
    except:
        raise Http404

    print(page,"data",len(data))
    last_three = data[0:3]
    return render(request, 'Plantilla/garden-index.html', { 'data': data, 'post': last_three, 'paginator': paginator, 'entity': data})

def view_new(request,noticia):
    data = News.objects.get(id=int(noticia))
    data.views += 1
    data.save()
    list_body = eval(data.body_news)
    for i,d in enumerate(list_body):
        list_body[i] = re.sub('(<([^>]+)>)', '', d)
        print("list_body[i]",list_body[i])
    data.body_news = list_body
    data_all = News.objects.all()
    last_three = data_all[0:3]
    print("request.method",request.method)
    print("data",data)
    print("noticia a ver:",noticia)
    return render(request, 'Plantilla/new-single.html', { 'data': data, 'post': last_three })

def upload(request):
    print("actualice")
    #subprocess.call(["python3","schedule.py"],cwd=(os.getcwd())+ "/noticias/Arañas/")
    return HttpResponseRedirect('/')

def filter(request,filtro):
    print("Filtrar por:",filtro,filtro[0:3],filtro[-5:])
    data_all = News.objects.all()
    page = request.GET.get('page',1)
    last_three = data_all[0:3]

    if filtro[0:3] == 'Len':
        # Filtro por Language
        print("Idioma")
        data = News.objects.filter(language=str(filtro[-5:])) 

    else:
        # Filtro por Category
        print("CAtegory")
        data = News.objects.filter(category=str(filtro))

    try:
        paginator = Paginator(data,10)
        data = paginator.page(page)
    
    except:
        raise Http404

    print("data",data)
    return render(request, 'Plantilla/garden-index.html', { 'data': data, 'post': last_three,'paginator': paginator, 'entity': data })
    #return HttpResponseRedirect('/')