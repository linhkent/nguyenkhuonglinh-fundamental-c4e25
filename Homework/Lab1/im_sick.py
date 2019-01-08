def mail_content():
    reason = {
        'cảm cúm' : 'Em sổ mũi và ho liên tục',
        'tiêu chảy' : 'Em đi ngoài rất nhiều lần',
        'đau dạ dày' : 'Bụng em đau dữ dội',
        'giãn dây chằng' : 'Lưng em rất đau đớn, không ngồi thẳng được'
    }
    html = ''' 
   <p>Ch&agrave;o sếp Huy đẹp trai,</p>
<p>Ng&agrave;y h&ocirc;m qua, l&uacute;c đi l&agrave;m về, em thấy trong người mệt mỏi. {{symptom}}. Em c&oacute; đến ph&ograve;ng kh&aacute;m. B&aacute;c sĩ bảo em bị <strong>{{sickness}}</strong>. V&igrave; vậy h&ocirc;m nay em xin ph&eacute;p được nghỉ tĩnh dưỡng. C&ocirc;ng việc em sẽ cố gắng ho&agrave;n th&agrave;nh sớm.</span></span></p>
<p><span class="tlid-translation translation"><span class="" title="">Tr&acirc;n trọng!</span></span></p>
<p><em><span class="tlid-translation translation"><span class="" title="">Nh&acirc;n-vi&ecirc;n-cực-kỳ-gương-mẫu-v&agrave;-chăm-chỉ-của-anh!</span></span></em></p>'''
    rk = random.choice(list(reason.keys()))
    html_content = html.replace('{{sickness}}',rk).replace('{{symptom}}',reason[rk])
    return(html_content)
def mail_send(receiver, content):
    mail = gmail.GMail('Khuong linh <abc@gmail.com>','******')
    msg = gmail.Message('Đơn xin nghỉ phép',to=receiver,html=content)
    mail.send(msg)
    return()
# MAIN
import gmail
import schedule
import random
import time
content = mail_content()
receiver = 'qhuydtvt@gmail.com'
    # schedule send email
def lazy():
    mail_send(receiver, content)
schedule.every().day.at("7:00").do(lazy)
while True:
    schedule.run_pending()
    time.sleep(1)