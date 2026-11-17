import requests
base='http://127.0.0.1:8080'
users=['Administrator','portal@example.invalid','sales@example.invalid','accounts@example.invalid','viewer@example.invalid']
for u in users:
 s=requests.Session(); r=s.post(base+'/api/method/login',data={'usr':u,'pwd':'admin' if u=='Administrator' else 'assessment-demo'}); print('\nUSER',u,'login',r.status_code)
 for d in ['Customer','Sales Order','Sales Invoice','Purchase Order','File']:
  r=s.get(base+'/api/resource/'+d,params={'fields':'["name"]','limit_page_length':20}); print('LIST',d,r.status_code,r.text[:600])
 for path in ['/private/files/fictional-note-1.txt','/private/files/fictional-note-2.txt']:
  r=s.get(base+path,allow_redirects=False); print('FILE',path,r.status_code,r.text[:120])
