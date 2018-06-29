import requests
import re

keyword = 'python'
class Job:
    def get_info(self):
        url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,' + keyword + ',2,' + '1' + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        headers = {
            'Host': 'search.51job.com',
            'Referer': 'https://search.51job.com/list/000000,000000,0000,00,9,99,python%25E5%25BC%2580%25E5%258F%2591,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        data = requests.get(url, headers=headers).content
        info = str(data.decode('gbk').encode('utf-8'), 'utf-8')
        pages = int(re.sub('共|页', '', re.search('共\d+页', info).group()))
        for page in range(2, pages):
            urls = 'https://search.51job.com/list/000000,000000,0000,00,9,99,' + keyword + ',2,' + str(page) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            data = requests.get(urls, headers=headers).content
            info = str(data.decode('gbk').encode('utf-8'), 'utf-8')
            for i, j, k, l, m in zip(re.findall('title=".*onmousedown', info),
                                     re.findall('title=.*?href="http.*?</a>', info), re.findall('t3.*?<', info)[1:],
                                     re.findall('t4.*?<', info)[1:], re.findall('t5.*?<', info)[1:]):
                name = re.sub('title=|"|\s|href.*', '', i)
                company = re.sub('title=|"|href=.*|</a>|\s', '', j)
                place = re.sub('t3">|<', '', k).split('-')[0]
                money = re.sub('t4">|<', '', l)
                moneys = (float(money[:-3].split('-')[0]) * 1000 + float(
                    money[:-3].split('-')[1]) * 1000) / 2 if '千/月' in money else (float(
                    money[:-3].split('-')[0]) * 10000 + float(money[:-3].split('-')[1]) * 10000) / 2 if '万/月' in money else \
                    float(money[:-3])*30 if '元/天' in money else 0
                date = re.sub('t5">|<', '', m)
                print(name, company, place, moneys, date)
                with open('job.txt', 'a+') as jb:
                    jb.write('职位名:'+name+' 公司名:' + company+' 工作地点:'+place+' 工资:'+str(moneys)+' 发布时间:'+date+'\n')

if __name__ == '__main__':
    job = Job()
    job.get_info()

