# web_scrap_googleforms

This project it´s to make web scraping to send the google forms entered by a file in this case horas.xml

The procedure it´s following

-Copy the Webdriver to C:\WebDriver
-Working version with chrome
-change the Filepath from xml file on the script
-fill script with the google forms pre-filled path, separators are not needed, script will find all the different paths checking the header https:

#PREFILL GOOGLE FORM
to prefill the Google form you need to get the id from html like example bellow


for this form : https://docs.google.com/forms/d/e/1FAIpQLSeC1SZdzpVFktyhnRiGO6SDLRLvRHu8NGLBcvK-wbvH2JW5og/viewform

find on command windows developer the following info:
  data-params
you should find something similiar to this for each text box:

  data-params='%.@.[1633920210,"Name",null,0,[[2005620554,[],true,[],[],null,null,null,null,null,[null,[]]]],null,null,null,[]],"i1","i2","i3",false]'
  
  so to prefill you need to use the code:  2005620554
  
and add to the normal path

"https://docs.google.com/forms/d/e/1FAIpQLSeC1SZdzpVFktyhnRiGO6SDLRLvRHu8NGLBcvK-wbvH2JW5og/viewform" + "?&entry.2005620554=HELLO"
final format will be :

"https://docs.google.com/forms/d/e/1FAIpQLSeC1SZdzpVFktyhnRiGO6SDLRLvRHu8NGLBcvK-wbvH2JW5og/viewform?&entry.2005620554=HELLO"
