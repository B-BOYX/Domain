import os,sys,requests,re,json,uuid,random,string,time,io,struct,base64
from uuid import UUID
from string import *

client_id = '6628568379'
client_secrets = 'c1e620fa708a1d5696fb991c1bde5662'

roman = ['X','X','X','X','12','13']
ver = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits) for _ in range(5))
ua_ios = 'Mozilla/'+str(random.randrange(1,9))+'.0 (iPhone; CPU iPhone OS '+str(random.randint(10,15))+'_'+str(random.randrange(1,9))+' like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ver+' [FBAN/FBIOS;FBDV/iPhone'+str(random.randint(8,13))+',1;FBMD/iPhone;FBSN/iOS;FBSV/'+str(random.randint(11,99))+'.'+str(random.randrange(1,9))+';FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]'


ua ="Mozilla/5.0 (iPad; CPU iPad OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/MessengerForiOS;FBAV/142.0.0.38.63;FBBV/77803202;FBDV/iPad8,4;FBMD/iPad;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/NOS;FBID/phone;FBLC/jv_ID;FBOP/5;FBRV/77803202]"
print(ua)
print('\n\n\n')
#print('Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]')
adid = str(uuid.uuid4())
device_id = str(uuid.uuid4())
li = ['28','29','210']
li2 = random.choice(li)
j1 = ''.join(random.choice(digits) for _ in range(2))
j2 = li2+j1
iid = "100087626332166"
pas = "ali12@@@"
data = {
    'adid':adid,
    'format':'json',
    'api_key':client_id,
    'community_id':'',
    'device_id':device_id,
    'family_device_id':device_id,
    'currently_logged_in_userid':'0',
    'try_num':'1',
    'email':iid,
    'password':pas,
    'jazoest':j2,
    'generate_analytics_claim':'1',
    'cpl':'true',
    'generate_session_cookies':'1',
#    'sim_serials':'%5B%2289014103211118510720%22%5D',
    'credentials_type':'password',
    'error_detail_type':'button_with_disabled',
    'source':'auth.login',
    'locale':'en_PK',
    'client_country_code':'PK',
    'advertising_id':adid,
    'meta_inf_fbmeta':'NO_FILE',
    'fb_api_req_friendly_name':'authenticate',
    'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
    'access_token':f'{client_id}|{client_secrets}'
}

head = {
    'Authorization':f'OAuth {client_id}|{client_secrets}',
    'X-FB-Connection-Quality':'EXCELLENT',
    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
    'x-fb-net-hni':str(random.randint(3e7,4e7)),
    'x-fb-connection-type':'unknown',
    'x-fb-friendly_name':'authenticate',
    'content-encoding':'application/x-www-form-urlencoded',
    'x-tigon-is_retry':'false',
    'x-fb-http-engine':'Liger',
    'user-agent':ua}
url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
po = requests.post(url,data=data,headers=head,allow_redirects=False).text
print(po)
 