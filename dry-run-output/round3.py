import requests
b='http://frontend:8080'
for u in ['sales@example.invalid','accounts@example.invalid','viewer@example.invalid']:
 s=requests.Session(); s.post(b+'/api/method/login',data={'usr':u,'pwd':'assessment-demo'})
 for d in ['GL Entry','Payment Entry','Journal Entry','Account']:
  r=s.get(b+'/api/resource/'+d,params={'fields':'["name"]','limit_page_length':5}); print(u,d,r.status_code,r.text[:100])
