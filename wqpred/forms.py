from django import forms
from .models import UserInput
# FloatField
# IntegerField
# create forms
# class FormDetection(forms.Form):
#     aluminum = forms.FloatField(label="Aluminum reading", widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                                           'placeholder':'Aluminum reading'}),required=True)
#     ammonia = forms.FloatField(label="Ammonia reading", 
#                                  widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Ammonia reading'}),
#                                                                 required=True) 
#     arsenic = forms.FloatField(label="Arsenic reading",
#                                  widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                         'placeholder':'Arsenic reading'}),
#                                                                         required=True)
#     barium = forms.FloatField(label="Barium reading",
#                                 widget=forms.TextInput(attrs={'class': 'form-control',
#                                                             'placeholder':'Barium reading'}),
#                                                             required=True)
#     cadmium = forms.FloatField(label="Cadmium reading",
#                                  widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Cadmium reading'}),
#                                                                   required=True)
#     chloramine = forms.FloatField(label="Chloramine reading",
#                                     widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Chloramine reading'}),
#                                                                   required=True) 
#     chromium = forms.FloatField(label="Chromium reading",
#                                   widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Chromium reading'}), required=True)
#     copper = forms.FloatField(label="Copper reading", 
#                                 widget=forms.TextInput(attrs={'class': 'form-control',
#                                                             'placeholder':'Copper reading'}),required=True)
#     flouride = forms.FloatField(label="Flouride reading",
#                                   widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Flouride reading'}), required=True)
#     bacteria = forms.FloatField(label="Bacteria reading",
#                                   widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Bacteria reading'}), required=True) 
#     viru ses = forms.FloatField(label="Viruses reading",
#                                  widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Viruses reading'}), required=True)
#     lead = forms.FloatField(label="Lead reading",
#                               widget=forms.TextInput(attrs={'class': 'form-control',
#                                                             'placeholder':'Lead reading'}), required=True)
#     nitrates = forms.FloatField(label="Nitrates reading",
#                                   widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Nitrates reading'}), required=True)
#     nitrites = forms.FloatField(label="Nitrites reading", 
#                                   widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Nitrites reading'}),required=True) 
#     mercury = forms.FloatField(label="Mercury reading", 
#                                  widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Mercury reading'}),required=True)
#     perchlorate = forms.FloatField(label="Percholrate reading", 
#                                      widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                     'placeholder':'Perchlorate reading'}),required=True)
#     radium = forms.FloatField(label="Radium reading",
#                                 widget=forms.TextInput(attrs={'class': 'form-control',
#                                                             'placeholder':'Radium reading'}), required=True)
#     selenium = forms.FloatField(label="Selenium reading", 
#                                   widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Selenium reading'}),
#                                                                 required=True) 
#     silver = forms.FloatField(label="Silver reading", 
#                                 widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                 'placeholder':'Silver reading'}),required=True)
#     uranium = forms.FloatField(label="Uranium reading", 
#                                  widget=forms.TextInput(attrs={'class': 'form-control',
#                                                             'placeholder':'Uranium reading'}),required=True)
# create a ModelForm
class FormDetection(forms.ModelForm):
    class Meta:
        model = UserInput
        fields="__all__"
        # exclude = ["pred"]
        widgets = {
            "aluminum":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Aluminum reading" 
                       }),
            "ammonia":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Ammonia reading" 
                       }),
            "arsenic":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Arsenic reading" 
                       }),
            "barium":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Barium reading" 
                       }),
            "cadmium":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Cadmium reading" 
                       }),
            "chloramine":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Chloramine reading" 
                       }),
            "chromium":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Chromium reading" 
                       }),
            "copper":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Copper reading" 
                       }),
            "flouride":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Flouride reading" 
                       }),
            "bacteria":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Bacteria reading" 
                       }),
            "viruses":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Viruses reading" 
                       }),
            "lead":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Lead reading" 
                       }),
            "nitrates":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Nitrates reading" 
                       }),
            "nitrites":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Nitrites reading" 
                       }),
            "mercury":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Mercury reading" 
                       }),
            "perchlorate":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Perchlorate reading" 
                       }),
            "radium":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Radium reading" 
                       }),
            "selenium":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Selenium reading" 
                       }),
            "silver":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Silver reading" 
                       }),
            "uranium":forms.TextInput(
                attrs={'class': 'form-control',
                       "placeholder": "Uranium reading" 
                       }),
            
            
            

        }
        labels = {
            "aluminum": "Aluminum"
        }
        # error_messages = {

        # }
