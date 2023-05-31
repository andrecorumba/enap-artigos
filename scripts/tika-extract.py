# Importa as bibliotecas
from tika import parser
import os
import json
from joblib import Parallel, delayed

JSON_FOLDER = "D:\data\data-enap-artigos\json-enap-artigos"
FILES_FOLDER = "D:\data\data-enap-artigos\pdf-enap-artigos"

# Servidor : 'http://localhost:9998/'
def worker(file_name):
    
    file_path = os.path.join(FILES_FOLDER, file_name)
    
    parsed = parser.from_file(file_path, 
                              serverEndpoint='http://localhost:9998/', 
                              requestOptions={'timeout': 900})
    
    text = parsed.get('content') 
    info = parsed.get('metadata')
    dic = {"file" : file_path,
           "text" : text.strip() if parsed['content'] else '',
           "info" : info}
    
    # Salva em json
    json_file_path = os.path.join(JSON_FOLDER, os.path.splitext(file_name)[0]) + ".json"
    save_json(dic, json_file_path)
    
# Salva o dicionário em um arquivo json
def save_json(dic, json_file_path):
    with open(json_file_path, "w") as f:
        json.dump(dic, f)

# def save_log(file_path, message):
#     log_file_path = 'log/log_tika_HTML.txt'
#     with open(log_file_path, 'a') as file:
#         file.write(f"{message} : Arquivo: {file_path}, {datetime.datetime.now()}\n")


if __name__ == '__main__':
    # Extracao pasta de relatorios
    Parallel(prefer='threads', n_jobs=2, verbose=1000)(delayed(worker)(file_name) for file_name in os.listdir(FILES_FOLDER))