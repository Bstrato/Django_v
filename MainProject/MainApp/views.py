from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from .forms import CaputureInputForm
import  pickle
import  numpy as np
from django.contrib.staticfiles.storage import staticfiles_storage

from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.method == 'POST':
        return HttpResponseRedirect("/dashboard")
    return render(request, 'MainApp/index.html')


def dashboard(request):
    return render(request, 'MainApp/dashboard.html')


def input_form(request):
    forms = {}
    predict_message = " "

    possible_classes = {0:"Not likely to receive RTSS_2", 1: "Likely to receive RTSS_2" }
    search_select = {"bcg": "", "pent1": "", "pent2": "", "pent3":"", "rota1":"", "rota2":"","polio1":"","polio2":"","pnuemo1":"","pnuemo1":"","pneumo2":"","rtss1":""}

    if request.method == 'POST':
        if request.POST.get("submit_form"):
            form = CaputureInputForm(request.POST)



            if form.is_valid():

                # load the model from disk
                model_path  = staticfiles_storage.path("model/production_model.sav")
                loaded_ai_model = pickle.load(open(model_path, 'rb'))

                bcg =    form.cleaned_data["bcg"]
                pent1 =  form.cleaned_data["pent1"]
                pent2 =  form.cleaned_data["pent2"]
                pent3 =  form.cleaned_data["pent3"]
                rota1 =  form.cleaned_data["rota1"]
                rota2 =  form.cleaned_data["rota2"]
                polio1 = form.cleaned_data["polio1"]
                polio2 = form.cleaned_data["polio2"]
                pnuemo1 = form.cleaned_data["pnuemo1"]
                pneumo2 =  form.cleaned_data["pneumo2"]
                rtss1 =   form.cleaned_data["rtss1"]

                search_select["bcg"] = bcg
                search_select["pent1"] = pent1
                search_select["pent2"] = pent2
                search_select["pent3"] = pent3
                search_select["rota1"] = rota1
                search_select["rota2"] = rota2
                search_select["polio1"] = polio1
                search_select["polio2"] = polio2
                search_select["pnuemo1"] = pnuemo1
                search_select["pneumo2"] = pneumo2
                search_select["rtss1"] = rtss1


                captured_input = [[int(bcg), int(pent1), int(pent2), int(pent3), int(rota1), int(rota2), int(polio1), int(polio2) ,int(pnuemo1), int(pneumo2), int(rtss1)]]
                process_input = np.asarray(captured_input)
                ai_predict = loaded_ai_model.predict(process_input)[0]
                ai_confidence = loaded_ai_model.predict_proba(process_input)


                rtss_2_class = possible_classes[ai_predict]
                rtss_2_confidence = ai_confidence[0][ai_predict]

                predict_message = "AI Prediction : "+ rtss_2_class +" with confidence of " + str(round(rtss_2_confidence*100,2))+"%"

            else:
                forms = form


    return render(request, 'MainApp/input_form.html',{"forms": forms,"pred_message":predict_message,"form_search":search_select})
