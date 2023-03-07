import base64
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from app.config import http_url, key, secret, filepath, attributes
import requests
import cv2
from app.models import connect_db, Image


router = APIRouter()


def convertToGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

@router.post('/image')
def post_image(database=Depends(connect_db)):
    fr = open(filepath, 'rb')
    img64 = base64.b64encode(fr.read())
    payload = {
        'api_key': key,
        'api_secret': secret,
        'image_base64': img64,
        'return_attributes': attributes
    }
    fr.close()

    json_resp = requests.post(http_url,
                              data=payload
                              )
    if not json_resp:
        raise Exception('Not found data')

    image_id = json_resp.json()['image_id']
    request_id = json_resp.json()['request_id']
    faces = json_resp.json()['faces']
    add_data = Image(request_id=request_id, image_id=image_id, faces=faces)
    database.add(add_data)

    database.commit()
    return {"id": json_resp.json()['request_id']}


@router.get('/image/<int:id>')
def get_image(id: int, color: str, database=Depends(connect_db)):
    try:
        image_from_db = database.query(Image.faces).filter(Image.id == id).one()
    except NoResultFound:
        return HTTPException(
            status_code=404,
            detail={"message": f"Лицо с id={id} не обнаружено"}
        )
    green = ["green", "g", "GREEN"]
    blue = ["blue", "b", "BLUE"]
    red = ["red", "r", "RED"]
    if color in green:
        int_color = (0, 255, 0)
    elif color in blue:
        int_color = (255, 0, 0)
    elif color in red:
        int_color = (0, 0, 255)
    else:
        int_color = (255, 0, 0)

    test_image = cv2.imread(filepath)

    for json_data in image_from_db:
        for i in json_data:
            x, y, w, h = i['face_rectangle'].values()
            cv2.rectangle(test_image, (x, y), (x + w, y + h), int_color, 2)


    res = cv2.imshow("face_detection", test_image)

    return res


@router.put('/image/<int:id>')
def put_image(id: int, database=Depends(connect_db)):
    try:
        image_from_db = database.query(Image.faces).filter(Image.id == id).one()

    except NoResultFound:

        return HTTPException(

            status_code=404,

            detail={"message": f"Лицо с id = {id} не обнаружено"}

        )

    test_image = cv2.imread(filepath)

    gray_image = convertToGray(test_image)

    for json_data in image_from_db:
        for i in json_data:
            x, y, w, h = i['face_rectangle'].values()
            cv2.rectangle(gray_image, (x, y), (x + w, y + h), (255, 255, 255), 4)


    res = cv2.imshow("face detected", test_image)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return res


@router.delete('/image/<int:id>')
def delete_image(id: int, database=Depends(connect_db)):
    try:
        face_id = database.query(Image).filter(Image.id == id).one()
    except NoResultFound:
        return HTTPException(
            status_code=404,
            detail={"message": f"Лицо с id = {id} не обнаружено"}
        )

    face = face_id
    database.delete(face)
    database.commit()
    return {"status": "OK"}
