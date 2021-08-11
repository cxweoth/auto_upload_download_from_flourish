# ---- This repository is end of life. Please do not use it. ----

# auto_upload_download_from_flourish
安裝 python Lib: requests, selenium
主要 code: upload_flourish_download_web

使用前請先至 https://flourish.studio/ 申請帳號密碼，並開啟一個 bar chart race 專案
這包 code 只適用於 bar chart race 喔!

如何使用這包 code 呢?
請用包裡的 sample_code.py 來做開始吧!

在 create_driver 這 method 你需要輸入 

- your_account: 你的 flourish 帳號
- your_password: 你的 flourish password
- full_screen: 開啟網頁是使用全螢幕還是小視窗 (預設 False)

web_generator.create_driver(account="your_account", password="your_password", full_screen=False)

在 upload_to_flourish 這 method 你需要輸入 

- your_flourish_id: 專案開啟後的 url 裏頭的 id 編號，如 https://app.flourish.studio/visualisation/2051238/edit 裡就是 2051238
- your_upload_file_name: 要上傳的檔案名稱 (將你要上傳到 flourish 的檔案放到包裡的 file_upload 資料夾，檔案格式為 json 詳細格式放於備註)
- data_beg_column: 上傳 flourish 的 data 起始欄位
- data_end_column: 上傳 flourish 的 data 終點欄位

current_url = web_generator.upload_to_flourish(flourish_id='your_flourish_id',
                                               upload_file_name='your_upload_file_name',
                                               data_beg_alphabet='data_beg_column',
                                               data_end_alphabet='data_end_column')
                                               
在 download_web 這 method 你需要輸入

- current_url: 從 upload_to_flourish 收到的 url
- web_name: 你下載下來後取的 html 檔名

web_generator.download_web(current_url, 'web_name')

在 open_local_web 這 method 你需要輸入

- web_name: 你下載下來後取的 html 檔名

web_generator.open_local_web('web_name')

close 這個 method 會關閉網頁

web_generator.close()

* 備註

flourish json format: [{'name':'test1', '1911':2, '1912':3}, {'name':'test2', '1911':2, '1912':3}, {'name':'test3', '1911':2, '1912':3}]

list 裏頭包 dictionary， flourish 的一列資料為 dictionary 轉換而來，像上面就有三筆資料~
