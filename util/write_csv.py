import csv
from os.path import dirname, abspath, join


# content_dict = {0: [], 1:[],...}
def write_csv(ROOT_PATH, target_file, content_dict):
  with open(join(ROOT_PATH, target_file), 'w', newline='') as csvFile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvFile)

    # 1.直接寫出-標題
    for content_id in content_dict:
      content = content_dict[content_id]
      writer.writerow(content)

# if __name__ == '__main__':
#   ROOT_PATH = dirname(abspath(__file__))
#   write_csv(ROOT_PATH, 'test.csv', {0: ['yes'], 1: [123, 134]})
# ROOT_PATH = "D:\CXWEO\Agorithm\src\Automatic_Flourish_Video"
#
# write_csv(ROOT_PATH, 'for_autoit_csv/file_path.csv',
#           {0: ["D:\CXWEO\Agorithm\src\Automatic_Flourish_Video\processing_data\\nba\\nba_champion_yearly_sum.json"]})
