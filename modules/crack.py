import re
import os
import requests
import json
import threading
from urllib.parse import quote
from requests.exceptions import RequestException
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import concurrent.futures
from utils.colors import (
    white,
    red,
    green,
    yellow,
    end,
    back,
    info,
    que,
    bad,
    good,
    run,
    red_line,
)

timeout = 30
retry_cnt = 2
common_headers = {u"User-Agent": u"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

# md5-16, md5-32
def tellyou(passwd):
    url = u"http://md5.tellyou.top/MD5Service.asmx/HelloMd5"
    try_cnt = 0
    while True:
        try:
            params = {u"Ciphertext": passwd}
            headers = dict(common_headers, **{u"X-Forwarded-For": u"192.168.1.1"})
            req = requests.get(url, params=params, headers=headers, timeout=timeout)
            result = re.findall(r'<string xmlns="http://tempuri.org/">(.*?)</string>', req.text)
            if result:
                print(f"%s tellyou: {result[0]}%s"% (good, end))
            else:
                print(f"%s tellyou: NotFound %s"%(bad, end))
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print(f"%s tellyou: RequestError %s" % (bad, end))
                break
        except:
            print(f"%s tellyou: Error: EXCEPTION OCCURED %s" % (bad, end))
            break

# md5-16, md5-32, sha1, mysql323, mysql5, discuz
def chamd5(passwd, type):
    url = u"https://www.chamd5.org/"
    try_cnt = 0
    while True:
        try:
            s = requests.Session()
            headers = dict(common_headers, **{u"Content-Type": u"application/json", u"Referer": url,
                                              u"X-Requested-With": u"XMLHttpRequest"})
            data = {u"email": u"jxtepz93152@chacuo.net", u"pass": u"!Z3jFqDKy8r6v4", u"type": u"login"}
            s.post(u"{0}HttpProxyAccess.aspx/ajax_login".format(url), headers=headers, data=json.dumps(data),
                   timeout=timeout, verify=False)

            data = {u"hash": passwd, u"type": type}
            req = s.post(u"{0}HttpProxyAccess.aspx/ajax_me1ody".format(url), headers=headers, data=json.dumps(data),
                         timeout=timeout, verify=False)
            rsp = req.json()
            msg = re.sub(r"<.+?>", u"", json.loads(rsp[u"d"])[u"msg"])
            if msg.find(u"\u7834\u89e3\u6210\u529f") > 0:
                plain = re.findall(r"\u660e\u6587:(.+?)\u6570\u636e\u6765\u6e90", msg)[0].strip()
                print(f"%s chamd5: {plain} %s" % (good, end))
            elif msg.find(u"\u91d1\u5e01\u4e0d\u8db3") >= 0:
                print(f"%s chamd5: {msg} %s" % (bad, end))
            else:
                print(f"%s chamd5: NotFound %s" % (bad, end))
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print(f"%s chamd5: RequestError %s" % (bad, end))
                break
        except:
            print(f"%s chamd5: Error: EXCEPTION OCCURED %s" % (bad, end))
            break

# md5-32
def gromweb(passwd):
    url = u"https://md5.gromweb.com/"
    try_cnt = 0
    while True:
        try:
            params = {u"md5": passwd}
            req = requests.get(url, headers=common_headers, params=params, timeout=timeout, verify=False)
            rsp = req.text
            if rsp.find(u"succesfully reversed") > 0:
                plain = re.findall(r'<em class="long-content string">(.*?)</em>', rsp)[0]
                print(f"%s gromweb: {plain} %s" % (good, end))
            else:
                print(f"%s gromweb: NotFound %s" % (bad, end))
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print(f"%s gromweb: RequestError %s" % (bad, end))
                break
        except:
            print(f"%s gromweb: Error: EXCEPTION OCCURED %s" % (bad, end))
            break

# md5-32
def myaddr(passwd):
    url = u"http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
    try_cnt = 0
    while True:
        try:
            data = {u"md5": passwd}
            req = requests.post(url, headers=common_headers, data=data, timeout=timeout)
            result = re.findall(r"Hashed string</span>:\s(.+?)</div>", req.text)
            if result:
                print(f"%s myaddr: {result[0]} %s" % (good, end))
            else:
                print(f"%s myaddr: NotFount %s" % (bad, end))
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print(f"%s myaddr: RequestError %s" % (bad, end))
                break

# md5-32, sha1, sha256, sha384, sha512
def hashtoolkit(passwd):
    url = u"https://hashtoolkit.com/reverse-hash/"
    try_cnt = 0
    while True:
        try:
            params = {u"hash": passwd}
            req = requests.get(url, headers=common_headers, params=params, timeout=timeout, verify=False)
            rsp = req.text
            if rsp.find(u"No hashes found for") > 0:
                print(f"%s hashtoolkit: NotFound %s" % (bad, end))
            else:
                plain = re.findall(r'<a href="/generate-hash/\?text=(.*?)"', rsp, re.S)[0]
                print(f"%s hashtoolkit: {quote(plain)} %s" % (good, end))
            break
        except RequestException:
            try_cnt += 1
            if try_cnt >= retry_cnt:
                print(f"%s hashtoolkit: RequestError %s" % (bad, end))
                break
        except:
            print(f"%s hashtoolkit: Error: EXCEPTION OCCURED %s" % (bad, end))
            break
def crack(passwd):
    threads = [threading.Thread(target=hashtoolkit, args=(passwd,))]
    if len(passwd) == 41 and re.match(r'\*[0-9a-f]{40}|\*[0-9A-F]{40}', passwd):
        threads.append(threading.Thread(target=chamd5, args=(passwd[1:], u"300",)))
    elif len(passwd) == 40 and re.match(r'[0-9a-f]{40}|[0-9A-F]{40}', passwd):
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"100",)))
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"300",)))
    elif len(passwd) == 32 and re.match(r'[0-9a-f]{32}|[0-9A-F]{32}', passwd):
        # threads.append(threading.Thread(target=pmd5, args=(passwd,)))
        # threads.append(threading.Thread(target=xmd5, args=(passwd,)))
        # threads.append(threading.Thread(target=navisec, args=(passwd,)))
        # threads.append(threading.Thread(target=nitrxgen, args=(passwd,)))
        threads.append(threading.Thread(target=myaddr, args=(passwd,)))
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"md5",)))
        threads.append(threading.Thread(target=gromweb, args=(passwd,)))
        # threads.append(threading.Thread(target=bugbank, args=(passwd,)))
        threads.append(threading.Thread(target=tellyou, args=(passwd,)))
    elif len(passwd) == 16 and re.match(r'[0-9a-f]{16}|[0-9A-F]{16}', passwd):
        # threads.append(threading.Thread(target=pmd5, args=(passwd,)))
        # threads.append(threading.Thread(target=xmd5, args=(passwd,)))
        # threads.append(threading.Thread(target=navisec, args=(passwd,)))
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"md5",)))
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"200",)))
        # threads.append(threading.Thread(target=bugbank, args=(passwd,)))
        threads.append(threading.Thread(target=tellyou, args=(passwd,)))
    elif passwd.find(':') > 0:
        threads.append(threading.Thread(target=chamd5, args=(passwd, u"10",)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()