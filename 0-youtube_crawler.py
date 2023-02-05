import time
import csv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = []
youtube_video_url = "https://www.youtube.com/watch?v=wJmUTfZCvhU"

with Chrome() as driver:

    wait = WebDriverWait(driver, 15)

    driver.get(youtube_video_url)

    video_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text

    for item in range(200):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        data.append([video_title, comment.text])

with open("youtube_comments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Video Title", "Comment"])
    writer.writerows(data)

    
    
    
'''
Video List
- Nissan Ariya
- https://www.youtube.com/watch?v=wJmUTfZCvhU
- https://www.youtube.com/watch?v=oIkETEaiHAo
- https://www.youtube.com/watch?v=hbykcnRP3Rc
- https://www.youtube.com/watch?v=FG4L_tQKwvQ
- https://www.youtube.com/watch?v=G4dtSpUpNec
- https://www.youtube.com/watch?v=-2KCb342cvw
- https://www.youtube.com/watch?v=j4gsJrnugDo
- https://www.youtube.com/watch?v=drQoMnU0euY
- https://www.youtube.com/watch?v=wplJU_Za9cI
- https://www.youtube.com/watch?v=7aa-ba2pvIs
- https://www.youtube.com/watch?v=eanzPeFrask
- https://www.youtube.com/watch?v=kI64VG-iRWs


- Nissan Leaf
-	https://www.youtube.com/watch?v=Ebx7gQCvqI0
-	https://www.youtube.com/watch?v=DkPs_BXSmWc
-	https://www.youtube.com/watch?v=atNwVXyIRP8
-	https://www.youtube.com/watch?v=gd_XNwNiTio
-	https://www.youtube.com/watch?v=WlOvInMME7Q
-	https://www.youtube.com/watch?v=lczuI_sBS-E
-	https://www.youtube.com/watch?v=AMpgcaHaN5k
-	https://www.youtube.com/watch?v=jvPTsx7e6gY
-	https://www.youtube.com/watch?v=dgKeZJuCdns
-	https://www.youtube.com/watch?v=bZgEoPVJlLU
-	https://www.youtube.com/watch?v=bHX6okFZfOI
-	https://www.youtube.com/watch?v=YBPC4sjKjUc
-	https://www.youtube.com/watch?v=FpafCyRboeg

- Chevy Equinox EV
-	https://www.youtube.com/watch?v=sVCvTlcxu4k
-	https://www.youtube.com/watch?v=ZPo-A3NBSTo
-	https://www.youtube.com/watch?v=wYnWIz9pNUE
-	https://www.youtube.com/watch?v=3WT-VSn_wLM
-	https://www.youtube.com/watch?v=HOIdVOpjFGg
-	https://www.youtube.com/watch?v=UMmF9Pykzsc
-	https://www.youtube.com/watch?v=NZ4u401LryM
-	https://www.youtube.com/watch?v=zCiQA4Dv_GE
-	https://www.youtube.com/watch?v=gBP-oOOkw6g
-	
- Ford F150 Lightning
-	https://www.youtube.com/watch?v=CkoquiSnqbk
-	https://www.youtube.com/watch?v=LRVVE707iHg
-	https://www.youtube.com/watch?v=Bq5EwFRab6Q
-	https://www.youtube.com/watch?v=HZKy6WRtGWs
-	https://www.youtube.com/watch?v=6tkPJ09xMBU
-	https://www.youtube.com/watch?v=bJ3uk86VZxU
-	https://www.youtube.com/watch?v=FsQd3D84HjA
-	https://www.youtube.com/watch?v=egXm1MrZ170
-	
- Ford Mustang Mach-E
-	https://www.youtube.com/watch?v=I1rP6kSFyPc
-	https://www.youtube.com/watch?v=c4n5iPqxpaw
-	https://www.youtube.com/watch?v=9-fDoTImbn0
-	https://www.youtube.com/watch?v=QLX8A_ZDCvY
-	https://www.youtube.com/watch?v=tS-Bnl7SKbg
-	https://www.youtube.com/watch?v=T_zIbmGvrm4
-	https://www.youtube.com/watch?v=7acYzpXZHvQ
-	
-   Hyundai Ioniq 4
- https://www.youtube.com/watch?v=Oi0Uqz7CbxQ
- https://www.youtube.com/watch?v=nkG2qaU9Kys
- https://www.youtube.com/watch?v=bJZuPdmwBf4
- Hyundai Ioniq 3
- https://www.youtube.com/watch?v=pYkReZaO7gA
- https://www.youtube.com/watch?v=54LUXMRS5hw
- https://www.youtube.com/watch?v=YvDY5AoeHN0
- https://www.youtube.com/watch?v=HwR0SodHVLY
•	Hyundai Ioniq 5
- https://www.youtube.com/watch?v=d7y9z7pjCRM
- https://www.youtube.com/watch?v=LJiIjEpky54
- https://www.youtube.com/watch?v=qRdq1y9RQhY
- https://www.youtube.com/watch?v=V_Tfu8othJc
- https://www.youtube.com/watch?v=A64twNzBCeU
- https://www.youtube.com/watch?v=B1YKP9Twdmg
- https://www.youtube.com/watch?v=3mgh_1-1sTU
- https://www.youtube.com/watch?v=BReRIxqO_Lg
- https://www.youtube.com/watch?v=H2AKIyDb0lM

- Kia EV6
- https://www.youtube.com/watch?v=ggR-5P1i8U8
https://www.youtube.com/watch?v=VU_vGXAewoE
https://www.youtube.com/watch?v=5bea6OBb8SQ
https://www.youtube.com/watch?v=HiZ64IEVQ6g
https://www.youtube.com/watch?v=ZQ1Y8giggKg
https://www.youtube.com/watch?v=tSVRlIsN85I
https://www.youtube.com/watch?v=ZjPciIahGdI
https://www.youtube.com/watch?v=mOwmow9e6Hs
https://www.youtube.com/watch?v=eO3COLniB_E
https://www.youtube.com/watch?v=LInZP8YtzEI
https://www.youtube.com/watch?v=FioyBZoe914
https://www.youtube.com/watch?v=CqCTdVimcp4
https://www.youtube.com/watch?v=d2GBFKcQ8q8

- Kia EV3
- https://www.youtube.com/watch?v=bJZuPdmwBf4&t=8s
https://www.youtube.com/watch?v=1lcVOMCm3Sc
https://www.youtube.com/watch?v=zgYoZHbq2pM
- Kia EV4
https://www.youtube.com/watch?v=FOWk0R0PJGI
https://www.youtube.com/watch?v=HwR0SodHVLY&t=6s
https://www.youtube.com/watch?v=YvDY5AoeHN0&t=4s
https://www.youtube.com/watch?v=r4Z8gu0B9kk
- Kona EV
https://www.youtube.com/watch?v=Z4gT7GFvrP8
https://www.youtube.com/watch?v=bK8Bxw5OEXs
https://www.youtube.com/watch?v=KGNmCJMwfbM
https://www.youtube.com/watch?v=ZNu3UTTkvBE
https://www.youtube.com/watch?v=emcZlJ45oVE
https://www.youtube.com/watch?v=JGjF4KxX46g
https://www.youtube.com/watch?v=E1dhttZUYJg
https://www.youtube.com/watch?v=Wo52jl2Vit8
https://www.youtube.com/watch?v=Hl2992UxejY
https://www.youtube.com/watch?v=ZDuVVEGaodI&list=RDQMTP_a9gy1MWk&start_radio=1


- Tesla Model 3
https://www.youtube.com/watch?v=5HejdMHL74o
https://www.youtube.com/watch?v=9CU530gjqco
https://www.youtube.com/watch?v=tYahCom6eT0
https://www.youtube.com/watch?v=uLUtEeEq33w
https://www.youtube.com/watch?v=kbulCM90w8w
https://www.youtube.com/watch?v=oLkxklTpSH0
https://www.youtube.com/watch?v=D8dMJe_h9VQ
https://www.youtube.com/watch?v=BsXT4itf9cg
https://www.youtube.com/watch?v=6e9M12lMC5s
https://www.youtube.com/watch?v=_JYCgrPS-lM
https://www.youtube.com/watch?v=jWXTcPy8AGQ
https://www.youtube.com/watch?v=U9EqpnirQC0
https://www.youtube.com/watch?v=siZs3E6zlmo
https://www.youtube.com/watch?v=C55k7TazVfM

- Tesla Model Y
https://www.youtube.com/watch?v=wMjsAL0hVqU
https://www.youtube.com/watch?v=ATDPv11B5Uc
https://www.youtube.com/watch?v=XSTvZhJXffY
https://www.youtube.com/watch?v=3vgLWwfP0I8
https://www.youtube.com/watch?v=OQri1NdscR4
https://www.youtube.com/watch?v=KAJFALcJjac
https://www.youtube.com/watch?v=FONBWVnnow0
https://www.youtube.com/watch?v=R1JzXdwVe74
https://www.youtube.com/watch?v=5r9AP2LwI3M
https://www.youtube.com/watch?v=a3XIeJOb51E
https://www.youtube.com/watch?v=lfCrBSwbXT0
https://www.youtube.com/watch?v=LpwctWk9KxE
https://www.youtube.com/watch?v=yXyV_4Lg-PA
https://www.youtube.com/watch?v=rTyRmwde1kE
https://www.youtube.com/watch?v=QvrWhRhLxew
https://www.youtube.com/watch?v=Ny2VqOfGeHc
https://www.youtube.com/watch?v=r4jNRyHnNFE


- VW ID.4
https://www.youtube.com/watch?v=WD1vteOfmyI
https://www.youtube.com/watch?v=nAwUkLp7T9A
https://www.youtube.com/watch?v=6DMOOAVktBU
https://www.youtube.com/watch?v=bvwG9UoCGaM
https://www.youtube.com/watch?v=1ugfL2bf-ho
https://www.youtube.com/watch?v=KTNmRWn-AwM
https://www.youtube.com/watch?v=pwMB-H9HnIk
https://www.youtube.com/watch?v=QbsHEO3rJo4
https://www.youtube.com/watch?v=ikheO2Nb3-k
https://www.youtube.com/watch?v=uzGs9OabeJ8
https://www.youtube.com/watch?v=vOYkxiOFI7Q
https://www.youtube.com/watch?v=mB7X4WF_p9M


- Toyota bZ4X
https://www.youtube.com/watch?v=Vtg3nIZH_cE
https://www.youtube.com/watch?v=yJEUOZC8FKY
https://www.youtube.com/watch?v=feqeTwe7WUM
https://www.youtube.com/watch?v=S9BVG4miqXw
https://www.youtube.com/watch?v=mrktYHIDv2M
https://www.youtube.com/watch?v=sX7EEuwFZYE
https://www.youtube.com/watch?v=sX1q5ij8Dn8
https://www.youtube.com/watch?v=wmG5JUadl1k
https://www.youtube.com/watch?v=MUGu3aWTdwc
https://www.youtube.com/watch?v=W-0j6FCrD1g
https://www.youtube.com/watch?v=sX7EEuwFZYE&t=6s
https://www.youtube.com/watch?v=GO1qW8oCNWw
https://www.youtube.com/watch?v=bXVFc5Y7DiI
https://www.youtube.com/watch?v=jFlcQwyWgUo
https://www.youtube.com/watch?v=ueJZPRWMCkY
https://www.youtube.com/watch?v=5tA--j4g73Y


- Toyota bZ3X
https://www.youtube.com/watch?v=0IYWapJM1Kk
https://www.youtube.com/watch?v=dwPXtwojmwA
https://www.youtube.com/watch?v=me8_7nes_Qw
https://www.youtube.com/watch?v=Ph3UzFPqP90
https://www.youtube.com/watch?v=BbqWdBb1x7o
https://www.youtube.com/watch?v=n6wYqr6N_2g
https://www.youtube.com/watch?v=bhCUaBERVXs
https://www.youtube.com/watch?v=me8_7nes_Qw&t=5s


- Subaru Solterra
https://www.youtube.com/watch?v=vCOYkYwEXPE
https://www.youtube.com/watch?v=Cq0CxnawS-w
https://www.youtube.com/watch?v=fqFfvkprYRc
https://www.youtube.com/watch?v=Fz8w4cn2c8M
https://www.youtube.com/watch?v=PIBZZooeFJI
https://www.youtube.com/watch?v=8OBuzxGSl80
https://www.youtube.com/watch?v=hqWi7f3Ens8
https://www.youtube.com/watch?v=hcfiAHvfHoQ
https://www.youtube.com/watch?v=fEEwFPAYDnc
https://www.youtube.com/watch?v=5cwBEfvhVWE
https://www.youtube.com/watch?v=XWpMH4qrFmg
https://www.youtube.com/watch?v=PnbkJGx4myg
https://www.youtube.com/watch?v=jmkADV8TGz8

- Honda Prologue
https://www.youtube.com/watch?v=9tmn8IphgAM
https://www.youtube.com/watch?v=FwEfJ7zBmXk
https://www.youtube.com/watch?v=P7rEaWTYJdg
https://www.youtube.com/watch?v=qpT-2tOp8ww
https://www.youtube.com/watch?v=z2_3fnXcRek
https://www.youtube.com/watch?v=MmEMB0a6se4
https://www.youtube.com/watch?v=7VPcWWeuPYM
https://www.youtube.com/watch?v=jx1d3p6hVUk
https://www.youtube.com/watch?v=ZIiXB1aysiA
https://www.youtube.com/watch?v=zH8hQ-N7oU4

'''
