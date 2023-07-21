# 从闲鱼获取商品主图数据
# 短链接-真实item信息
# 真实item信息可以在web-h5端访问

import requests
url = """https://h5.m.goofish.com/item?id=719945687523&ut_sk=1.ZI15XuRCxvoDANvagaOs3KbL_21407387_1686993259501.copy.detail.719945687523.2215958134984&forceFlush=1&ownerId=2c8678ce89270d40abb21f6e7a41e2c4&un=0356d687e89b4434710a1ee8faf92a20&share_crt_v=1&un_site=77&spm=a2159r.13376460.0.0&sp_abtk=common_xianyu_commonInfo&sp_tk=VW42aWRyMlRCRTM%3D&cpp=1&shareurl=true&short_name=h.UARIrOw&bxsign=scdLQctM_t_4arxCv_emQ-gJkp0nbxyBz_rHXIbaN2wkS5prqT0SWepUr3bx_Vy4mYXcLVE90gfUTY3TCUg4gcenZnzF6Oyi91VDcwzMvsPMtPKnEDgAMWnztuD7yzH21TpRVZ3jxD5UfqPLeCWR4RJTw&tk=Un6idr2TBE3%20CZ0001&app=chrome"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

# 简单点，使用无头浏览器来搞定之
res = requests.get(url, headers=headers)
with open("1.html", "w+") as f:
    f.write(res.text)

# 从阿里cdn获取图片🆗
url2 = "http://img.alicdn.com/bao/uploaded/i2/O1CN01XAT5yS24lS0WcctZG_!!53-fleamarket.heic"
res = requests.get(url2)
with open("1.jpg", "wb") as f:
    f.write(res.content)


# 改为使用无头浏览器
