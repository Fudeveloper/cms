from django.shortcuts import render

# Create your views here.
# 主要界面
def main(request):
    return render(request, 'log/main.html')




def loginLog(request):
    return render(request, 'log/loginLog.html')

def operateLog(request):
    return render(request, 'log/operateLog.html')

def warnLog(request):
    return render(request, 'log/warnLog.html')

def warn_drawing(request):
    return render(request, 'log/warn_drawing.html')