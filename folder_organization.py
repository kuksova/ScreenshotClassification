import os
import shutil
import json

def create_folder(arr_id_images, keyword, path):

    #name_folder = os.path.split(path_images)[1]
    # moving images with the keyword
    if arr_id_images:

        path_new = os.path.join(path, keyword)
        exis = os.path.exists(path_new)
        if not exis:
            os.mkdir(path_new)
            print("Created a new album if it doesn't exist already ", path_new)
        else:
            print("There is already an album with this keyword - ", keyword)

        #saveData(arr_id_images, foundImgs)

        # move images
        path_images = os.path.join(path, 'images/')
        for f in arr_id_images:
            file_name = os.path.join(path_images + f)
            if not os.path.exists(file_name):
                return
            shutil.move(path_images + f, path_new +'/'+ f)

def has_keys(dict1, keys_list):
    return all(key in dict1 for key in keys_list)

def copy_dict_pairs(orig_dict, keys_list):
    remain_dict ={}
    for key in keys_list:
        if key in orig_dict:
            remain_dict[key] = orig_dict[key]
    return remain_dict

def process_remained(path, fl = True):
    # Create a json file for remained images from input_images.json,
    # then delete the input_images.json

    path_remained = os.path.join(path,'remained/')
    exis = os.path.exists(path_remained)
    if not exis:
        os.mkdir(path_remained)

    # Checking now many images was remained
    path_images = os.path.join(path, 'images/')
    img_names = sorted(os.listdir(path_images))
    print(len(img_names))

    # Checking now many images was originally
    with open("input_images.json", "r", encoding='utf-8') as read_file:
        # print("Reading JSON serialized Unicode data from file")
        sampleData = json.load(read_file)

    if len(sampleData) != len(img_names):

        remain_dict = copy_dict_pairs(sampleData, img_names)

        with open("remained_images.json", "w", encoding='utf-8') as outfile:
            json.dump(remain_dict, outfile, ensure_ascii=False)
        print("Json was created.")
    else:
        os.rename('input_images.json', "remained_images.json")
        #shutil.move('remained_images.json', path_remained + 'remained_images.json')

    if fl:
        # move images
        for f in img_names:
            file_name = os.path.join(path_images + f)
            #if not os.path.exists(file_name):
            #    return

            shutil.move(path_images + f, path_remained + f)
        # remove original json file
        os.remove("input_images.json")




