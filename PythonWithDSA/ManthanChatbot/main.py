file = open("response.txt", "r")
data = file.read().split("\n")
file.close()

dic = dict()
for line in data:
    k,v = line.split(" : ")
    dic[k] = v 

def chatKro():
    while True:
        prompt = input("enter a msg = ")
        if prompt in ["by", "bye", "good bye"]:
            print("Good by buddy")
            print("thank you🙏")
            break 
        
        if "calc" in prompt:
            ex = prompt.replace("calc","")
            print(f"{ex} = {eval(ex)}")
            continue

        if prompt in dic:
            print(dic[prompt])
        else:
            ans = input(f"tell me answer of '{prompt}' = ")
            file = open("response.txt","a")
            file.write(f"\n{prompt} : {ans}")
            file.close()
            dic[prompt] = ans

chatKro()

        

