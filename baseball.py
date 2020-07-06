import random



score = 0
out_count = 0
hit_count = 0
homerun_count = 0

batting_name  = [None,"強振","軽打","見送る"]
pitching_name = [None,"直球","変化球","ボール球"]


runner = [None,0,0,0] #左から　ダミー、１塁、２塁、３塁　ランナーいる場合数値を１に

def Homerun(score,runner):
    
    homerun_category = ["none",
                        "★　ソロホームラン!  + 1 点　★","★　2ランホームラン!  + 2 点　★",
                        "★　3ランホームラン!  + 3 点　★","★　満塁ホームラン!  + 4 点　★"]
    
    runner_count = 0
    
    for i in runner:
        if i == 1:
            runner_count += 1
        
    score += runner_count + 1 #ランナーの人数+1得点する
    print(homerun_category[runner_count + 1])
    
    runner = [None,0,0,0]
    
    global homerun_count 
    homerun_count += 1
    
    return score,runner
    
    
    
    

def Hit(score,runner):
    
    if runner[3] == 1:#3塁にランナーいる場合得点
        score += 1
        print("★　タイムリーヒット　+１点　★")
    
    if runner[2] == 1:#２塁から３塁へ進塁
        runner[3] = 1
            
    if runner[1] == 1:#１塁から２塁へ進塁
        runner[2] = 1
    
    runner[1] = 1
    
    global hit_count 
    hit_count += 1
    
    return score,runner

    

def Base_on_ball(score,runner):
    
    if runner[3] == 1:#3塁にランナーいる場合得点
        score += 1
        print("★　押し出し　+１点　★")
    
    if runner[2] == 1:#２塁から３塁へ進塁
        runner[3] = 1
            
    if runner[1] == 1:#１塁から２塁へ進塁
        runner[2] = 1
    
    runner[1] = 1
    
    return score,runner


def Runner_display(runner):
    print("")
   
    if runner[1] == 0:
        if runner[2] == 0:
            
            if runner [3] == 0:
                print("     ◇     ")
                print("            ")
                print("◇       　◇")
                print("          ")   
                print("    　▽    ")
                
            else:                    
                print("     ◇     ")
                print("            ")
                print("◆       　◇")
                print("          ")   
                print("    　▽    ")
                
        elif runner[3] == 0:
            print("     ◆     ")
            print("            ")
            print("◇       　◇")
            print("          ")   
            print("    　▽    ")
            
        else:
            print("     ◆     ")
            print("            ")
            print("◆       　◇")
            print("          ")   
            print("    　▽    ")
             

    if runner[1] == 1:
        if runner[2] == 0:
            
            if runner [3] == 0:                
                print("     ◇     ")
                print("            ")
                print("◇       　◆")
                print("          ")   
                print("    　▽    ")
            else:
                print("     ◇     ")
                print("            ")
                print("◆       　◆")
                print("          ")                       
                print("    　▽    ")
                
                
        elif runner[3] == 0:
            print("     ◆     ")
            print("            ")
            print("◇       　◆")
            print("          ")   
            print("    　▽    ")    
        
        else:
            print("     ◆     ")
            print("            ")
            print("◆       　◆")
            print("          ")   
            print("    　▽    ")  


def Out_count_display(out_count):
    
    print("out:", end="")
    
    for i in range(out_count):
        print("●", end="")    
    
    print("")

def Result(score,hit_count,homerun_count):
    
    print("\n試合終了")
    print("成績")
    print("得点: " + str(score) )
    print("安打: " + str(hit_count))
    print("ホームラン: " + str(homerun_count))
    
    
    
print("""
      『　野球ゲーム監督プレイ（仮）　』

      ルール：
      
      バッティングは「強振」、「軽打」、「見送る」
      
      ピッチングは「直球」、「変化球」、「ボール球」  コマンドを使用できます
      
      相性が良ければ　「安打」、「ホームラン」が打てて
      
      ホームベースを踏むことができれば得点が入ります
      
      3アウトで終了
      
      チェンジは未実装
      
      「h」　入力でちょっとしたヒントを表示します。 
      """)

hint = """
～ ヒント ～
                
    強振　→　「直球」に強く、ホームランが打てます。
    　　　　　「軽打」、「ボール球」に弱く、アウトになってしまいます。
                          
    総評：ランナーが溜まった状態でホームランを打てば高得点が入りますが、
        「直球」以外だとアウトになってしまうため、大味なコマンドです。
        
                           
    軽打　→　 「変化球」に強く、安打が打てます。ランナーが3塁にいると、1点入ります。
    　　　　　　「直球」に弱く、アウトになります。
    　　　　　　「ボール球」はファールにすることができます。
                           
    総評：ホームランは打てませんが、アウトになる確率が1/3であるため、安定したコマンドです。
    
            
    見送る　→　「直球」、「変化球」に弱く、アウトになります。
    　　　　　　「ボール球」だと四球になり、ランナーが進みます。満塁時は、押し出しで1点が入ります。
                            
    総評：他のコマンドと比べると弱いです。
    　　　　相手が「ボール球」を選んできそうな場面限定で有用です
        
                
～ ヒント　終わり ～
"""

while out_count <= 2:
    batting_choise = input("バッティングコマンドを選んでください　（1:強振　2:軽打　3:見送る）\n")
    
    if batting_choise == 'h': #「h」入力でヒント表示
       
        print(hint)
        continue
    
    
    
    batting_choise = int(batting_choise)
    print("")

    #pitching_choise = input("ピッチング　（1:直球　2:変化球　3:ボール球）\n")
    #pitching_choise = int(pitching_choise)
    pitching_choise = random.randint(1,3)
    
    print("自分:"+ batting_name[batting_choise], end="")
    print("    "+"CPU:"+ pitching_name[pitching_choise])
    
        
    
    
    if batting_choise == 1: #「強振」はホームラン打てるが「直球」でなければアウト
        if pitching_choise == 1:
            print("バッティング勝ち")
            result = "ホームラン"
            print("結果:" + result)
            score,runner = Homerun(score,runner)
            print("\n得点:" + str(score))
        
    
        if pitching_choise == 2:
            print("バッティング負け")
            result = "アウト"
            out_count += 1
            print("結果:" + result)
            print("\n得点:" + str(score))
        
        if pitching_choise == 3:
            print("バッティング負け")
            result = "アウト"
            out_count += 1
            print("結果:" + result)
            print("\n得点:" + str(score))
        
    if batting_choise == 2: #「軽打」は「強振」と「見送る」の中間
        if pitching_choise == 1:
            print("バッティング負け")
            result = "アウト"
            out_count += 1
            print("結果:" + result)
            print("\n得点:" + str(score))
        
        if pitching_choise == 2:
            print("バッティング勝ち")
            result = "安打"
            print("結果:" + result)
            score,runner = Hit(score,runner)
            print("\n得点:" + str(score))
        
        if pitching_choise == 3: #「軽打」　と　「ボール球」　の判定どうする？　→ファールにしよう
            print("バッティング引き分け")
            result = "ファール"
            print("結果:" + result)
            print("\n得点:" + str(score))
    
    if batting_choise == 3: #「見逃す」は「ボール球」キラー
        if pitching_choise == 1:
            print("バッティング負け")
            result = "アウト"
            out_count += 1
            print("結果:" + result)
            print("\n得点:" + str(score))
        
        if pitching_choise == 2:
            print("バッティング負け")
            result = "アウト"
            out_count += 1
            print("結果:" + result)
            print("\n得点:" + str(score))
        
        if pitching_choise == 3:
            print("バッティング勝ち")
            result = "四球"
            score,runner = Base_on_ball(score,runner)
            print("結果:" + result)
            print("\n得点:" + str(score))
    
    print("___________")
    Out_count_display(out_count)
    Runner_display(runner)
    print("___________\n")
    

Result(score,hit_count,homerun_count)
