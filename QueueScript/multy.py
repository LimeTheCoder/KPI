import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pickle

def load(file_name):
    with open(file_name, 'rb') as f:
        coords = pickle.load(f)
    return coords


def save(file_name, obj):
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)


'''
Names to insert in unicode
'''
names_to_insert = [u'\u0421\u0430\u0445\u0430\u0440\u0447\u0443\u043a', u'\u0420\u0430\u0442\u043e\u0448\u043d\u044e\u043a',
                   u'\u041b\u0438\u0441\u043e\u0433\u043e\u0440', u'\u041a\u043e\u0436\u043e\u043a\u0430\u0440\u044c']

'''
Titles of tables in unicode
'''
ws_titles = [u'\u041e\u0421', u'\u041a\u041b', u'\u0411\u0414', u'\u041e\u041e\u041f',
            u'\u0415\u043c\u043f\u0456\u0440\u0438\u0447\u043d\u0456 \u043c\u0435\u0442\u043e\u0434\u0438']

'''
Path to columns index
'''
file_path = 'D:\Projects\DocQueueScript\data.txt'
curr_coords = load(file_path)

'''
Document key(from url)
'''
key_to_doc = '176s_vkjtre_WwTR1CWg7gs40WRDViECGQHZHnTMLdhY'

scope = ['https://spreadsheets.google.com/feeds', 'https://docs.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('D:\Projects\DocQueueScript\\test1.json', scope)
gc = gspread.authorize(credentials)

sht = gc.open_by_key(key_to_doc)

idx = 0

for title, coord in zip(ws_titles, curr_coords):
    ws = sht.worksheet(title)
    val = ws.cell(2, coord).value
    val_second = ws.cell(3, coord).value

    name_idx = 0
    move_to_next = False

    if val or val_second:
        for i in range(1, 20):
            val = ws.cell(2 + i, coord).value
            if not val:
                ws.update_cell(2 + i, coord, names_to_insert[name_idx])
                name_idx += 1
                move_to_next = True

                if name_idx == len(names_to_insert):
                    break
                    
        if move_to_next == True:
            curr_coords[idx] += 1
    idx += 1

save(file_path, curr_coords)