# Benchmark entry added after the competition deadline. The entry simply uses the last known value.
# Based on an MATLAB script by Daniel Alexander and Neil Oxtoby.
# ============
# Authors:
#   Razvan Valentin-Marinescu

## Read in the TADPOLE data set and extract a few columns of salient information.
# Script requires that TADPOLE_D1_D2.csv is in the parent directory. Change if
# necessary

import pandas as pd
import numpy as np
import os
import sys

from tadpole_algorithms.models.tadpole_model import TadpoleModel

import datetime as dt
from dateutil.relativedelta import relativedelta

import logging

from datetime import datetime
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)
#this import is for use R code into Python
from rpy2 import robjects
from rpy2.robjects.packages import importr
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector
#to transform r to python df
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

class BenchmarkSVM_R(TadpoleModel):

    def R_df_to_python_df(self,R_df,csvname=""):
        #func to convert a R df into python and if a csvname is specified can be saved
        pandas2ri.activate()
        d_from_r_df = pd.DataFrame()
        with localconverter(robjects.default_converter + pandas2ri.converter):
            pd_from_r_df = robjects.conversion.rpy2py(tidy_df)
        if csvname :
            pd_from_r_df.to_csv(csvname)
        return pd_from_r_df

    def Python_df_to_R_df(self,Python_df):
        #func to convert a Python df into R DF
        pandas2ri.activate()
        r_from_pd_df = robjects.DataFrame({})
        with localconverter(robjects.default_converter + pandas2ri.converter):
            r_from_pd_df = robjects.conversion.py2rpy(Python_df)
        return r_from_pd_df


##################################### final functions   
    def preproc_tadpole_D1_D2(self,Tadpole_D1_D2,usePreProc=True):
        #using the usePreProc flag you can select between use the preprocess model results or not
        if usePreProc == False:
            preproc_tadpole_D1_D2_RSCRIPT = ""
            Tadpole_D1_D2.to_csv("data/temp/train_df.csv")        
            with open('R_scripts/preproc_tadpole_D1_D2.r', 'r') as file: 
                preproc_tadpole_D1_D2_RSCRIPT = file.read()
            #replace the values on the script with the actual atributes needed (its like pasing arguments in a function)   
            #preproc_tadpole_D1_D2_RSCRIPT = preproc_tadpole_D1_D2_RSCRIPT.replace("_preTrain_",str(usePreProc))
            preproc_tadpole_D1_D2_RFUNC = robjects.r(preproc_tadpole_D1_D2_RSCRIPT)
            #load the result of preprocesing of Tadpole_d1_d2

        AdjustedTrainFrame = pd.read_csv("data/temp/dataTadpole$AdjustedTrainFrame.csv")
        testingFrame = pd.read_csv("data/temp/dataTadpole$testingFrame.csv")
        Train_Imputed = pd.read_csv("data/temp/dataTadpole$Train_Imputed.csv")
        Test_Imputed = pd.read_csv("data/temp/dataTadpole$Test_Imputed.csv")

        return AdjustedTrainFrame,testingFrame,Train_Imputed,Test_Imputed

    def preproc_tadpole_D3(self,Tadpole_D3,usePreProc=True):
        #using the usePreProc flag you can select between use the preprocess model results or not
        if usePreProc == False :
            preproc_tadpole_D3_RSCRIPT = ""
            Tadpole_D3.to_csv("data/TADPOLE_D3.csv")        
            with open('R_scripts/preproc_tadpole_D3.r', 'r') as file: 
                preproc_tadpole_D3_RSCRIPT = file.read()
            #replace the values on the script with the actual atributes needed (its like pasing arguments in a function)   
            #preproc_tadpole_D3_RSCRIPT = preproc_tadpole_D3_RSCRIPT.replace("_preTrain_",str(usePreProc))
            preproc_tadpole_D3_RFUNC = robjects.r(preproc_tadpole_D3_RSCRIPT)
            #load the result of preprocesing of Tadpole_D3

        AdjustedTrainFrame = pd.read_csv("data/temp/dataTadpoleD3$AdjustedTrainFrame.csv")
        testingFrame = pd.read_csv("data/temp/dataTadpoleD3$testingFrame.csv")
        Train_Imputed = pd.read_csv("data/temp/dataTadpoleD3$Train_Imputed.csv")
        Test_Imputed = pd.read_csv("data/temp/dataTadpoleD3$Test_Imputed.csv")

        return AdjustedTrainFrame,testingFrame,Train_Imputed,Test_Imputed



    def Forecast_D2(self,AdjustedTrainFrame,testingFrame,Train_Imputed,Test_Imputed,usePreProc=True):
        if usePreProc == False :
            Forecast_D2_RSCRIPT = ""
            #Tadpole_D1_D2.to_csv("data/temp/train_df.csv")        
            with open('R_scripts/Forecast_D2.r', 'r') as file: 
                Forecast_D2_RSCRIPT = file.read()
            Forecast_D2_RFUNC = robjects.r(Forecast_D2_RSCRIPT)
        ForecastD2_BORREGOS_TEC = pd.read_csv("data/temp/_ForecastD2_BORREGOS_TEC.csv")
        return ForecastD2_BORREGOS_TEC


    def Forecast_D2_HLCM_EM(self,AdjustedTrainFrame,testingFrame,Train_Imputed,Test_Imputed,usePreProc=True):
        if usePreProc == False :
            Forecast_D2_RSCRIPT = ""
            #Tadpole_D1_D2.to_csv("data/temp/train_df.csv")        
            with open('R_scripts/Forecast_D2_HLCM_EM.R', 'r') as file: 
                Forecast_D2_RSCRIPT = file.read()
            Forecast_D2_RFUNC = robjects.r(Forecast_D2_RSCRIPT)
        ForecastD2_BORREGOS_TEC = pd.read_csv("data/temp/HLCM_EM_ForecastD2_BORREGOS_TEC.csv")
        return ForecastD2_BORREGOS_TEC

    def Forecast_D3(self,AdjustedTrainFrame,testingFrame,Train_Imputed,Test_Imputed,usePreProc=True):
        if usePreProc == False :
            Forecast_D3_RSCRIPT = ""
            with open('R_scripts/Forecast_D3.r', 'r') as file: 
                Forecast_D3_RSCRIPT = file.read()       
            Forecast_D3_RFUNC = robjects.r(Forecast_D3_RSCRIPT)
        ForecastD3_BORREGOS_TEC = pd.read_csv("data/temp/_ForecastD3_BORREGOS_TEC.csv")
        return ForecastD3_BORREGOS_TEC

    def Forecast_D3_HLCM_EM(self,AdjustedTrainFrame,testingFrame,Train_Imputed,Test_Imputed,usePreProc=True):
        if usePreProc == False :
            Forecast_D3_RSCRIPT = ""
            with open('R_scripts/Forecast_D3_HLCM_EM.R', 'r') as file: 
                Forecast_D3_RSCRIPT = file.read()       
            Forecast_D3_RFUNC = robjects.r(Forecast_D3_RSCRIPT)
        ForecastD3_BORREGOS_TEC = pd.read_csv("data/temp/HLCM_EM_ForecastD3_BORREGOS_TEC.csv")
        return ForecastD3_BORREGOS_TEC
###############################################

#end R functions
    def preprocess(self, path_d1="data/TADPOLE_D1_D2.csv",
    path_dict="data/TADPOLE_D1_D2_Dict.csv",
    path_d3="data/TADPOLE_D3.csv"):
        tamez_tidying = ""
        with open('R_scripts/tamez_tadpole_tidying.txt', 'r') as file:
            #this file contains magic R scrpits 
            tamez_tidying = file.read()
            tamez_tidying_function = robjects.r(tamez_tidying)
            tidy_df = tamez_tidying_function(path_d1,path_dict,path_d3)
            #save_Robject= robjects.r("save")
            #save_Robject(tidy_df,file="tidy_df.RDATA")
            return tidy_df

    def train(self, train_df):
        return super().train(train_df)

    def predict(self, test_df):
        logger.info("Predicting")

        # select last row per RID
        test_df = test_df.sort_values(by=['EXAMDATE'])
        test_df = test_df.groupby('RID').tail(1)
        exam_dates = test_df['EXAMDATE']

        test_df = self.preprocess(test_df)
        
        # Select same columns as for traning for testing
        test_df = test_df[["RID", "Diagnosis", "ADAS13", "Ventricles_ICV"]]

        # Default values
        Ventricles_typical = 25000
        Ventricles_broad_50pcMargin = 20000  # +/- (broad 50% confidence interval)
        Ventricles_default_50pcMargin = 1000  # +/- (broad 50% confidence interval)
        ADAS13_typical = 12
        ADAS13_broad_50pcMargin = 10 
        ADAS13_default_50pcMargin = 1
        
        subjects = test_df["RID"].unique()
        diag_probas = np.zeros([len(subjects),3])
        adas_prediction = np.zeros(len(subjects))
        adas_ci = np.zeros(len(subjects))
        ventricles_prediction = np.zeros(len(subjects))
        ventricles_ci = np.zeros(len(subjects))
        for i, subject in enumerate(subjects):
            diag_probas[i, int(test_df.loc[test_df["RID"] == subject, "Diagnosis"].dropna().values.tolist()[-1])-1] = 1
            
            adas_prediction[i] = test_df.loc[test_df["RID"] == subject, "ADAS13"].dropna().values.tolist()[-1]
            if adas_prediction[i] > 0: 
                adas_ci[i] = ADAS13_default_50pcMargin
                adas_ci[i] = ADAS13_default_50pcMargin
            else:
                # Subject has no history of ADAS13 measurement, so we'll take a
                # typical score of 12 with wide confidence interval +/-10.
                adas_prediction[i] = ADAS13_typical 
                adas_ci[i] = ADAS13_broad_50pcMargin
            
            try:
                ventricles_prediction[i] = test_df.loc[test_df["RID"] == subject, "Ventricles_ICV"].dropna().values.tolist()[-1]    
            except IndexError:
                print(test_df.loc[test_df["RID"] == subject, "Ventricles_ICV"].dropna().values.tolist())
                
            if ventricles_prediction[i] > 0: 
                ventricles_ci[i] = Ventricles_default_50pcMargin
            else:
                # Subject has no imaging history, so we'll take a typical
                # ventricles volume of 25000 & wide confidence interval +/-20000
                ventricles_prediction[i] = Ventricles_typical
                ventricles_ci[i] = Ventricles_broad_50pcMargin 
        
        diag_probas_t = diag_probas.T.copy()

        def add_months_to_str_date(strdate, months=1):
            try:
                return (datetime.strptime(strdate, '%Y-%m-%d') + relativedelta(months=months)).strftime('%Y-%m-%d')
            except ValueError:
                return (datetime.strptime(strdate, '%d/%m/%Y') + relativedelta(months=months)).strftime('%d/%m/%Y')

        df = pd.DataFrame.from_dict({
            'RID': subjects,
            'month': 1,
            'Forecast Date': list(map(lambda x: add_months_to_str_date(x, 1), exam_dates.tolist())),
            'CN relative probability': diag_probas_t[0],
            'MCI relative probability': diag_probas_t[1],
            'AD relative probability': diag_probas_t[2],

            'ADAS13': adas_prediction,
            'ADAS13 50% CI lower': adas_prediction - adas_ci, # To do: Set to zero if best-guess less than 1.
            'ADAS13 50% CI upper': adas_prediction + adas_ci,

            'Ventricles_ICV': ventricles_prediction,
            'Ventricles_ICV 50% CI lower': ventricles_prediction - ventricles_ci,
            'Ventricles_ICV 50% CI upper': ventricles_prediction + ventricles_ci,
        })

        # copy each row for each month
        new_df = df.copy()
        for i in range(2, 12 * 10):
            df_copy = df.copy()
            df_copy['month'] = i
            df_copy['Forecast Date'] = df_copy['Forecast Date'].map(lambda x: add_months_to_str_date(x, i - 1))
            new_df = new_df.append(df_copy)

        return new_df
    


