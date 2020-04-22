from .upload_flourish_download_web import FlourishWebGenerator
import time
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
