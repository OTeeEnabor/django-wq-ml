import pickle
import os

import pandas as pd
import numpy as np
from django.conf import settings
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView,CreateView
import shortuuid as suuid
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomTreesEmbedding, RandomForestClassifier

from plotly.offline import plot
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go

from .forms import FormDetection
from .models import UserInput






# Create your views here.
def loadReturnDf(file_path):
    # read in static file csv
    data_root = f'{settings.BASE_DIR}/data/'
    static_csv_filepath = os.path.join(data_root,file_path)
    # load csv
    df = pd.read_csv(static_csv_filepath)
    # drop unwanted column
    df = df.drop(labels="Unnamed: 0", axis=1)
    #  calculate median groupby
    median_df = df.groupby("is_safe").median()
    median_df = median_df.T
    # filter by top 10 features
    top_10 =["aluminium","arsenic","barium","cadmium","chloramine","chromium","perchlorate","silver","uranium","viruses"]
    median_df = median_df[median_df.index.isin(top_10)]

    return df, median_df

def targetDistribution(df):
    is_safe_count = df["is_safe"].value_counts()
    is_safe_count.index = ["Not Safe","Safe"]
    fig = px.bar(is_safe_count, text_auto=True)
    fig.update_layout(
        title="Distribution of Target Variable",
        xaxis_title= "Water Quality Status",
        yaxis_title = "Count",
        showlegend=False
    )
    return fig


def groupByDf(median_df,pred=None, input_list=None):
    # create safe bar chart
    safe_bar = go.Bar(name="Safe",x =median_df.index, y= median_df[1])
    # create not safe bar chart
    not_safe_bar = go.Bar(name="Not Safe",x =median_df.index, y= median_df[0])
    # create input list
    top_input_features = go.Bar(name="input",x=median_df.index, y=input_list)
    if pred == 0:
        data = not_safe_bar
    else:
        data = safe_bar
    fig = go.Figure(data=[data,top_input_features])
    fig.update_layout(
        barmode="group", title="Median vs Input"
    )
    return fig


def getPredictions(features_list):
    # load the model
    model = pickle.load(open('rf_model.sav', 'rb'))
    prediction = model.predict(features_list)
    prediction = prediction[0]
    return prediction
 
class IndexView(View):

    def get(self, request):
        form = FormDetection()
        
        # print("this is a get request")
        id = suuid.uuid()
        context = {"form":form,
                   "id": id,
                   }
        return render(request, "wqpred/index.html", context)
    
    def post(self, request):
        form  = FormDetection(request.POST)

        if form.is_valid():
            id = form.cleaned_data["id"]
            form.save()
            return HttpResponsePermanentRedirect(f"result/{id}")

        else:
            print(form.errors)

        context = {
            "form":form,
        }
        return render(request,"wqpred/index.html", context)

class ResultView(DetailView):
    # define the template to render
    template_name = "wqpred/result.html"
    # load the model which holds data needed to make predictions
    model = UserInput
    
    def get_context_data(self, **kwargs):
        # get required context
        context = super().get_context_data(**kwargs)
        # get the loaded input values
        user_input = self.get_object()
        # define feature list
        feature_list = ["aluminum","ammonia","arsenic", "barium","cadmium", "chloramine","chromium","copper","flouride","bacteria","viruses","lead","nitrates","nitrites","mercury","perchlorate","radium","selenium","silver","uranium"]
        # get model features using list comprehension
        model_features = [getattr(user_input, i) for i in feature_list]
        # make prediction with model
        pred = getPredictions([model_features])
        self.object.pred = pred
        self.object.save()
        top_features = {
            "Aluminum": model_features[0],
            "Arsenic": model_features[2],
            "Barium": model_features[3],
            "Cadmium": model_features[4],
            "Chloramine": model_features[5],
            "Chromium": model_features[6],
            "Perchlorate": model_features[15],
            "Silver": model_features[18],
            "Uranium": model_features[19],
            "Viruses": model_features[10]
                        }
        # use the top features in results text and groupby function
        top_features_list = [i for i in top_features.values()]
        # return full df and groupby df
        full_df, group_df = loadReturnDf("waterquality_clean.csv")
        # create target_plot
        target_dist_plot = plot(targetDistribution(full_df), output_type="div")
        # create median_plot
        median_plot = plot(groupByDf(group_df,pred,top_features_list), output_type = "div")


        # show distribution of data


        # assign pred to context as pred
        context["pred"] = pred
        # assign influential features to context
        context["features"] = top_features
        # assign target distirbution plot to context
        context["target_distribution"] = target_dist_plot
        # assign groupby distribution plot to context
        context["median_distribution"] = median_plot
        return context

def post_detail(request):
    pass
