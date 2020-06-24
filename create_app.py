import zalo.sdk.app
app_id=2344987292493285787
secret_key="Fpg0n9nlVd6st0IlYy35"
callback_url="https://www.vib.com.vn/wps/portal/vn/ca-nhan"
zalo_info = zalo.sdk.app.ZaloAppInfo(app_id, secret_key, callback_url)
print(zalo_info)
