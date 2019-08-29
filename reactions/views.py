from reactions.models import reactions
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse



def index(request):
       request.session.set_expiry(0)
       r = reactions.objects.first()
       if request.method == "POST":
           if  not request.session.get('has_reacted', False):
               if request.POST['data'] == "upvote":
                     r.upvote = r.upvote + 1
                     count = r.upvote
               elif request.POST['data'] == "funny":
                     r.funny = r.funny + 1
                     count = r.funny
               else:
                    if request.POST['data'] == "love":
                       r.love = r.love + 1
                       count = r.love
               r.save()
               request.session["has_reacted"] = True
               total_responses = reactions.objects.first().upvote +  reactions.objects.first().funny + reactions.objects.first().love
               data = {}
               data["count"] = count
               data["total_responses"] = total_responses
               return JsonResponse(data)
           else:
               return HttpResponse("already_commented")
       else:
            total_responses = r.upvote + r.funny + r.love
            context = {
                       'total_responses':total_responses ,
                       'upvotes':r.upvote,
                       'funny':r.funny,
                       'love':r.love,
                      }
            return render(request,'reactions/index.html',context)

def delete(request):
    r = reactions.objects.first()
    r.delete()
    return HttpResponse("deleted")

def put(request):
    r = reactions(upvote = 0, funny = 0, love = 0, last_session_id ="")
    r.save()
    return HttpResponse("success")

