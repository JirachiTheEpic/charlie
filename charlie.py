import requests
import time
from datetime import datetime

# ============================================================
#  charlie
#  so cool
# ============================================================

SESSION_ID = "YOUR_SESSION_ID_HERE"   # thineth sessiono id
USERNAME = "YOUR_USERNAME_HERE"      # thineth usernamington

def post_comment(project_id, comment_text):
    url = f"https://scratch.mit.edu/site-api/comments/project/{project_id}/add/"

    headers = {
        "x-csrftoken": SESSION_ID,
        "Cookie": f"scratchsessionsid={SESSION_ID}; scratchcsrftoken={SESSION_ID};",
        "referer": f"https://scratch.mit.edu/projects/{project_id}/",
        "user-agent": "charlie"
    }

    payload = {
        "content": comment_text,
        "parent_id": "",
        "commentee_id": ""
    }

    r = requests.post(url, json=payload, headers=headers)

    if r.status_code == 200:
        print("charlie did it:", comment_text)
    else:
        print("charlie sad:", r.status_code, r.text)


if __name__ == "__main__":
    print("charlie v1.1")

    project_id = input("id: ").strip()
    count = int(input("how many: ").strip())
    delay = float(input("seconds delay: ").strip())

    print("what the charlie do you wanna comment")
    print("leave blank for charlie timestamp mode\n")

    for i in range(count):
        comment_text = input(f"Comment #{i+1}: ").strip()

        if comment_text == "":
            comment_text = "charlie @ " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        post_comment(project_id, comment_text)

        if i < count - 1:
            print(f"waiting {delay} seconds for charlie…")
            time.sleep(delay)

    print("charlie has charlied")
