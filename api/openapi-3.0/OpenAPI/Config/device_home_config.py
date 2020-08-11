import time, os, datetime
from OpenAPI.Config.api_config import *

path = os.path.split(os.path.realpath(__file__))[0]
param_openapi_path = os.path.join(path + '/../RunCase/')


# 3.0 线下(默认)  18566666668
home_id = '5c8107545cdc782eb5c771c0'        # OpenAPI
home_id_2 = '5d88917eab38ec5bafea244e'       # OpenAPI2
room_pub = '5c8107545cdc782eb5c771c0'
room_1001 = '5c8107541254a52eaf207exx'
room_1001_uid = '5c8107541254a52eaf207edd'
room_1002 = '5c8107541254a52eaf207ey1'
room_1003 = '5c8107541254a52eaf207edf'
elemeter_A1_uuid = 'f7d45c26288e809caa01aab349b28b68'
elemeter_A3_uuid = '43edb9bf9277c474eb670829105a017e'
elemeter_A4_uuid = 'c66c467a97c9dbb49e343b2fef1f534b'
# elemeter_A4_uuid = '8d0b8ed82c0b7ce981ac385510548b2b'
elecollector_uuid = '2ded63bfad9b0472d2dcf2e209cbb74a'
lock_uuid = 'e29fe4fbebef8f7e62f5859203536ba7'
lock_uuid_noroute = 'e29fe4fbebef8f7e62f5859203536ba7'
gateway_uuid = 'e9f94c4b9902ae350b554e890718ad55'
water_gw_uuid = '5ea684c165ff4da291052f68a79f51a4'
water_cold_uuid = '2a5b62c8a714ce38e89aea4abd440687'
water_hot_uuid = 'c19b0342654b1acac167ba5110dc530b'
water_gw_sn = '000001523678'
water_cold_sn = '00000170474152'
water_hot_sn = '00000171457868'
elemeter_A4_sn = '180725050733'
# elemeter_A4_sn = '190313130019'
lock_sn = 'lkjl0012180400810936'
lock_sn_noroute = 'lkjl0007180600004000'
install_ticket = 'ISLK1903081780419'
fix_ticket = 'RPMR1903081723306'
phone_num = '18566666668'

# 3.0 线上 18566666666
home_id_30_on = '5c19b7b8213993244a77efb8'        # OpenAPI
home_id_2_30_on = '5c19b824213993244a77efb9'       # OpenAPI2
room_pub_30_on = '5c19b7b8213993244a77efb8'
room_1001_uid_30_on = '5cece564bd8989641c20b4d8'
room_1001_30_on = '5d084aa735c2e14380cc4375'
room_1002_30_on = '5c19b7b8dd10a428f662a16e'
room_1003_30_on = '5c19b7b8dd10a428f662a16d'
elemeter_A1_uuid_30_on = '889e8f9ef2faff9c0ea6c95bee52e30c'
elemeter_A3_uuid_30_on = '3d1e06cd04c377eaf7421e579e0a99ae'
elemeter_A4_uuid_30_on = '0077f226c34227f23edf3b8fc7a3aa02'
elecollector_uuid_30_on = 'd64f62bdc85eace78726d0035265c017'
lock_uuid_30_on = 'b1085351fdbb03c87e388454f951dd6b'
lock_uuid_noroute_30_on = 'b1085351fdbb03c87e388454f951dd6b'
gateway_uuid_30_on = 'd51544228b14011727b1be67ddf67748'
water_gw_uuid_30_on = 'fa9a881b4921cb8e148aa5488ca8c398'
water_cold_uuid_30_on = '19e01a7faacd5213813b78b98c914cd5'
water_hot_uuid_30_on = 'c19b0342654b1acac167ba5110dc530b'
water_gw_sn_30_on = '000001523699'
water_cold_sn_30_on = '00000180501095'
water_hot_sn_30_on = '00000171457868'
elemeter_A4_sn_30_on = '180822030608'
lock_sn_30_on = 'lkjl0007181011682063'
lock_sn_noroute_30_on = 'lkjl0019180500932243'
install_ticket_30_on = 'ISLK1901231054928'
fix_ticket_30_on = 'RPMR1901231053950'
phone_num_30_on = '18566666666'

# 2.0 线下   18566666666
home_id_20_off = '5c19e7b67eaede1fb2c4053b'        # OpenAPI
home_id_2_20_off = '5c19e7e07eaede1fb2c40544'       # OpenAPI2
room_pub_20_off = '5c19e7b67eaede1fb2c4053b'
room_1001_uid_20_off = '5c19e7b77eaede1fb2c4053e'
room_1001_20_off = '5c19e7b77eaede1fb2c4053e'
room_1002_20_off = '5c19e7b77eaede1fb2c4053f'
room_1003_20_off = '5c19e7b77eaede1fb2c40540'
elemeter_A1_uuid_20_off = '8a3466769176cc00d26830e5e22766e6'
elemeter_A3_uuid_20_off = 'd0210890b772ff1eb4dfab5124c64423'
elemeter_A4_uuid_20_off = '322918f4654f22c38e4d67f7d0db7fc9'
elecollector_uuid_20_off = '0f3f134e405492561bac8d376e4f8db2'
lock_uuid_20_off = 'e29fe4fbebef8f7e62f5859203536ba7'
lock_uuid_noroute_20_off = 'e2bb9fd508f2e9a7b1847fb48a93b149'
gateway_uuid_20_off = '584363eaf434b7edd705d6c13e50c82e'
water_gw_uuid_20_off = '03cd395e10e1f2f9ff3f5209674d4eef'
water_cold_uuid_20_off = '5a39d93ec0ef01e7a42559475592570a'
water_hot_uuid_20_off = '6e3f40d56cea72cee00fa444fe004dd9'
water_gw_sn_20_off = '000001523684'
water_cold_sn_20_off = '00000180505246'
water_hot_sn_20_off = '00000171457923'
elemeter_A4_sn_20_off = '180411051423'
lock_sn_20_off = 'lkjl0012180400810936'
lock_sn_noroute_20_off = 'lkjl0007180500004382'
install_ticket_20_off = 'ISCN181227151238840'
fix_ticket_20_off = 'RPMR181227151783877'
phone_num_20_off = '18566666666'

# 2.0 线上  18566666666
home_id_20_on = '5c19b5f6f365974d9d72c806'        # OpenAPI
home_id_2_20_on = '5c19b6348e674b24486279b7'       # OpenAPI2
room_pub_20_on = '5c19b5f6f365974d9d72c806'
room_1001_uid_20_on = '5c19b5f6f365974d9d72c809'
room_1001_20_on = '5c19b5f6f365974d9d72c809'
room_1002_20_on = '5c19b5f6f365974d9d72c80a'
room_1003_20_on = '5c19b5f6f365974d9d72c80b'
elemeter_A1_uuid_20_on = '889e8f9ef2faff9c0ea6c95bee52e30c'
elemeter_A3_uuid_20_on = '3d1e06cd04c377eaf7421e579e0a99ae'
elemeter_A4_uuid_20_on = '0077f226c34227f23edf3b8fc7a3aa02'
elecollector_uuid_20_on = 'd64f62bdc85eace78726d0035265c017'
lock_uuid_20_on = 'b1085351fdbb03c87e388454f951dd6b'
lock_uuid_noroute_20_on = '2ca2cf08e8a20a5bc6394bd943cd73a0'
gateway_uuid_20_on = 'd51544228b14011727b1be67ddf67748'
water_gw_uuid_20_on = '000001523669'
water_cold_uuid_20_on = '00000180501263'
water_hot_uuid_20_on = '00000181501439'
water_gw_sn_20_on = '000001523684'
water_cold_sn_20_on = '00000180505246'
water_hot_sn_20_on = '00000171457923'
elemeter_A4_sn_20_on = '170817050050'
lock_sn_20_on = 'lkjl0012180400810936'
lock_sn_noroute_20_on = 'lkjl0019180500932243'
install_ticket_20_on = 'ISCN1809262172362'
fix_ticket_20_on = 'RPMR1809251503731'
phone_num_20_on = '18566666666'

# xx账户  线下yangs 11066660028
home_id_xx = '5c638b18ade0205e0e3afe01'        # OpenAPI
home_id_2_xx = '5b9a27c670458f0534207218'       # OpenAPI2
room_pub_xx = '5c638b18ade0205e0e3afe01'
room_1001_uid_xx = '5b9610aab859bc23b58ffcc9'
room_1001_xx = '5c638b180266560249ff5857'
room_1002_xx = '5ce3babe7684cf01ea7f37e6'
room_1003_xx = '5ccf9831650a524a7965b24f'
elemeter_A1_uuid_xx = '6762441a57f9b5a1971aa4d632c66e3d'
elemeter_A3_uuid_xx = 'dc7de1f936465f860531578cf25d982e'
elemeter_A4_uuid_xx = '79bfd426439c22fb7fba471b673652b3'
elecollector_uuid_xx = '41d92f456748c61500aba3e910f9a296'
lock_uuid_xx = '6f962284ef2781c7f3cb2b9d45aae087'
lock_uuid_noroute_xx = '2ca2cf08e8a20a5bc6394bd943cd73a0'
gateway_uuid_xx = '40759d4b37b4a7e194795b64a15873c6'
water_gw_uuid_xx = '000001523669'
water_cold_uuid_xx = '00000180501263'
water_hot_uuid_xx = '00000181501439'
water_gw_sn_xx = '000001523684'
water_cold_sn_xx = '00000180505246'
water_hot_sn_xx = '00000171457923'
elemeter_A4_sn_xx = '190313130013'
lock_sn_xx = 'lkjl0023190532767376'
lock_sn_noroute_xx = 'lkjl0019180500932243'
phone_num_xx = '18566260535'
install_ticket_xx = 'ISCN1809262172362'
fix_ticket_xx = 'RPMR1809251503731'

# xx账户  线上蘑菇迁移
# home_id_xx = '5bf22a8a80269a1504a7c700'        # OpenAPI
# home_id_2_xx = '5b9a27c670458f0534207218'       # OpenAPI2
# room_pub_xx = '5b9610aab859bc23b58ffcc6'
# room_1001_xx = '5b9610aab859bc23b58ffcc9'
# room_1002_xx = '5b9610aab859bc23b58ffcca'
# room_1003_xx = '5b9610aab859bc23b58ffccb'
# elemeter_A1_uuid_xx = '889e8f9ef2faff9c0ea6c95bee52e30c'
# elemeter_A3_uuid_xx = '3d1e06cd04c377eaf7421e579e0a99ae'
# elemeter_A4_uuid_xx = '0077f226c34227f23edf3b8fc7a3aa02'
# elecollector_uuid_xx = 'd64f62bdc85eace78726d0035265c017'
# lock_uuid_xx = 'b1085351fdbb03c87e388454f951dd6b'
# gateway_uuid_xx = 'd51544228b14011727b1be67ddf67748'
# water_gw_uuid_xx = '000001523669'
# water_cold_uuid_xx = '00000180501263'
# water_hot_uuid_xx = '00000181501439'
# elemeter_A4_sn_xx = '170817050050'
# install_ticket_xx = 'ISCN1809262172362'
# fix_ticket_xx = 'RPMR1809251503731'
# yaos 线上迁移商户
# home_id_xx = '5b7a8b6ed1251322316f53ea'        # OpenAPI
# home_id_2_xx = '5bbef17de06a7349e581c6b1'       # OpenAPI2
# room_pub_xx = '5b9610aab859bc23b58ffcc6'
# room_1001_xx = '5b7a8b6ed1251322316f53ee'
# room_1002_xx = '5c13551fd923cb2da0dd9f22'
# room_1003_xx = '5c13551fd923cb2da0dd9f23'
# elemeter_A1_uuid_xx = '889e8f9ef2faff9c0ea6c95bee52e30c'
# elemeter_A3_uuid_xx = '3d1e06cd04c377eaf7421e579e0a99ae'
# elemeter_A4_uuid_xx = 'da7579d09b6120657b2ef61006a63537'
# elecollector_uuid_xx = 'd64f62bdc85eace78726d0035265c017'
# lock_uuid_xx = 'b1085351fdbb03c87e388454f951dd6b'
# gateway_uuid_xx = 'd51544228b14011727b1be67ddf67748'
# water_gw_uuid_xx = '000001523669'
# water_cold_uuid_xx = '00000180501263'
# water_hot_uuid_xx = '00000181501439'
# water_gw_sn_xx = '000001523684'
# water_cold_sn_xx = '00000180505246'
# water_hot_sn_xx = '00000171457923'
# elemeter_A4_sn_xx = '170817050050'
# install_ticket_xx = 'ISCN1809262172362'
# fix_ticket_xx = 'RPMR1809251503731'
# 2.0 线上 liuy
# home_id_xx = '5c0772113e7b11062cb4d701'        # liuyue_apartment_a02
# home_id_2_xx = '5bbef17de06a7349e581c6b1'       # OpenAPI2
# room_pub_xx = '5c0772113e7b11062cb4d701'
# room_1001_xx = '5c077211aa3d7d503f005b7c'
# room_1002_xx = '5bcd402c63468b391f0480ad'
# room_1003_xx = '5c13551fd923cb2da0dd9f23'
# elemeter_A1_uuid_xx = '889e8f9ef2faff9c0ea6c95bee52e30c'
# elemeter_A3_uuid_xx = '3d1e06cd04c377eaf7421e579e0a99ae'
# elemeter_A4_uuid_xx = 'c009c055ef1b050f961b0dcad1bf809d'
# elecollector_uuid_xx = 'd64f62bdc85eace78726d0035265c017'
# lock_uuid_xx = '4818be22ad2ddc0b1ceec7fb00f46aeb'
# gateway_uuid_xx = 'd51544228b14011727b1be67ddf67748'
# water_gw_uuid_xx = '000001523684'
# water_cold_uuid_xx = '00000180505246'
# water_hot_uuid_xx = '00000171457923'
# water_gw_sn_xx = '000001523684'
# water_cold_sn_xx = '00000180505246'
# water_hot_sn_xx = '00000171457923'
# elemeter_A4_sn_xx = '160810001550 '
# install_ticket_xx = 'ISCN1809262172362'
# fix_ticket_xx = 'RPMR1809251503731'

elemeter_wrong_uuid = 'c66c467a97c9dbb49e343b2fef1f534b'
lock_wrong_uuid = ''
gateway_wrong_uuid = '2d5173c12a1ac889bd8daea7302bf148'
elecollector_wrong_uuid = ''

# 通用配置
# encrypted加密后的密码（每次添加需要根据token重新生成）
encrypted_password_123456 = 'qEjqqBnRitiAAqT+pr+p3A=='
# 5天前 ms
before_ms = int(time.time()) * 1000 - 3600000 * 24 * 5
# 12h前 ms
# before_ms = int(time.time()) * 1000 - 3600000 * 12
# 当前时间 ms
now_ms = int(time.time()) * 1000
# 5天后 ms
after_ms = int(time.time()) * 1000 + 3600000 * 24 * 5
# 12h后 ms
# after_ms = int(time.time()) * 1000 + 3600000 * 12
# 5天前 s
before_s = int(time.time()) - 3600 * 24 * 5
# 12h前 s
# before_s = int(time.time()) - 3600 * 12
# 当前时间 s
now_s = int(time.time())
# 5天后 s
after_s = int(time.time()) + 3600 * 24 * 5
# 12h后 s
# after_s = int(time.time()) + 3600 * 12
phonenumber = '18566260535'
# 当前日期
now_d = str(datetime.date.today())
# 5天前日期
before_d = str(datetime.date.today() - datetime.timedelta(days=5))
# 5天后日期
after_d = str(datetime.date.today() + datetime.timedelta(days=5))
# print('now: %s\nbefore: %s\nafter: %s' % (now_d, before_d, after_d))
# 回调地址
callback_uri = 'http://121.42.140.86:7070/callback/test'
# 泊寓定制房源编号
# project_code = 'lifeichao-test'
# project_code = '5c468d421fa4073c5bd72c82'
project_code = '5c19b7b8213993244a77efb8'


# 根据需求获取所有的参数
def get_all_param():
    openapi = operate_param_file(flag='openapi')
    onoffline = operate_param_file(flag='onoffline')
    custom = operate_param_file(flag='custom')
    global home_id, home_id_2, room_pub, room_1001_uid, room_1001, lock_uuid_noroute, lock_sn_noroute, address_token, lock_sn, room_1002, room_1003, elemeter_A1_uuid, elemeter_A3_uuid, elemeter_A4_uuid, elecollector_uuid, lock_uuid, gateway_uuid, water_gw_uuid, water_cold_uuid, water_hot_uuid, water_gw_sn, water_cold_sn, water_hot_sn, elemeter_A4_sn, install_ticket, fix_ticket, phone_num, address, client_id, client_secret, openplatform_url, user_name_openplatform, user_pwd_openplatform
    if openapi == '3.0':
        if onoffline == 'on':
            home_id = home_id_30_on
            home_id_2 = home_id_2_30_on
            room_pub = room_pub_30_on
            room_1001_uid = room_1001_uid_30_on
            room_1001 = room_1001_30_on
            room_1002 = room_1002_30_on
            room_1003 = room_1003_30_on
            elemeter_A1_uuid = elemeter_A1_uuid_30_on
            elemeter_A3_uuid = elemeter_A3_uuid_30_on
            elemeter_A4_uuid = elemeter_A4_uuid_30_on
            elecollector_uuid = elecollector_uuid_30_on
            lock_uuid = lock_uuid_30_on
            lock_uuid_noroute = lock_uuid_noroute_30_on
            gateway_uuid = gateway_uuid_30_on
            water_gw_uuid = water_gw_uuid_30_on
            water_cold_uuid = water_cold_uuid_30_on
            water_hot_uuid = water_hot_uuid_30_on
            water_gw_sn = water_gw_sn_30_on
            water_cold_sn = water_cold_sn_30_on
            water_hot_sn = water_hot_sn_30_on
            elemeter_A4_sn = elemeter_A4_sn_30_on
            lock_sn = lock_sn_30_on
            lock_sn_noroute = lock_sn_noroute_30_on
            install_ticket = install_ticket_30_on
            fix_ticket = fix_ticket_30_on
            phone_num = phone_num_30_on
            client_id = client_id_30_on
            client_secret = client_secret_30_on
            openplatform_url = openplatform_url_on
            user_name_openplatform = user_name_openplatform_on
            user_pwd_openplatform = user_pwd_openplatform_on
            address_token = address_token_30_on
            if custom == 'noroute':
                address = address_30_on_noroute
            elif custom == 'pms':
                address = address_30_on_pms
            elif custom == 'sdk':
                address = address_30_on_sdk
            elif custom == 'self':
                address = address_30_on
            else:
                return False
            return True
        elif onoffline == 'off':
            if custom == 'noroute':
                address = address_noroute
            elif custom == 'pms':
                address = address_pms
            elif custom == 'sdk':
                address = address_sdk
            elif custom == 'self':
                return True
            else:
                return False
            return True
        elif onoffline == 'qa-off':
            address_token = address_token_30_off_qa
            if custom == 'noroute':
                address = address_30_off_qa_noroute
            elif custom == 'pms':
                address = address_30_off_qa_pms
            elif custom == 'sdk':
                address = address_30_off_qa_sdk
            elif custom == 'self':
                address = address_30_off_qa
            else:
                return False
            return True
        else:
            return False
    elif openapi == '2.0':
        if onoffline == 'off':
            home_id = home_id_20_off
            home_id_2 = home_id_2_20_off
            room_pub = room_pub_20_off
            room_1001_uid = room_1001_uid_20_off
            room_1001 = room_1001_20_off
            room_1002 = room_1002_20_off
            room_1003 = room_1003_20_off
            elemeter_A1_uuid = elemeter_A1_uuid_20_off
            elemeter_A3_uuid = elemeter_A3_uuid_20_off
            elemeter_A4_uuid = elemeter_A4_uuid_20_off
            elecollector_uuid = elecollector_uuid_20_off
            lock_uuid = lock_uuid_20_off
            lock_uuid_noroute = lock_uuid_noroute_20_off
            gateway_uuid = gateway_uuid_20_off
            water_gw_uuid = water_gw_uuid_20_off
            water_cold_uuid = water_cold_uuid_20_off
            water_hot_uuid = water_hot_uuid_20_off
            water_gw_sn = water_gw_sn_20_off
            water_cold_sn = water_cold_sn_20_off
            water_hot_sn = water_hot_sn_20_off
            elemeter_A4_sn = elemeter_A4_sn_20_off
            lock_sn = lock_sn_20_off
            lock_sn_noroute = lock_sn_noroute_20_off
            install_ticket = install_ticket_20_off
            fix_ticket = fix_ticket_20_off
            phone_num = phone_num_20_off
            client_id = client_id_20_off
            client_secret = client_secret_20_off
            address_token = address_token_20_off
            if custom == 'self':
                address = address_20_off
            elif custom == 'noroute':
                address = address_20_off_noroute
            elif custom == 'pms':
                address = address_20_off_pms
            elif custom == 'sdk':
                address = address_20_off_sdk
            else:
                return False
            return True
        elif onoffline == 'on':
            home_id = home_id_20_on
            home_id_2 = home_id_2_20_on
            room_pub = room_pub_20_on
            room_1001_uid = room_1001_uid_20_on
            room_1001 = room_1001_20_on
            room_1002 = room_1002_20_on
            room_1003 = room_1003_20_on
            elemeter_A1_uuid = elemeter_A1_uuid_20_on
            elemeter_A3_uuid = elemeter_A3_uuid_20_on
            elemeter_A4_uuid = elemeter_A4_uuid_20_on
            elecollector_uuid = elecollector_uuid_20_on
            lock_uuid = lock_uuid_20_on
            lock_uuid_noroute = lock_uuid_noroute_20_on
            gateway_uuid = gateway_uuid_20_on
            water_gw_uuid = water_gw_uuid_20_on
            water_cold_uuid = water_cold_uuid_20_on
            water_hot_uuid = water_hot_uuid_20_on
            water_gw_sn = water_gw_sn_20_on
            water_cold_sn = water_cold_sn_20_on
            water_hot_sn = water_hot_sn_20_on
            elemeter_A4_sn = elemeter_A4_sn_20_on
            lock_sn = lock_sn_20_on
            lock_sn_noroute = lock_sn_noroute_20_on
            install_ticket = install_ticket_20_on
            fix_ticket = fix_ticket_20_on
            phone_num = phone_num_20_on
            client_id = client_id_20_on
            client_secret = client_secret_20_on
            openplatform_url = openplatform_url_on
            user_name_openplatform = user_name_openplatform_on
            user_pwd_openplatform = user_pwd_openplatform_on
            address_token = address_token_20_on
            if custom == 'self':
                address = address_20_on
            elif custom == 'noroute':
                address = address_20_on_noroute
            elif custom == 'pms':
                address = address_20_on_pms
            elif custom == 'sdk':
                address = address_20_on_sdk
            else:
                return False
            return True
        else:
            return False
    elif openapi == 'xx' and onoffline == 'xx':
        home_id = home_id_xx
        home_id_2 = home_id_2_xx
        room_pub = room_pub_xx
        room_1001_uid = room_1001_uid_xx
        room_1001 = room_1001_xx
        room_1002 = room_1002_xx
        room_1003 = room_1003_xx
        elemeter_A1_uuid = elemeter_A1_uuid_xx
        elemeter_A3_uuid = elemeter_A3_uuid_xx
        elemeter_A4_uuid = elemeter_A4_uuid_xx
        elecollector_uuid = elecollector_uuid_xx
        lock_uuid = lock_uuid_xx
        lock_uuid_noroute = lock_uuid_noroute_xx
        gateway_uuid = gateway_uuid_xx
        water_gw_uuid = water_gw_uuid_xx
        water_cold_uuid = water_cold_uuid_xx
        water_hot_uuid = water_hot_uuid_xx
        water_gw_sn = water_gw_sn_xx
        water_cold_sn = water_cold_sn_xx
        water_hot_sn = water_hot_sn_xx
        elemeter_A4_sn = elemeter_A4_sn_xx
        lock_sn = lock_sn_xx
        lock_sn_noroute = lock_sn_noroute_xx
        install_ticket = install_ticket_xx
        fix_ticket = fix_ticket_xx
        phone_num = phone_num_xx
        address_token = address_xx_token
        client_id = client_id_xx
        client_secret = client_secret_xx
        if custom == 'self':
            address = address_xx
        elif custom == 'noroute':
            address = address_xx_noroute
        elif custom == 'pms':
            address = address_xx_pms
        elif custom == 'sdk':
            address = address_xx_sdk
        return True
    else:
        return False


# 获取配置文件
# operate: r or w
# content: when operate == w, write content
# flag: openapi   onoffline   platform  custom
def operate_param_file(operate='r', content=[], flag='openapi'):
    # 读取配置文件
    if operate == 'r':
        # 保存处理后的参数
        ret_list = ['', '', '', '']
        try:
            with open(param_openapi_path+'param.cfg', 'r') as fl:
                ret = fl.readlines()
        except:
            # 读取文件失败，默认返回3.0 线下 非开放平台 自用
            if flag == 'openapi':
                return '3.0'
            elif flag == 'onoffline':
                return 'off'
            elif flag == 'platform':
                return 'openapi'
            elif flag == 'custom':
                return 'self'
        for tmp in ret:
            if tmp.find('openapi=') != -1:
                ret_list[0] = tmp.split("=")[-1].strip('\n')
            elif tmp.find('onoffline=') != -1:
                ret_list[1] = tmp.split("=")[-1].strip('\n')
            elif tmp.find('platform=') != -1:
                ret_list[2] = tmp.split("=")[-1].strip('\n')
            elif tmp.find('custom=') != -1:
                ret_list[3] = tmp.split("=")[-1].strip('\n')
        if flag == 'openapi':
            return ret_list[0]
        elif flag == 'onoffline':
            return ret_list[1]
        elif flag == 'platform':
            return ret_list[2]
        elif flag == 'custom':
            return ret_list[3]
    # 写配置文件
    elif operate == 'w':
        with open(param_openapi_path+'param.cfg', 'w') as fl:
            for tmp in content:
                fl.write(str(tmp)+'\n')
        return True
    # 删除配置文件
    elif operate == 'd':
        os.remove(param_openapi_path+'param.cfg')
    else:
        return False


get_all_param()
