from pathlib import Path
import sys
import shutil
import os

MAIN_DIC = {"images": ['.jpeg', '.png', '.jpg', '.svg'], "video": ['.avi', '.mp4', '.mov', '.mkv', '.eml'], "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsm', '.pptx', '.xlsx', '.py'],
"audio": ['.mp3', '.ogg', '.wav', '.amr'], "archives": ['.zip', '.gz', '.tar']}

CYRILLIC = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'є', 'і', 'ї', 'ґ']
TRANSLATION=["a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "c", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"]
TRANS = {}
for c, l in zip(CYRILLIC, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def path_exist():
    
    if len(sys.argv)<2:
        print("You didn\'t enter path to folder")
        exit()
    
    path_ex = Path(sys.argv[1])
    
    if not (path_ex.exists() and path_ex.is_dir()):
        print("Bad path")
        exit()

def moving(user_path, DIC=MAIN_DIC):
    
    global base_path

    path_0 = Path (base_path)
    path_1 = Path (user_path)

    for element in path_1.iterdir():
        if element.suffix in DIC["archives"]:
            shutil.unpack_archive(element, path_0.joinpath("archives", element.stem))
            element.unlink()
            print (f"Moving file {element} to folder {key}")
        elif element.suffix in DIC["images"]:
            element.rename(path_0.joinpath("images", element.name))
            print (f"Moving file {element} to folder 'images'")
        elif element.suffix in DIC["video"]:
            element.rename(path_0.joinpath("video", element.name))
            print (f"Moving file {element} to folder 'video'")
        elif element.suffix in DIC["documents"]:
            element.rename(path_0.joinpath("documents", element.name))
            print (f"Moving file {element} to folder 'documents'")
        elif element.suffix in DIC["audio"]:
            element.rename(path_0.joinpath("audio", element.name))
            print (f"Moving file {element} to folder 'audio'")
        elif element.is_dir() and (element.name not in ["archives", "images", "video", "documents", "audio"]):
            moving(element)

def del_empty_folders(user_path):
    
    for element in os.listdir(user_path):
        a = os.path.join(user_path, element)
        if os.path.isdir(a):
            del_empty_folders(a)
            if not os.listdir(a):
                os.rmdir(a)
                


def translate(name):
    new_name = ""
    for b in range(len(name)):
        if (name[b] in CYRILLIC) or (name[b].lower() in CYRILLIC):
            new_name += name[b].translate(TRANS)
        elif (name[b] in TRANSLATION) or (name[b].lower() in TRANSLATION):
            new_name += name[b]
        else:
            new_name += "_"    
        
    return (new_name)


def rename(user_path):
    i="d"
        
    for path in Path(user_path).iterdir():
    
        try:   
            if path.is_file():
                new_name = translate(path.stem)+path.suffix
                path.rename(Path(path.parent, new_name))
        except FileExistsError:
                new_name = i+ translate(path.stem)+path.suffix
                i=i+"d"
                path.rename(Path(path.parent, new_name))
         
        if path.is_dir():
            rename (path)
            new_name = translate(path.name)
            path.rename(Path(path.parent, new_name))
        
def main():

    path_exist()

    base_path = sys.argv[1]
    path_ex = Path (sys.argv[1]) 
    
    for key in MAIN_DIC:
        path_ex.joinpath(key).mkdir(exist_ok=True)

    moving (path_ex)
    
    del_empty_folders(path_ex)

    rename(path_ex)


if __name__ == "__main__":
    
    main()
    exit()
   

        

