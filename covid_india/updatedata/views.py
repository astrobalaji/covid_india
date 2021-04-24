from django.shortcuts import render
import pandas as pd
import numpy as np
import json

from medical_services.models import med_serv
from food_services.models import food_ser
from hospitals.models import hosp_dat
from oxygen_supliers.models import oxy_sup

state_code = json.load(open("lookup_data/state_code.json", 'r'))
state_lis = list(state_code.keys())


# Create your views here.
def med_serv_update_from_csv():
    med_serv.objects.all().delete()
    df = pd.read_csv("../data/Remedesivir_cleaned.csv")
    df = df.fillna('')
    med_serv.objects.bulk_create(med_serv(**vals) for vals in df.to_dict('records'))

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def normalize_state(name):
    df_temp = pd.DataFrame()
    df_temp['state_in'] = state_lis
    df_temp['similarity'] = df_temp['state_in'].apply(lambda x: jaccard_similarity(x, name))
    df_temp.sort_values(by = 'similarity', ascending = False, inplace = True)
    return df_temp.head(1)['state_in'].values[0]

def food_serv_update():
    food_ser.objects.all().delete()
    state_gcode = [
        ('MH', '0'),
        ('DL', '794930816'),
        ('KA', '350566634'),
        ('GJ', '74720744'),
        ('TN', '808242085'),
        ('TS', '712364823'),
        ('UP', '1541971071'),
        ('RJ', '1602193910'),
        ('WB', '1764758064'),
        ('BR','1882298724'),
        ('MP', '309838706'),
        ('CG', '1335404210'),
        ('OD', '1375698813'),
        ('JK', '1123862156'),
        ('AP', '176500685'),
        ('KL', '1717527069'),
        ('UK', '1647185593'),
        ('PB', '79336741'),
        ('AS', '274482358'),
        ('JH', '834966747')
    ]


    city_lis = ['Mumbai', 'Delhi', 'Bengaluru', 'Vadodara', 'Chennai', 'Hyderabad', 'Lucknow', 'Kota', 'Kolkata', 'Patna',
    'Bhopal', 'Durg & Bhilai', 'Bhubaneswar', 'Jammu', 'Vishakhapatnam', 'Kottayam', 'Rishikesh', 'Chandigarh',
    'Guwahati', 'Ranchi']
    for i in range(len(state_gcode)):
        state = state_gcode[i]
        city = city_lis[i]

        temp_df = pd.read_csv("https://docs.google.com/spreadsheets/d/1wu80sP5tq2k9bfxjuzUfRORxPDf07gUALfLMrOv-YEI/export?format=csv&gid={0}".format(state[1]))
        col1 = temp_df.columns[5]
        i = 0
        while i!=len(temp_df):
            if type(temp_df.loc[i, col1]) == str:
                break
            else:
                i += 1
        temp_df.columns = ['City']+list(temp_df.loc[i])[1:]
        temp_df.drop(list(range(i+1)), axis = 0, inplace = True)
        temp_df.dropna(subset = ["Number"], inplace = True)
        for i, row in temp_df.iterrows():
            if type(row['City']) == str:
                city = row['City']

            temp_df.at[i, 'City'] = city
        temp_df.drop(temp_df.filter(like = 'Unnamed').columns, axis = 1, inplace = True)
        temp_df['State'] = [state[0]]*len(temp_df)
        rename_dict = {"Hours of Delivery":"Hours",
               "Email/Instagram/Links":"Social",
               "Delivery Options":"Delivery"}
        col_list = ['State', 'City', 'Area', 'Name', 'Number', 'Hours', 'Service', 'Social', 'Delivery']
        temp_df.rename(columns = rename_dict, inplace = True)
        temp_df = temp_df[col_list]
        temp_df = temp_df.fillna('')
        try:
            food_ser.objects.bulk_create(food_ser(**vals) for vals in temp_df.to_dict('records'))
        except:
            print(state,"failed!!!")

def hospital_update():
    hosp_dat.objects.all().delete()
    df = pd.read_csv('../data/hospitals_cleaned.csv')
    df['state_code'] = df['state'].apply(lambda x: state_code[x])
    df = df.fillna('')
    hosp_dat.objects.bulk_create(hosp_dat(**vals) for vals in df.to_dict('records'))

def oxygen_update():
    sheet_url = "https://docs.google.com/spreadsheets/d/1fHiBtzxBC_3Q7I5SXr_GpNA4ivT73w4W4hjK6IkGDBY/export?format=csv&gid=2074968679"
    df = pd.read_csv(sheet_url)
    df.dropna(subset = ['State'], inplace = True)
    df['State'] = df['State'].apply(normalize_state)
    df['state_code'] = df['State'].apply(lambda x: state_code[x])
    df.fillna('', inplace = True)
    df = df[['state_code', 'State', 'City', 'Contact', 'Number']]
    oxy_sup.objects.bulk_create(oxy_sup(**vals) for vals in df.to_dict('records'))

def index(request):
    med_serv_update_from_csv()
    food_serv_update()
    #hospital_update()
    return render(request, 'good_karma.html')
