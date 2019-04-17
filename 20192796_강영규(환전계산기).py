# 실생활에서 사용할 수 있는 변환 프로그램 만들기
# 환율계산기

# 시간정보를 가져오기 위한 모듈
import time
# 환율정보를 네이버로부터 가져오는 모듈
import urllib.request
page = urllib.request.urlopen(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8")
text = page.read().decode("utf8")
# 나라별 환율정보(url들어가서 우클릭하고 페이지 소스를 누르면 얻을 수 있음)
Japan = text.find('<span>일본 <em>JPY 100</em></span></a></th> <td><span>')
position = text[Japan + 52:Japan + 60]
China = text.find("<span>중국 <em>CNY</em></span></a></th> <td><span>")
position1 = text[China + 48:China + 54]
USA = text.find('<span>미국 <em>USD</em></span></a></th> <td><span>')
position2 = text[USA + 48:USA + 56]
Euro=text.find('<span>유럽연합 <em>EUR</em></span></a></th> <td><span>')
position3 = text[Euro+50:Euro+58]






#필요한 변수들
out = 0 #탈출
escape = 0
won = 0
yen = 0
usd = 0
kmoney = 1000 #기준 원화 1000원으로 설정





while True: #반복문 while문 사용
    print("\t\t\t\t <<<<어서오세요>>>>\n\t\t\t    <<<<환율계산프로그램입니다>>>>\n") #소개
    print("\t\t   <<<실행기준날짜:", time.strftime('%c 기준>>>\n ', time.localtime(time.time())))  # 프로그램을 시작한 순간부터의 날짜와 시간을 저장하여 출력함/cmd창에는 time모듈이 없기때문에 인식X,Idle에서 열지 않으면 오류발생
    money = int(input("\t\t\t\t      <<메뉴>> \n\n\t\t\t\t   1.엔화(¥)환전\n\t\t\t\t   2.달러($)환전\n\t\t\t\t   3.위안(¥)환전\n\t\t\t\t   4.유로(€)환전\n\t\t\t\t   5.나가기\n선택:  "))  # 메뉴
    if money == 1:
         time.sleep(0.5) #프로그램의 느낌이 나게 0.5초씩 멈춰줌
         print("\t\t\t      <<엔화(Yen:¥) 환전계산기>>\n")
         time.sleep(0.5)
         print("\t\t\t      엔화환전을 선택하셨습니다.\n \t\t  계속하시려면 1번,잘못실행하셨다면 2번을 눌러주세요") #프로그램을 계속해서 실행할려면 1번을 누르고 만약 실수로 다른 메뉴를 들어왔다면 2번을 눌러서 메뉴창으로 다시 돌아감
         escape = int(input("\t\t\t\t     1.계속\n\t\t\t\t     2.나가기\n\n선택: "))
         time.sleep(0.5)
         if escape == 1:  # escape에 번호 '1'이 입력되면 프로그램이 실행됌.
              kor = int(input("\t\t엔화(¥)를 원화(\)로 환전하시겠습니까? (1번을/를 눌러주세요)\n\t\t\t\t\tOR\n\t\t원화(\)를 엔화(¥)로 환전하시겠습니까? (2번을/를 눌러주세요)\n선택: "))  # 1번을 누르면 엔화를 원화로 환전
                                                                                                                                                                                          # 2번를 누르면 원화를 엔화로 환전
              if kor == 1:
                   print("현시간 기준 엔화 환율(100엔):", position, "원")
                   time.sleep(0.5)
                   yen = int(input("한화로 환전하실 엔화(¥)을/를 입력하십시요:"))
                   time.sleep(0.75)
                   print("실시간으로 환전하신 엔화는 %0.1f" % (float(float(yen / 100) * float(
                        position[0] + position[2] + position[3] + position[4] + position[5] + position[6] + position[7]))),"원(\) 입니다")  # position변수는 숫자와 문자가 섞여있는 string문자열이기 때문에
                                                                                                                                            # float형과 같이 대입할려고하면 문제가 발생했다.그래서 position 변수안에 있는 숫자를
                                                                                                                                            # 꺼내 대입하기 위해 중괄호([])를 사용하여 위치를 정해줌으로써 숫자를 꺼내고 대입할 수 있었다
                   break  # 환전을 끝내면 프로그램을 종료 
              if kor == 2:
                   print("현시간 기준 원화 환율(1000원):%.2f" % (float(kmoney) / (float( # %.2f를 사용해 소수점이하 둘째자리까지 출력
                        position[0] + position[2] + position[3] + position[4] + position[5] + position[6] + position[7])) * 100), "엔")                # '2'를 누르면 원화를 엔화로 환전할 수 있다.
                   time.sleep(0.5)
                   won = int(input("환전하실 원화(\)을/를 입력하십시요:"))
                   time.sleep(0.75)
                   print("실시간으로 환전하신 원화는 %0.2f" % (float(won) * (float(kmoney) / float(position[0] + position[2] + position[3] + position[4] + position[5] + position[6] + position[7]) / 10)), "엔(¥) 입니다")
                   break

         if escape==2:# 이 프로그램을 사용하는 유저가 잘못들어왔을때를 가정해 만들어둔 것
             time.sleep(1.5) #넘어가는 순간 1.5초 멈춤
             out=int(input("\t메뉴창으로 돌아가실려면 1번,프로그램을 종료하실려면 2번을 눌러주세요.\n선택: "))
             if out==1:
                 print("\t\t\t      <<<메뉴창으로 돌아갑니다>>>\n\n\n\n\n") #1번을 누르면 메뉴창으로 돌아감
                 time.sleep(2) #2초뒤 메뉴창으로 돌아감
                 continue   
             else:
                 break # 2번을를 누르면 종료
                   
         #아래의 내용은 다 똑같음

    elif money == 2:
         time.sleep(0.5)
         print("\t\t\t    <<달러(Dollar:$) 환전계산기>>\n")
         time.sleep(0.5)
         print("\t\t\t      달러환전을 선택하셨습니다.\n \t\t  계속하시려면 1번,잘못실행하셨다면 2번을 눌러주세요")
         time.sleep(0.5)
         escape = int(input("\t\t\t\t     1.계속\n\t\t\t\t     2.나가기\n선택: "))
         if escape == 1:
              time.sleep(0.5)
              kor = int(input( "\t\t달러($)를 원화(\)로 환전하시겠습니까? ('1'을/를 눌러주세요)\n\t\t\t\t\tOR\n\t\t원화(\)를 달러($)로 환전하시겠습니까? ('2'을/를 눌러주세요)\n선택: "))
              
              if kor == 1:
                    print("현시간 기준 달러 환율(1달러):", position2, "원")
                    time.sleep(0.5)
                    usd = int(input("한화로 환전하실 달러($)을/를 입력하십시요:"))
                    time.sleep(0.75)
                    print('실시간으로 환전하신 $%.1f은 원화로' % usd, float(position2[0] + position2[2] + position2[3] + position2[4] + position2[5] + position2[6] + position2[7]) * usd, '원(\) 입니다')
                    break
              if kor==2:
                   print("현시간 기준 원화 환율(1000원):%.2f" % float(float(kmoney) / float( position2[0] + position2[2] + position2[3] + position2[4] + position2[5] + position2[6] + position2[7])), "달러")
                   time.sleep(0.5)
                   won = int(input("환전하실 원화(\)을/를 입력하십시요:"))
                   time.sleep(0.75)
                   print("실시간으로  환전하신 원화는 %.2f" % (float(float(won) / float( position2[0] + position2[2] + position2[3] + position2[4] + position2[5] + position2[6] + position2[7]))), "달러($) 입니다")
                   break
         if escape==2:# 이 프로그램을 사용하는 유저가 잘못들어왔을때를 가정해 만들어둔 것
             time.sleep(1.5) #넘어가는 순간 1.5초 멈춤
             out=int(input("\t메뉴창으로 돌아가실려면 1번,프로그램을 종료하실려면 2번을 눌러주세요.\n선택: "))
             if out==1:
                 print("\t\t\t      <<<메뉴창으로 돌아갑니다>>>\n\n\n\n\n") #1을 누르면 메뉴창으로 돌아감
                 time.sleep(2) #2초뒤 메뉴창으로 돌아감
                 continue   
             else:
                 break #2를 누르면 종료
         
        


    elif money == 3:
         time.sleep(0.5)
         print("\t\t\t     <<위안(CNY:¥) 환전계산기>>\n")
         time.sleep(0.5)
         print("\t\t\t      위안환전을 선택하셨습니다.\n \t\t  계속하시려면 1번,잘못실행하셨다면 2번을 눌러주세요")
         time.sleep(0.5)
         escape = int(input("\t\t\t\t     1.계속\n\t\t\t\t     2.나가기\n선택: "))
         if escape == 1:
              time.sleep(0.5)
              kor = int(input("\t\t위안(¥)를 원화(\)로 환전하시겠습니까? ('1'을/를 눌러주세요)\n\t\t\t\t\tOR\n\t\t원화(\)를 위안(¥)으로 환전하시겠습니까? ('2'을/를 눌러주세요)\n선택: "))
              time.sleep(0.5)
              if kor == 1:
                   print("현시간 기준 위안(¥) 환율(1위안):", position1, "원")
                   time.sleep(0.5)
                   cny = int(input("한화로 환전하실 위안(¥)을/를 입력하십시요:"))
                   time.sleep(0.75)
                   print('실시간으로 환전하신 ¥%.1f은 원화(\)로' % cny, float(cny) * float(position1[0] + position1[1] + position1[2] + position1[3] + position1[4] + position1[5]),'원(\) 입니다')
                   break
              if kor == 2:
                   print('현시간 기준 원화 환율(1000원):%.2f' % float(float(kmoney) / (float(position1[0] + position1[1] + position1[2] + position1[3] + position1[4] + position1[5]))),"위안(¥)")
                   time.sleep(0.5)
                   won = int(input("환전하실 원화(\)을/를 입력하십시요:"))
                   time.sleep(0.75)
                   print('실시간으로 환전하신 원화(\)는 %0.2f' % (float(won) / (float(position1[0] + position1[1] + position1[2] + position1[3] + position1[4] + position1[5]))),'위안(¥)입니다.')
                   break
         if escape==2:# 이 프로그램을 사용하는 유저가 잘못들어왔을때를 가정해 만들어둔 것
             time.sleep(1.5) #넘어가는 순간 1.5초 멈춤
             out=int(input("\t메뉴창으로 돌아가실려면 1번,프로그램을 종료하실려면 2번을 눌러주세요.\n선택: "))
             if out==1:
                 print("\t\t\t      <<<메뉴창으로 돌아갑니다>>>\n\n\n\n\n") #1을 누르면 메뉴창으로 돌아감
                 time.sleep(2) #2초뒤 메뉴창으로 돌아감
                 continue   
             else:
                 break #2를 누르면 종료
         
              
    elif money == 4:
         time.sleep(0.5)
         print("\t\t\t     <<유로(EUR:€) 환전계산기>>\n")
         time.sleep(0.5)
         print("\t\t\t      유로환전을 선택하셨습니다.\n \t\t   계속하시려면 1번,잘못실행하셨다면 2번을 눌러주세요")
         time.sleep(0.5)
         escape = int(input("\t\t\t\t     1.계속\n\t\t\t\t     2.나가기\n선택: "))
         if escape == 1:
              time.sleep(0.5)
              kor = int(input("\t\t유로(€)를 원화(\)로 환전하시겠습니까? ('1'을/를 눌러주세요)\n\t\t\t\t\tOR\n\t\t원화(\)를 유로(€)로 환전하시겠습니까? ('2'을/를 눌러주세요)\n선택: "))
              time.sleep(0.5)
              if kor == 1:
                   print("현시간 기준 유로 환율(1유로):", position3, "원")
                   time.sleep(0.5)
                   eur = int(input("한화로 환전하실 유로(€)을/를 입력하십시요:"))
                   time.sleep(0.75)
                   print('실시간으로 환전하신 €%.1f은 원화로' % eur, float(eur) * float(position3[0] + position3[2] + position3[3] + position3[4] + position3[5] + position3[6]+position3[7]),'원(\) 입니다')
                   break
              if kor == 2:
                   print('현시간 기준 원화 환율(1000원):%.2f' % float(float(kmoney) / (float(position3[0] + position3[2] + position3[3] + position3[4] + position3[5] + position3[6]+position3[7]))), "유로(€)")
                   time.sleep(0.5)
                   won = int(input("환전하실 원화(\)을/를 입력하십시요:"))
                   time.sleep(0.75)
                   print('실시간으로 환전하신 원화는 %0.2f' % (float(won) / (float(position3[0] + position3[2] + position3[3] + position3[4] + position3[5] + position3[6]+position3[7]))), '유로(€)입니다.')
                   break
         if escape==2:# 이 프로그램을 사용하는 유저가 잘못들어왔을때를 가정해 만들어둔 것
             time.sleep(1.5) #넘어가는 순간 1.5초 멈춤
             out=int(input("\t메뉴창으로 돌아가실려면 1번,프로그램을 종료하실려면 2번을 눌러주세요.\n선택: "))
             if out==1:
                 print("\t\t\t      <<<메뉴창으로 돌아갑니다>>>\n\n\n\n\n") #1을 누르면 메뉴창으로 돌아감
                 print(time.sleep(2)) #2초뒤 메뉴창으로 돌아감
                 continue   
             else:
                 break #2를 누르면 종료
         
         

    elif money==5: #5번을 누르면 프로그램 종료
        break
    else:
         print("\t\t\t\n잘못입력하셨습니다.메뉴로 돌아갑니다") #처음 메뉴창이 떴을때 1에서 5까지의 숫자가 아닌 다른 숫자를 입력하면 메시지가 뜨고 다시 메뉴창으로 돌아감
         

time.sleep(0.5)
print("이용해주셔서 감사합니다, 행복한 하루 되십시요.")
