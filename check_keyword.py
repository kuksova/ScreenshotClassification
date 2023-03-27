import json

def get_key_by_value(dict, word):
  key_list = []
  for key, value in dict.items():
    for item in value:
      if word.lower() in item.lower():
        key_list.append(key)
        break
  return key_list

def processing_by_keyword(word):
  # train_screens.json
  with open("input_images.json", "r", encoding='utf-8') as read_file:
      #print("Reading JSON serialized Unicode data from file")
      sampleData = json.load(read_file)

  name_imgs = get_key_by_value(sampleData, word)
  return name_imgs