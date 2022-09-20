

from typing import Union
from typing import List
import shutil
# from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Form
from starlette.middleware.cors import CORSMiddleware


from keras.models import load_model
import keras
from tensorflow.keras.utils import load_img, img_to_array
from keras.preprocessing import image
import numpy as np
import time
import asyncio
from PIL import Image

# 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

img_width, img_height = 224, 224
getFormList = ['dew', 'fogsmog', 'frost', 'glaze', 'hail', 'lightning', 'rain', 'rainbow', 'rime',
'sandstorm', 'snow']
                # load the model we saved
model = load_model('best_model_kk.h5')
model.compile(loss='binary_crossentropy',
                            optimizer='rmsprop',
                            metrics=['accuracy'])

                # predicting images

@app.post("/uploadfile/")
async def create_upload_file(files: UploadFile):
    
    if not files:
        return {"message": "No upload file sent"}
    else:
        with open(files.filename, 'wb') as f:
                # fdst = open(f, 'w')
            shutil.copyfileobj(files.file, f)
                # dimensions of our images
                # print("hello1")
            img = load_img(files.filename, target_size=(img_width, img_height))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])
            classes = model.predict(images, batch_size=5)
            # print (classes5
            a = 0
            getFormListV =""
            for i in classes[0]:
                
                if i == 1:
                    print(a)
                    getFormListV= getFormList[a]
                a+=1

            return {"data":getFormListV}
                # def preprocess(img):
                    # img = cv.resize(img, (224, 224))
                    # img = np.array([img]).astype('float64')/255.0

                # return {"data": predictions}
        



# @app.post("/test/")
# async def create_upload_file():
#     print("test1")
#     if True:
#         return {"message": "No upload file sent"}
#     else:
#         return {"filename": "file"}




























# def upload(files: List[UploadFile] = File(...)):
#     for file in files:
#         try:
#             with open(file.filename, 'wb') as f:
#                 # fdst = open(f, 'w')
#                 shutil.copyfileobj(file.file, f)
#         except Exception:
#             return {"message": "There was an error uploading the file(s)"}
#         finally:
#             file.file.close()

#     return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}  
# test.py





# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
