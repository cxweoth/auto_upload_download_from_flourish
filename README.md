# auto_upload_download_from_flourish
安裝 python Lib: requests, selenium
主要 code: upload_flourish_download_web

使用前請先至 https://flourish.studio/ 申請帳號密碼，並開啟一個 bar chart race 專案
這包 code 只適用於 bar chart race 喔!

如何使用這包 code 呢?
請用包裡的 sample_code.py 來做開始吧!

web_generator = FlourishWebGenerator()
web_generator.create_driver(account="your_account", password="your_password", full_screen=False)
current_url = web_generator.upload_to_flourish(flourish_id='your_flourish_id',
                                               upload_file_name='your_upload_file_name',
                                               data_beg_alphabet='data_beg_column',
                                               data_end_alphabet='data_end_column')
web_generator.download_web(current_url, 'web_name')
web_generator.open_local_web('web_name')
time.sleep(5)
web_generator.close()
