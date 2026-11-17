import requests
b='http://frontend:8080'; s=requests.Session(); s.post(b+'/api/method/login',data={'usr':'portal@example.invalid','pwd':'assessment-demo'})
for p in ['/orders','/invoices','/orders/SAL-ORD-2026-00001','/orders/SAL-ORD-2026-00002','/invoices/ACC-SINV-2026-00001','/invoices/ACC-SINV-2026-00002','/api/resource/Sales%20Order/SAL-ORD-2026-00002','/api/resource/Sales%20Invoice/ACC-SINV-2026-00002']:
 r=s.get(b+p,allow_redirects=False); print(p,r.status_code,'Northstar', 'Northstar Workshop' in r.text,'Bluebird','Bluebird Outfitters' in r.text, 'location',r.headers.get('Location'), 'bytes',len(r.content))
