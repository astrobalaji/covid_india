from django.shortcuts import render
import pandas as pd
from .models import med_serv
from covid_india import settings
from sqlalchemy import create_engine

# Create your views here.
def update_from_csv():
    df = pd.read_csv("../data/Remedesivir_cleaned.csv")
    conn_default = create_engine(settings.DATABASES['default']['name']).connect()

    df.to_sql(med_serv._meta.db_table, index = False, con = conn_default)
