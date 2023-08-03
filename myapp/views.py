from django.shortcuts import render, redirect
from .forms import CovidForm
from .models import *
from joblib import load 
import pandas as pd
model = pd.read_pickle('treeModel/covid.pickle')
# from .prediction import make_prediction

# def your_view(request):
#     if request.method == 'POST':
#         form = CovidForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             instance = form.save()

#             # Make a prediction using the saved data
#             prediction = make_prediction(instance)  # Replace 'make_prediction' with your prediction function

#             # Store the prediction in the session
#             request.session['prediction'] = prediction

#             return redirect('result')  # Redirect to a result page to display the prediction
#     else:
#         form = CovidForm()

#     return render(request, 'predict.html', {'form': form})



# def make_prediction(instance):
#     # Extract the necessary data from the instance
#     diabetes = instance.diabetes  # Replace 'field1' with the actual field name from your model
#     asthma = instance.asthma  # Replace 'field2' with the actual field name from your model
#     icu = instance.icu  # Replace 'field_name' with the actual field name from your model

#     # Perform your prediction logic using the extracted data
#     # ...
#     # Return the prediction result
#     prediction = "Positive"

#     return prediction


# def predict_view(request):
#     if request.method == 'POST':
#         form = CovidForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             prediction = make_prediction(instance)
#             print(model)
#             request.session['prediction'] = prediction
#             return redirect('result')
#     else:
#         form = CovidForm()
#     return render(request, 'predict.html', {'form': form})


# def result_view(request):
#     prediction = request.session.get('prediction', None)
#     if prediction:
#         del request.session['prediction']  # Remove the prediction from the session
#         return render(request, 'prediction_result.html', {'prediction': prediction})
#     else:
#         return redirect('predict')
    
def home(request):
    return render(request, 'home.html')


def predict(request):
    model = pd.read_pickle('treeModel/covid.pickle')
    
    cough = request.GET.get('cough')
    fever = request.GET.get('fever')
    sore_throat  = request.GET.get('sore_throat')
    shortness_of_breath = request.GET.get('shortness_of_breath')
    head_ache = request.GET.get('head_ache')

    lis = []

    lis.append(cough)
    lis.append(fever)
    lis.append(sore_throat)
    lis.append(shortness_of_breath)
    lis.append(head_ache)

    print(lis)

    classification = model.predict([lis])

    CovidPredict.objects.create(
        cough=cough,
        fever=fever,
        sore_throat=sore_throat,
        shortness_of_breath=shortness_of_breath,
        head_ache=head_ache,
        classification=classification[0]
    )
    return render(request, 'prediction_result.html',{'classification_result': classification[0]})


def result_view(request):
    covid_prediction = CovidPredict.objects.all()
    
    context={
            'covid_records': covid_prediction
        }
    
    return render(request, 'prediction_result.html', context)
    