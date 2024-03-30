import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    # 发送HTTP GET请求获取网页内容
    response = requests.get(url)
    
    # 检查响应状态码
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到所有的文字内容并输出
        text_content = soup.get_text()
        print(text_content)
    else:
        print("请求失败，状态码：", response.status_code)

if __name__ == "__main__":
    target_url = input("请输入要爬取的网站URL：")
    crawl_website(target_url)
