from pickle import FALSE
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request,"calculator/index.html")

def port(request):
    return render(request,"calculator/port.html")

def depart(request):
    return render(request, "calculator/it.html", {})

def sh3(request):
    return render(request, "calculator/sh3.html", {})

def it2yr(request):
    return render(request, "calculator/it2yr.html", {})

def it2yr3(request):
    return render(request, "calculator/it2yr3.html", {})

def it2yr4(request): 
    return render(request, "calculator/it2yr4.html", {})

def it2ndyr3R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2

    S1=res1/30
    S2=res2/30
    S3=res3/30

    
    res= res1+res2+res3
    total= res/90
    P=(total-0.5)*10

    return render(request, "calculator/result2yr3.html", {"result":total, "P":P, "S1":S1,"S2":S2,"S3":S3})

def it2ndyr4R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])


    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])


    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])

    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])
    
    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])

    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    
    
    res= res1+res2+res3+res4
    total= res/120
    P=(total-0.5)*10
    
    return render(request, "calculator/result2yr4.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4})


def it3yr(request):
    return render(request, "calculator/it3yr.html", {})
    
def it3yr5(request):
    return render(request, "calculator/it3yr5.html", {})

def it3yr6(request):
    return render(request, "calculator/it3yr6.html", {})

def it3rdyr5R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    sub30=int(request.GET["sub30"])

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP=int(request.GET["GP"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+sub30*4+lab13*2+lab14*2+lab15*2+GP
    res= res1+res2+res3+res4+res5

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    S5=res3/30

    total= res/151
    total= res/120
    P=(total-0.5)*10

    return render(request, "calculator/result3yr5.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5})

def it3rdyr6R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    sub30=int(request.GET["sub30"])

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])

    sub31=int(request.GET["sub31"])
    sub32=int(request.GET["sub32"])
    sub33=int(request.GET["sub33"])
    sub34=int(request.GET["sub34"])
    sub35=int(request.GET["sub35"])
    sub36=int(request.GET["sub36"])

    lab16=int(request.GET["lab16"])
    lab17=int(request.GET["lab17"])
    lab18=int(request.GET["lab18"])

    GP1=int(request.GET["GP1"])
    GP=int(request.GET["GP"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+sub30*4+lab13*2+lab14*2+lab15*2+GP
    res6 = sub31*4+sub32*4+sub33*4+sub34*4+sub35*4+sub36*4+lab16*2+lab17*2+lab18*2+GP1
    res= res1+res2+res3+res4+res5+res6
    
    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    S5=res3/30
    S6=res3/30

    total= res/151
    total= res/182
    P=(total-0.5)*10

    return render(request, "calculator/result3yr6.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5,"S6":S6})


def it4yr(request):
    return render(request, "calculator/it4yr.html", {})
    
def it4yr7(request):
    return render(request, "calculator/it4yr7.html", {})

def it4yr8(request):
    return render(request, "calculator/it4yr8.html", {})

    
def it4yr7R(request):
    return render(request, "calculator/it3yr7R.html", {})

def it4yr8R(request):
    return render(request, "calculator/it3yr8R.html", {})


def cse(request):
    return render(request, "calculator/cse.html", {})

def cse2yr(request):
    return render(request, "calculator/cse2yr.html", {})

def cse2yr3(request):
    return render(request, "calculator/cse2yr3.html", {})





def cse2yr4(request):
    return render(request, "calculator/cse2yr4.html", {})

def cse3yr(request):
    return render(request, "calculator/cse3yr.html", {})

def cse3yr5(request):
    return render(request, "calculator/cse3yr5.html", {})

def cse3yr5R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP=int(request.GET["GP"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+lab13*2+lab14*2+lab15*2+GP
    res= res1+res2+res3+res4+res5

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    S5=res3/30

    total= res/147
    P=(total-0.5)*10

    return render(request, "calculator/result3yr5.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5})

def cse3yr6(request):
    return render(request, "calculator/cse3yr6.html", {})

def cse3yr6R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP=int(request.GET["GP"])

    sub30=int(request.GET["sub30"])
    sub31=int(request.GET["sub31"])
    sub32=int(request.GET["sub32"])
    sub33=int(request.GET["sub33"])
    sub34=int(request.GET["sub34"])
    

    lab16=int(request.GET["lab16"])
    lab17=int(request.GET["lab17"])
    lab18=int(request.GET["lab18"])


    GP1=int(request.GET["GP1"])
    IV=int(request.GET["IV"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+lab13*2+lab14*2+lab15*2+GP
    res6 = sub30*4+sub31*4+sub32*4+sub33*4+sub34*4+lab16*2+lab17*2+lab18*2+GP1+IV
    res= res1+res2+res3+res4+res5+res6

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    S5=res3/30
    S6=res3/30

    total= res/147
    P=(total-0.5)*10

    return render(request, "calculator/result3yr6.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5,"S6":S6})

def cse4yr(request):
    return render(request, "calculator/cse4yr.html", {})

def cse4yr7(request):
    return render(request, "calculator/cse4yr7.html", {})


def cse4yr7R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP=int(request.GET["GP"])

    sub30=int(request.GET["sub30"])
    sub31=int(request.GET["sub31"])
    sub32=int(request.GET["sub32"])
    sub33=int(request.GET["sub33"])
    sub34=int(request.GET["sub34"])
    

    lab16=int(request.GET["lab16"])
    lab17=int(request.GET["lab17"])
    lab18=int(request.GET["lab18"])


    GP1=int(request.GET["GP1"])
    IV=int(request.GET["IV"])

    sub35=int(request.GET["sub30"])
    sub36=int(request.GET["sub31"])
    sub37=int(request.GET["sub32"])
    sub38=int(request.GET["sub33"])
    

    lab19=int(request.GET["lab19"])
    lab20=int(request.GET["lab20"])
    lab21=int(request.GET["lab21"])


    PW1=int(request.GET["PW1"])
    

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+lab13*2+lab14*2+lab15*2+GP
    res6 = sub30*4+sub31*4+sub32*4+sub33*4+sub34*4+lab16*2+lab17*2+lab18*2+GP1+IV
    res7 = sub35*4+sub36*4+sub37*4+sub38*4+lab19*2+lab20*2+lab21*2+PW1
    res= res1+res2+res3+res4+res5+res6+res7

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res4/30
    S5=res5/30
    S6=res6/30
    S7=res7/30

    total= res/203
    P=(total-0.5)*10

    return render(request, "calculator/result4yr7.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5,"S6":S6,"S7":S7})



def cse4yr8(request):
    return render(request, "calculator/cse4yr8.html", {})



def ece(request):
    return render(request, "calculator/ece.html", {})

def ece2yr(request):
    return render(request, "calculator/ece2yr.html", {})

def ece2yr3(request):
    return render(request, "calculator/ece2yr3.html", {})

def ece2yr3R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2

    S1=res1/30
    S2=res2/30
    S3=res3/30

    
    res= res1+res2+res3
    total= res/90
    P=(total-0.5)*10

    return render(request, "calculator/result2yr3.html", {"result":total, "P":P, "S1":S1,"S2":S2,"S3":S3})

def ece2yr4(request):
    return render(request, "calculator/ece2yr4.html", {})

def ece2yr4R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])


    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])


    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])

    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])
    
    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])

    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    
    
    res= res1+res2+res3+res4
    total= res/120
    P=(total-0.5)*10
    
    return render(request, "calculator/result2yr4.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4})

def ece3yr(request):
    return render(request, "calculator/ece3yr.html", {})

def ece3yr5(request):
    return render(request, "calculator/ece3yr5.html", {})

def ece3yr5R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    sub30=int(request.GET["sub30"])
    

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP1=int(request.GET["GP1"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+sub30*4+lab13*2+lab14*2+lab15*2+GP1
    res= res1+res2+res3+res4+res5

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    S5=res3/31

    total= res/151
    P=(total-0.5)*10

    return render(request, "calculator/result3yr5.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5})

def ece3yr6(request):
    return render(request, "calculator/ece3yr6.html", {})

def ece3yr6R(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP=int(request.GET["GP"])

    sub30=int(request.GET["sub30"])
    sub31=int(request.GET["sub31"])
    sub32=int(request.GET["sub32"])
    sub33=int(request.GET["sub33"])
    sub34=int(request.GET["sub34"])
    sub35=int(request.GET["sub35"])
    

    lab16=int(request.GET["lab16"])
    lab17=int(request.GET["lab17"])
    lab18=int(request.GET["lab18"])


    GP1=int(request.GET["GP1"])
    IV=int(request.GET["IV"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+lab13*2+lab14*2+lab15*2+GP
    res6 = sub30*4+sub31*4+sub32*4+sub33*4+sub34*4+lab16*2+lab17*2+lab18*2+GP1+IV+sub35*4
    res= res1+res2+res3+res4+res5+res6

    S1=res1/30
    S2=res2/30
    S3=res3/30
    S4=res3/30
    S5=res3/30
    S6=res3/30

    total= res/147
    P=(total-0.5)*10

    return render(request, "calculator/result3yr6.html", {"result":total,"P":P, "S1":S1,"S2":S2,"S3":S3,"S4":S4,"S5":S5,"S6":S6})


def eee(request):
    return render(request, "calculator/eee.html", {})

def eee2yr(request):
    return render(request, "calculator/eee2yr.html", {})

def eee2yr3(request):
    return render(request, "calculator/eee2yr3.html", {})

def eee2yr4(request):
    return render(request, "calculator/eee2yr4.html", {})

def eee3yr(request):
    return render(request, "calculator/eee3yr.html", {})

def eee3yr5(request):
    return render(request, "calculator/eee3yr5.html", {})

def eee3yr6(request):
    return render(request, "calculator/eee3yr6.html", {})




def mech(request):
    return render(request, "calculator/mech.html", {})
    
def mech2yr(request):
    return render(request, "calculator/mech2yr.html", {})

def mech2yr3(request):
    return render(request, "calculator/mech2yr3.html", {})

def mechR1(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2

    
    res= res1+res2+res3
    total= res/90

    return render(request, "calculator/result.html", {"result":total})

def mech2yr4(request):
    return render(request, "calculator/mech2yr4.html", {})

def mechR2(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])
    
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])
    
    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])


    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2


    
    res= res1+res2+res3+res4
    total= res/120

    return render(request, "calculator/result.html", {"result":total})

def mech3yr(request):
    return render(request, "calculator/mech3yr.html", {})

def mech3yr5(request):
    return render(request, "calculator/mech3yr5.html", {})

def mech3yr6(request):
    return render(request, "calculator/mech3yr6.html", {})







def cal(request):
    sub1=int(request.GET["sub1"])
    sub2=int(request.GET["sub2"])
    sub3=int(request.GET["sub3"])
    sub4=int(request.GET["sub4"])
    sub5=int(request.GET["sub5"])
    sub6=int(request.GET["sub6"])
    
    lab1=int(request.GET["lab1"])
    lab2=int(request.GET["lab2"])
    lab3=int(request.GET["lab3"])



    sub7=int(request.GET['sub7'])
    sub8=int(request.GET["sub8"])
    sub9=int(request.GET["sub9"])
    sub10=int(request.GET["sub10"])
    sub11=int(request.GET["sub11"])
    sub12=int(request.GET["sub12"])

    lab4=int(request.GET["lab4"])
    lab5=int(request.GET["lab5"])
    lab6=int(request.GET["lab6"])



    sub13=int(request.GET["sub13"])
    sub14=int(request.GET["sub14"])
    sub15=int(request.GET["sub15"])
    sub16=int(request.GET["sub16"])
    sub17=int(request.GET["sub17"])
    sub18=int(request.GET["sub18"])
    
    lab7=int(request.GET["lab7"])
    lab8=int(request.GET["lab8"])
    lab9=int(request.GET["lab9"])


   
    sub19=int(request.GET["sub19"])
    sub20=int(request.GET["sub20"])
    sub21=int(request.GET["sub21"])
    sub22=int(request.GET["sub22"])
    sub23=int(request.GET["sub23"])
    sub24=int(request.GET["sub24"])

    lab10=int(request.GET["lab10"])
    lab11=int(request.GET["lab11"])
    lab12=int(request.GET["lab12"])



    sub25=int(request.GET["sub25"])
    sub26=int(request.GET["sub26"])
    sub27=int(request.GET["sub27"])
    sub28=int(request.GET["sub28"])
    sub29=int(request.GET["sub29"])
    sub30=int(request.GET["sub30"])

    lab13=int(request.GET["lab13"])
    lab14=int(request.GET["lab14"])
    lab15=int(request.GET["lab15"])


    GP=int(request.GET["GP"])

    
    res1 = sub1*4+sub2*4+sub3*4+sub4*4+sub5*4+sub6*4+lab1*2+lab2*2+lab3*2
    res2 = sub7*4+sub8*4+sub9*4+sub10*4+sub11*4+sub12*4+lab4*2+lab5*2+lab6*2
    res3 = sub13*4+sub14*4+sub15*4+sub16*4+sub17*4+sub18*4+lab7*2+lab8*2+lab9*2
    res4 = sub19*4+sub20*4+sub21*4+sub22*4+sub23*4+sub24*4+lab10*2+lab11*2+lab12*2
    res5 = sub25*4+sub26*4+sub27*4+sub28*4+sub29*4+sub30*4+lab13*2+lab14*2+lab15*2+GP
    res= res1+res2+res3+res4+res5
    total= res/150
    percentage= (total - 0.5)*10
    return render(request,"calculator/result1.html", {"result":total})
    