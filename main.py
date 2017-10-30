import requests, random
config = {
    "email" : "email@gmail.com",
    "share_code" : "ZERO23649",
    "amount" : 2
}
#  ^^^ ONLY Change the part in quotes on the right side of :
# Your share code it the last part of the share URL you get when signing up initially

x = 0
def main():
    email = config['email'].split('@')[0]
    domain = config['email'].split('@')[1]
    postEmail = "{}_{}@{}".format(email, random.randint(0,999999), domain)
    # print postEmail
    url = "https://zerofinancial.com/api/v1/user/"
    try:
        response = requests.post(url=url, json={
            "access_code" : config['share_code'],
            "campaign" : "null",
            "email" : postEmail,
            "is_mobile" : False,
            "source" : "null"
        }, headers = {
            "user-agent" : "_zruss_ was here"
        })
        if response.status_code == 200:
            print "{}: Success".format(postEmail)
    except Exception as e:
        print e


while x < config['amount']:
    main()