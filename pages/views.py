from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponse
from .report import ReportSeo
class HomePageView(TemplateView):
    template_name = "home.html"


class SeoPage(TemplateView):
    template_name = "seo.html"
    def dispatch(self, request, *args, **kwargs):
        if not(request.user.is_authenticated):
            return redirect('http://localhost:8000/accounts/login/')
        return super(SeoPage, self).dispatch(request, *args, **kwargs)



def score_number(number):
    if number==0:
        return "Bad"
    elif number==1:
        return "Good"
    else:
        return "Very Good"
    
class report_page(TemplateView):
    template_name = "report.html"
    def dispatch(self, request, *args, **kwargs):
        if not(request.user.is_authenticated):
            return redirect('http://localhost:8000/accounts/login/')
        # elif request.GET.get('url'):
        elif True:
            url=request.GET.get('url')
            type(url)
            rp=ReportSeo()
            rp.url=url
            report=rp.analyze_seo()
            
            
            title=report["title"][0]
            score_title=report["title"][1]
            len_title=len(report["title"][0])
            
            
            description=report["description"][0]
            score_description=report["description"][1]
            len_description=len(report["description"][0])
            
            
            h1=report["h1"]
            count_h1=len(h1)
                
            h2=report["h2"]
            count_h2=len(h2)
            
            h3=report["h3"]
            count_h3=len(h3)
            
            h4=report["h4"]
            count_h4=len(h4)
            
            h5=report["h5"]
            count_h5=len(h5)
            
            h6=report["h6"]
            count_h6=len(h6)  
            
            sitemap=report["sitemap"]
            robots=report["robots"]       
            
            
            return render(request, "report.html",{
                "title":title,
                "score_title":score_title,
                "len_title":len_title,
                
                "description":description,
                "score_description":score_description,
                "len_description":len_description,
                
                "h1":h1,
                "count_h1":count_h1,
                
                "h2":h2,
                "count_h2":count_h2,
                
                
                "h3":h3,
                "count_h3":count_h3,
                
                
                "h4":h4,
                "count_h4":count_h4,
                
                
                "h5":h5,
                "count_h5":count_h5,
                
                
                "h6":h6,
                "count_h6":count_h6,
                
                "sitemap":sitemap,
                "robots":robots,
                

                
                })
        else:
            return redirect('http://localhost:8000/')

        