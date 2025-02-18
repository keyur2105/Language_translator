from django.shortcuts import render
from googletrans import Translator

def translator(request):
    
    if request.method=="GET":

        text = request.GET.get("text","").strip()
        language = request.GET.get("language")

        if not text or not language:
            return render(request,"index.html", {"error":"All Feild Required.."})
        
        translate = Translator()
        translate_text = translate.translate(text,dest=language).text
        return render(request, "index.html", {'translate_text':translate_text})
    
    return render(request, "index.html")