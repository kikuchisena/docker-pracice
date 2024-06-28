from django.shortcuts import render,redirect
from django.views import View
from .models import Task
from .forms import TaskForm
# Create your views here.
class IndexView(View):
    def get(self,request):
        #todoリストを取得
        todo_list =Task.objects.all()
        
        context ={
            "todo_list":todo_list }
        
    
        return render(request,"mytodo/index.html", context)
    
class AddView(View):
    def get(seif, request):
        form =TaskForm()  
        return render(request,'mytodo/add.html',{'form':form})

    def post(self, request, *args, **kargs):
        form = TaskForm(request.POST)
        #入力データに誤りがないかチェック
        is_valid = form.is_valid()
        
        
        #データが正常であれば
        if is_valid:
            #モデルに登録
            form.save()
            return redirect('/')
        
        #データが正常じゃない
        return render(request,'mytodo/add.html',{'form':form})

class Update_task_complete(View):
    def post(self,request,*args, **kwargs):
        task_id =request.POST.get('task_id')
    
        task =Task.objects.get(id=task_id)
        task.complete =not task.complete
        task.save()
        
        return redirect('/')



    
index =IndexView.as_view()   
add =AddView.as_view() 
Update_task_complete =Update_task_complete.as_view()
