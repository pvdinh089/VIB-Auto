from zalo.sdk.app import *

app_id = 2344987292493285787
secret_key = "Fpg0n9nlVd6st0IlYy35"
callback_url = "https://www.vib.com.vn/wps/portal/vn/ca-nhan"
access_token = "LzrSEpfwgL9KsrmnEN6ZKbZNM3isQkORMCr89t8EoInX-aSoSHwy6a76DIT-0vSQOwKq1bnNeILVanWkOZ2QDalk5nrRKEiSGVDZ8I4an20l-tqI427MT7g7TrPnG_9cRQ5hOGPtwaOjdHDYH6otLMUB5aCAMhbc8wOCM3HaYMiufnPiBtsJ44_V43Pw3xaoPze_Lse8k6u4z0DN90xxJ4JAHtTgD_XjKjG2SYPqkd0vYY8J1bkW5YoR2XC7NVyZReLI9mHyq1GyZ6e_NNIG0JEp3oDfMPFCKJrWeba"

zalo_info = ZaloAppInfo(app_id, secret_key, callback_url)
vib_autoapp = Zalo3rdAppClient(zalo_info)
print(vib_autoapp)

login_url = Zalo3rdAppClient.get_login_url(vib_autoapp)
print(login_url)

profile = vib_autoapp.get('/me', access_token,
                          {'fields': 'id, name, birthday, gender, picture'})
# print(type(profile))
# id = profile['id']
# print("My Id is:", id)
# Lấy danh sách khách hàng đang sử dụng ứng dụng
friends = vib_autoapp.get('/me/friends', access_token, {
    'offset': 0,
    'limit': 50,
    'fields': 'id, gender'
})
print(friends)
# Lấy danh sách khách hàng chưa sử dụng ứng dụng và có thể gửi tin nhắn
invitable_friends = vib_autoapp.get(
    '/me/invitable_friends', access_token, {
        'offset': '0',
        'limit': '10',
        'fields': 'id, name, birthday, gender, picture'
    })
"""
# Mời bạn bè sử dụng ứng dụng
send_app_request = vib_autoapp.post('/apprequests', access_token, {
    'message': 'Để được chăm sóc tốt hơn, vui lòng sử dụng App VIBAuto',
    'to': 'pvdinh089'
})
print(send_app_request)

"""
# print(send_app_request)
# gửi tin nhắn đến bạn bè
send_message = vib_autoapp.post(
    '/me/message', access_token, {
        'message':
        'Đây là tin nhắn tự động từ hệ thống quản lý thông tin cấp cà vẹt của VIB Trần Hưng Đạo',
        'to': '1727712766203459523, 6128912743477133623',
        'link': 'https://vib.com.vn'
    })
# print(send_message)
# print(send_message)
