from keep_alive import keep_alive

keep_alive()
import datetime, requests, time, threading


replitUrl = "https://testlive.vinhquoc.repl.co"
webhook_url = "https://discord.com/api/webhooks/1151152168771006546/bvwW89q6DsZhnOhhrtwK3xxwDasF7266g9CQq2JvJU9o7XuF2Zu4xgDp_BCuCmlP7C6d"

def get_current_time():
    time = datetime.datetime.now()
    hour = time.strftime("%H")
    hour = str(int(hour) + 7)
    if int(hour) >= 24:
        if int(hour) == 24:
            hour = 0
        else:
            hour = str(int(hour) - 24)
    return hour + time.strftime(':%M:%S')
def to_discord(s):
    requests.post(webhook_url, data={"content": s})

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'viewport-width': '1366',
}
def run():
  r = requests.get(replitUrl, headers=headers).text
  r = requests.get("https://notificationvnedu.onrender.com/", headers=headers).text
  r = requests.get("https://testlive.onrender.com/", headers=headers).text
  to_discord(f"Send requests | {r} | " + get_current_time())


while True:
  try:
    threading.Thread(target=run).start()
    time.sleep(60)
  except Exception as e:
     to_discord(e)

    

