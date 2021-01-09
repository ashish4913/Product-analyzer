from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Create your views here.
def home(request):
    return render(request,'home.html')
def flipkart(request):
    if request.method=='POST':
        
        site_url=request.POST.get('url')
        print(site_url)
        
        headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        response=requests.get(site_url,headers=headers)
        soup=BeautifulSoup(response.content,'html.parser')
        title=soup.find("span",{"class":"B_NuCI"}).get_text()
        print(title)
        price=soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()

        #getting highlights..
        highlights=[]
        for i in soup.findAll("li",{"class":"_21Ahn-"}):
            highlights.append(i.text)

        #scrap ratting
        rating=soup.find("div",{"class":"_2d4LTz"},text=True).get_text()

        

        #scrap reviews
        url2=site_url.replace("/p/", "/product-reviews/", 1)
        url_pages=[]
        for i in range(1,5):
            url_pages.append(url2+"&page="+str(i))
        
        final_review2=[]

        for i in url_pages:
            t=requests.get(i)
            page_soup=BeautifulSoup(t.content,'html.parser')
            for row in page_soup.find_all('div',attrs={"class" : "t-ZTKy"}):
                final_review2.append(row.text)  

            #sentiment analysis
            positive=[]
            negative=[]
            nltk.download('vader_lexicon')

            sid = SentimentIntensityAnalyzer()
            #sentence=["nice",'bad','very nice','very bad']
            for i in final_review2:
                result=sid.polarity_scores(i)
                if(result['pos']>=result['neg']):
                    positive.append(i[0:len(i)-9])
                else:
                    negative.append(i[0:len(i)-9])



        total=len(positive)+len(negative)
        #pie chart
        labels= ['Positive_review,Negative_review']
        data=[len(positive),len(negative)]

        

       


        d={'title':title,'price':price,'highlights': highlights,'rating':rating,'reviews':final_review2,'positive':positive,'negative':negative,'total':total,'labels':labels,'data':data}
     
        return render (request,'flipkart_details.html',d)

















    return render(request,'flipkart.html')



   
   
    