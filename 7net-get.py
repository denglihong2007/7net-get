import requests
import json
headers = headers = {"Host":"teacherapi.7net.cc","Version":"3.0.0","Token":"8C324A8E3B0E8AEFE33FB0439B7B061C_APP_VJ0V85FXF4RXDWRH","User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi Note 8 Build/SP2A.220405.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 septnet browser"}
stu_list = ["安俊钢","安俊南","安俊妍","曹颢","曹颖菲","陈何杰科","陈鹏霏","陈思颖","陈西桥","邓力洪","杜冰怡","冯奕铭","高梦涵","顾梓莹","何美宸","何雨杰","何籽锋","胡榆悦","黄鑫妍","简飞扬","李博文","李东恒","李壕","李欢清","李佳艺霏","李金阳","林焱","林奕佳","刘曦炫","刘宇轩","刘重阳","龙佳居","陆瑞霖","庞力畅","彭文彬","齐彬如","饶皓天","饶钰","尚千惠","谭晓亚","唐菡伯","唐蕊韵","唐一楷","王慧怡","王锦娅","王诗棋","王小垭","王铱麟","王梓茗","吴佳雨","吴静渊","吴宗蔚","谢思琪","谢昕钰","谢俞鸿","徐紫轩","严熙贤","晏峻峰","杨高飞","杨宇航","尹宏月","余佳根","岳恺丞","张嘉洋","张天赐","张雨婷","张梓涵","赵君豪","赵苛含","钟怡瑶","左尚晨"]
with open('.\CMB\R.csv', 'w', newline='') as file:
    file.write("姓名," + str(stu_list)[1:-1].replace("'",""))
    def sget(schoolGuid,classCode,subject,examGuid):
        url = "https://teacherapi.7net.cc/api/PaperAnalysis/GetScenes"
        datas = {"schoolGuid":schoolGuid,"classCode":classCode,"subject":subject,"examGuid":examGuid}
        q_list = json.loads(requests.post(url,headers=headers,data=datas).text)['data']['itemScore']['ths']
        q_list_len = len(q_list)
        stu_list_a = {}
        stu_list_a_no = {}
        for i in stu_list:
            stu_list_a[i] = 0
            stu_list_a_no[i] = q_list_len
        url = "https://teacherapi.7net.cc/api/PaperAnalysis/GetAnswerEntity"
        for i in q_list:
            datas = {"schoolGuid":schoolGuid,"classCode":classCode,"subject":subject,"examGuid":examGuid,"th":i,"obj":"false"}
            get_s=json.loads(requests.post(url,headers=headers,data=datas).text)
            for j in get_s['data']['details']:
                for k in j['list']:
                    stu_list_a[k['name']] = stu_list_a[k['name']] + float(k['score'])
                    stu_list_a_no[k['name']] = stu_list_a_no[k['name']] - 1
        file.write(subject + "分数,"+ str(stu_list_a)[1:-1].replace("'","") + "\n" + subject + "未号个数,"+ str(stu_list_a_no)[1:-1].replace("'","") + "\n")
    sget("c3f91f88-1f32-11e6-9a2b-02004c4f4f50","A925","语文","20221020-0907-42f4-e2b0-eaced2859368")
    sget("c3f91f88-1f32-11e6-9a2b-02004c4f4f50","A925","数学","20221020-0907-42f4-e2b0-eaced2859368")
    sget("c3f91f88-1f32-11e6-9a2b-02004c4f4f50","A925","英语","20221020-0907-42f4-e2b0-eaced2859368")
    sget("c3f91f88-1f32-11e6-9a2b-02004c4f4f50","A925","科学","20221020-0907-42f4-e2b0-eaced2859368")
    sget("c3f91f88-1f32-11e6-9a2b-02004c4f4f50","A925","历史与社会","20221020-0907-42f4-e2b0-eaced2859368")
    file.close()
