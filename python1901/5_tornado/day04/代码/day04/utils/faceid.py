from aip import AipFace

APP_ID = '16107069'
API_KEY = 'wLrGIlDsYIwPO3S1wcKw8Rtv'
SECRET_KEY = '9xXBx4p6WB4UyCKPXMY2bCY53XTWvzUh'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def register_face_user(image, user_id, image_type='BASE64', group_id='user'):
    # 人脸注册
    response = client.addUser(image, image_type, group_id, user_id)
    return False if response['error_code'] else True
