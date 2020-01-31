line   = "\n---------------------------"

def write_review():
    post = {}

    post["genre"] = input("ジャンルを入力:\n")
    post["title"]= input("タイトルを入力:\n")
    post["review"] = input("感想を入力:\n")
    
    
    
    print("ジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 :\n" + post["review"]  + line)
    
    posts.append(post)


def read_reviw():
    for (i,post) in enumerate(posts):
        print('[' + str(i) + ']:' + post['title'] + "のレビュー")
    user_input = int(input("見たい番号を入力"))
    post = posts[user_input]
    print("ジャンル :" + post["genre"] + line)
    print("タイトル:" + post["title"] + line)
    print("感想 :" + post["review"] + line)



posts = []
    
    
while True:
    print("\nレビュー数：" + str(len(posts)))
    print("[0]レビューを書く")
    print("[1]レビューを読む")
    print("[2]アプリを終了する")
    user_input = input()
    
    try:
        if int(user_input) == 0:
            write_review()
        
        elif int(user_input) == 1:
            read_reviw()
        
        elif int(user_input) == 2:
            print("終了します")
            exit()
            
        else:
            print("入力された値は無効な値です")
            
    except ValueError:
        print("数字を入力してください")

