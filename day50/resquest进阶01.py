#登录->得到cookie
#带着cookie去拿到书架url—>书架上的内容

# 必须把上面两个操作连起来
#我们可以使用session进行请求->session是一连串的请求，在这个过程中的cookie不会丢失
#
import requests
#
session = requests.session()#会话session
# data={
#     'loginName':' 15664753579',
#     'password':'2003815K?'
# }
# #登录
# url='https://passport.17k.com/ck/user/login'
# session.post(url,data=data)
# # print(resp.text)
# # print(resp.cookies)
#
# # #拿到书架上的数据
#刚才的那个session中有cookie
resp=session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919',headers={"Cookie":"GUID=4de6962c-4a68-4fb8-a29d-b4546579b10a; acw_sc__v2=6807897be1db7661fa3cd93dd32f0f8f9f526581; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1745324412,1745325244; HMACCOUNT=8F265BB7C63083A9; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F02%252F22%252F06%252F104090622.jpg-88x88%253Fv%253D1745324560000%26id%3D104090622%26nickname%3D%25E4%25B9%2584%25E4%25B8%25B6418512318%26e%3D1760877502%26s%3D887dc4dcdd189a1a; ssxmod_itna=7qUOD5DKiI4fxBPGKiQi3rSDujCRh=EP+dIpdD/A+DnqD=GFDK40oA7oPAPKvmqebZkuPtqb17Gmhobm4nT3dbPM0PoiDCPGnDBFvdADeW=D5xGoDPxDeDADYoXDAqiOD7qDdjpkVUkDm4GW7qGfDDoDY+=uDitD4qDBzhdDKqGgzdxD0uovDYv2iG0egf2SfCU=bm437qDMUeGXCi9e7dROL=hZbCcFPQPuDB6hxBjMfwNXfeDHzLNlem5IFYLeBg35FOq3tBTob7wpQOD39Yx4/oLP9BGqlGwPi24j65DAAYxdU8zxD===; ssxmod_itna2=7qUOD5DKiI4fxBPGKiQi3rSDujCRh=EP+dIPG9iEttDBuqY5GaYEyt9+oCTIx8hRQ3ZD3m70O/FB3Obm4Z6EE0vP6SWBnjcAfC99f5XtIk7wqZ3a1HsF1Ht88UQEuIAXpzTFHQBMj2eC1Zu4AoxkvEHz6hFssxP8tD7bL2BDxUvFj2Tp=Sudq/AzP4gAuQowXBgFKSqPrSq+QtEvYFSLomowy3HLscgrstTXqZyT5Mk+P=Kw39AiNK1TK3njKHQE4VluBOjyTuBEGNqIBIj244EUXbAR6d1=7S37o0/yfV3rRgGUR6DrAy4UKAChCU97/5QGWfQFAGe3D07m0xC0GdhDe7YBAKeA+TxF1WwWGw3B+ci5cYxk7YqGeKQ8ECxLjC2BmWYxqDQd0itYq73mBWv10ihBI2Gpm0ikAD/MYY6wK+DkDDLxD27vqzGxyrNYoPfAH1DTA0DIePBozifeietZSDK0/iiNSG=ddIbiQlvOMhz=7xSrqtk7TiOgxd0dDEGDD===; tfstk=gjxmaH2mjE7jRzOLMQSj-UDYik0RG-s1PCEO6GCZz_556x1AMdRMIp7N3oRvr1AyZsSODnnMS_SV5ECOM1jMCBD-9DnphKs14XhKv-8CQ6SC3-546aPPIGX2rcUEDKs1bbe8b2nHhIsCr2-VbYjPIOUNblRNzu55COPVQokkU_1z0O7a0T5PC9XV_CSZEL55QGWqgbgVGh-y4btEtQMh8Xx5nZfe3sJvL3zcyr9PZuqkqUbcTGfubl-lndf_IjEnW68CMwCMa0EcjLWMZwLmtoAMQpTNrhVqHBRySCWWPf4GtFJvRF7o3mJlmsblnZw4SiYwGhbXoRMBUiRWR6_qPb6kDHQGOaVrgLplgwYMMbZNMevyZwK8wkIeRQxG8MSzszzUj-r1UAKu5P_VFTfdCIBnECx6fLDoEyk1uT6f9YDu57NQblU-EY4E4ZW53ff..; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104090622%22%2C%22%24device_id%22%3A%221965d710db2724-01e7aad0745c808-4c657b58-1327104-1965d710db316dd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%224de6962c-4a68-4fb8-a29d-b4546579b10a%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1745326702"})
print(resp.text)