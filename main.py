from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os

def setup_driver():
    print(f"[{datetime.now()}] 开始初始化浏览器...")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    print(f"[{datetime.now()}] 配置 Chrome 选项完成")
    
    print(f"[{datetime.now()}] 正在启动 Chrome...")
    driver = webdriver.Chrome(options=options)
    
    print(f"[{datetime.now()}] 正在访问网站...")
    driver.get('https://app.follow.is/')
    
    print(f"[{datetime.now()}] 正在设置 cookie...")
    # 从环境变量获取 cookie
    cookie_string = os.environ.get('COOKIE_STRING')
    if not cookie_string:
        raise Exception("Cookie 未设置！请在 GitHub Secrets 中设置 COOKIE_STRING")
    
    driver.execute_script(f"document.cookie = '{cookie_string}'")
    
    print(f"[{datetime.now()}] 浏览器初始化完成")
    return driver

def main():
    try:
        driver = setup_driver()
        
        print(f"[{datetime.now()}] 等待页面加载...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print(f"[{datetime.now()}] 页面加载完成")
        
        print(f"[{datetime.now()}] 正在获取页面焦点...")
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()
        print(f"[{datetime.now()}] 已获取页面焦点")
        
        count = 1
        print(f"[{datetime.now()}] 开始执行自动滚动...")
        while True:
            print(f"[{datetime.now()}] 第 {count} 次按下向下键")
            body.send_keys(Keys.DOWN)
            print(f"[{datetime.now()}] 等待 120 秒后执行下一次操作...")
            time.sleep(120)
            count += 1
            
    except Exception as e:
        print(f"[{datetime.now()}] 发生错误: {str(e)}")
        
    finally:
        print(f"[{datetime.now()}] 正在关闭浏览器...")
        driver.quit()
        print(f"[{datetime.now()}] 程序执行完毕")

if __name__ == "__main__":
    print(f"[{datetime.now()}] 程序开始运行")
    main()
