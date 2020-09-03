from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import re
import pickle
#형태소 분석기 Mecab 사용을위함
from konlpy.tag import Mecab
mecab = Mecab()
#학습된 모델을 저장하고 불러오기위한 lib

import sklearn.externals
import joblib
# Tfidf 벡터화를 하기 위함
from sklearn.feature_extraction.text import TfidfVectorizer

# Create your views here.
def index(request):
    return render(request, "index.html")

def index2(request):
    return render(request,'index2.html')

def complaint_input_form(request):
    return render(request,'complaint_input.html')

def complaint_input(request):
    #post형식 데이터 받아오기
    input_area = request.POST['area']
    input_title = request.POST['title']
    input_text = request.POST['text']
    
    # 메캅으로 text 형태소 제거하기    
    input_text =mecab.nouns(input_text)
    # 불용어 제거하기
    stopwords = pd.read_csv('/root/teamProject/complaintPrj/BigData_Project/main/ML_Data/stop_words.csv')
    stopwords = stopwords.stopwords.to_list()
    stopwords_set = set(stopwords)
    text_result = [word for word in input_text if not word in stopwords_set]

    # 벡터화 하기 위한 역토큰화 (토큰화 작업을 역으로 되돌림)
    text_list = []
    text = ''
    text = text+str(text_result)
    text = re.sub('[\[\]\'\'\,]', '',text)
    text_list.append(text)

    #tfidf 벡터화 위한 단어 빈도데이터 가져오기
    f = open("/root/teamProject/complaintPrj/BigData_Project/main/ML_Data/text_list.pickle",'rb')
    X = pickle.load(f)
    f.close()

    # Tfidf벡터화
    vector_X = TfidfVectorizer()
    vector_X.fit_transform(X)
    text_tfidf_vec = vector_X.transform(text_list)

    # 학습된 xgb모델 불러오기
    xgb = joblib.load('/root/teamProject/complaintPrj/BigData_Project/main/ML_Data/xgboost_model.pkl')

    result_output = ''
    # xgb 모델에서 결과 가져오기
    result_label = xgb.predict(text_tfidf_vec)
    department=pd.read_csv('/root/teamProject/complaintPrj/BigData_Project/main/ML_Data/department_labels.csv')
    for i in range(len(department['구'])):
        if (department['구'][i] == input_area and department['labels'][i] == result_label):
            result_output = department['과'][i]
            break

    qs = {'area' : input_area , 'result':result_output , 'label' : result_label}

    return render(request , 'result.html',qs)
