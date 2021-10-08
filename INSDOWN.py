from tkinter import *
from PIL import Image, ImageTk
import instaloader
import tkinter.messagebox as tmsg


def story_window():
    def story_submit():
        username = user_var.get()
        password = pwd_var.get()
        username_interest = uint_var.get()
        statusvar.set("Downloading...")
        sbar.update()
        try:
            ins = instaloader.Instaloader()
            ins.login(username, password)
            profile = instaloader.Profile.from_username(ins.context, username=username_interest)
            ins.download_stories(userids=[profile.userid], filename_target='{}/stories'.format(profile.username))
            history("stories", username_interest)
        except:
            statusvar.set("Downloaded")
            tmsg.showinfo("Success", f"Check '{username_interest}/stories' folder to see the downloaded items")
            st.destroy()
    st = Toplevel()
    st.geometry("400x310")
    st.minsize(400, 310)
    st.maxsize(400, 310)
    st.title("Story Downloader")
    statusvar = StringVar()
    statusvar.set("Ready")
    user_var = StringVar()
    pwd_var = StringVar()
    uint_var = StringVar()
    Label(st, image=story).grid(row=0, column=2)
    Label(st, text="Username : ", font="Georgia 10 italic").grid(row=1)
    Label(st, text="Password : ", font="Georgia 10 italic").grid(row=2)
    Label(st, text="Username of your interest : ", font="Georgia 10 italic").grid(row=3)
    st.user = Entry(st, text=user_var, relief=SUNKEN)
    st.pwd = Entry(st, text=pwd_var, relief=SUNKEN,show="*")
    st.uint = Entry(st, text=uint_var, relief=SUNKEN)
    st.user.grid(row=1, column=2)
    st.pwd.grid(row=2, column=2)
    st.uint.grid(row=3, column=2)
    st.submit = Button(st, text="Submit", padx=15, relief=RAISED, bd=2, bg="light green", fg="black",
                       command=story_submit)
    st.submit.grid(row=4, column=2, pady=15)
    sbar = Label(st, textvariable=statusvar, bd=1, anchor="n", relief=SUNKEN)
    sbar.grid(row=6)

def post_window():
    def post_submit():
        username = user_var.get()
        password = pwd_var.get()
        link_var = link.get()
        statusvar.set("Downloading...")
        sbar.update()
        id = link_var.split("/")[4]
        try:
            ins = instaloader.Instaloader()
            ins.login(username, password)
            post = instaloader.Post.from_shortcode(ins.context, id)
            ins.download_post(post, target="Instagram Posts")
            history("post", link)
        except:
            statusvar.set("Downloaded")
            tmsg.showinfo("Success", f"Check 'Instagram Posts' for the downloaded items")
            st.destroy()

    st = Toplevel()
    st.geometry("400x310")
    st.minsize(400, 310)
    st.maxsize(400, 310)
    st.title("Post Downloader")
    statusvar = StringVar()
    statusvar.set("Ready")
    user_var = StringVar()
    pwd_var = StringVar()
    link = StringVar()
    Label(st, image=post).grid(row=0, column=2)
    Label(st, text="Username : ", font="Georgia 10 italic").grid(row=1)
    Label(st, text="Password : ", font="Georgia 10 italic").grid(row=2)
    Label(st, text="Enter link : ", font="Georgia 10 italic").grid(row=3)
    st.user = Entry(st, text=user_var, relief=RAISED,bd=2)
    st.pwd = Entry(st, text=pwd_var, relief=RAISED,show="*",bd=2)
    st.link = Entry(st, text=link, relief=RAISED,bd=2)
    st.user.grid(row=1, column=2)
    st.pwd.grid(row=2, column=2)
    st.link.grid(row=3, column=2)
    st.submit = Button(st, text="Submit", padx=15, relief=RAISED, bd=2, bg="light green", fg="black",
                       command=post_submit)
    st.submit.grid(row=4, column=2, pady=15)
    sbar = Label(st, textvariable=statusvar, bd=1, anchor="n", relief=SUNKEN)
    sbar.grid(row=6)
    st.grab_set()

def profile_window():
    def profile_submit():
        username = user_var.get()
        password = pwd_var.get()
        user_int_var = username_interest.get()
        statusvar.set("Downloading...")
        sbar.update()
        try:
            ins = instaloader.Instaloader()
            ins.login(username, password)
            ins.download_profile(user_int_var)
            history("profile", user_int_var)
        except:
            statusvar.set("Downloaded")
            tmsg.showinfo("Success", "Downloaded successfully")
            st.destroy()

    st = Toplevel()
    st.geometry("400x310")
    st.minsize(400, 310)
    st.maxsize(400, 310)
    st.title("Profile Downloader")
    statusvar = StringVar()
    statusvar.set("Ready")
    user_var = StringVar()
    pwd_var = StringVar()
    username_interest = StringVar()
    Label(st, image=profile).grid(row=0, column=2)
    Label(st, text="Username : ", font="Georgia 10 italic").grid(row=1)
    Label(st, text="Password : ", font="Georgia 10 italic").grid(row=2)
    Label(st, text="Username of your interest : ", font="Georgia 10 italic").grid(row=3)
    st.user = Entry(st, text=user_var, relief=SUNKEN)
    st.pwd = Entry(st, text=pwd_var, relief=SUNKEN,show="*")
    st.user_int = Entry(st, text=username_interest, relief=SUNKEN)
    st.user.grid(row=1, column=2)
    st.pwd.grid(row=2, column=2)
    st.user_int.grid(row=3, column=2)
    st.submit = Button(st, text="Submit", padx=15, relief=RAISED, bd=2, bg="light green", fg="black",
                       command=profile_submit)
    st.submit.grid(row=4, column=2, pady=15)
    sbar = Label(st, textvariable=statusvar, bd=1, anchor="n", relief=SUNKEN)
    sbar.grid(row=6)


def highlights_window():
    def highlights_submit():
        username = user_var.get()
        password = pwd_var.get()
        user_int_var = username_interest.get()
        statusvar.set("Downloading...")
        sbar.update()
        ins = instaloader.Instaloader()
        ins.login(username, password)
        profile = instaloader.Profile.from_username(ins.context, user_int_var)
        for highlight in ins.get_highlights(user=profile):
            for item in highlight.get_items():
                ins.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
        history("highlights", user_int_var)
        statusvar.set("Downloaded")
        tmsg.showinfo("Success", "Downloaded successfully")

    st = Toplevel()
    st.geometry("400x310")
    st.minsize(400, 310)
    st.maxsize(400, 310)
    st.title("Highlights Downloader")
    statusvar = StringVar()
    statusvar.set("Ready")
    user_var = StringVar()
    pwd_var = StringVar()
    username_interest = StringVar()
    Label(st, image=highlights).grid(row=0, column=2)
    Label(st, text="Username : ", font="Georgia 10 italic").grid(row=1)
    Label(st, text="Password : ", font="Georgia 10 italic").grid(row=2)
    Label(st, text="Username of your interest : ", font="Georgia 10 italic").grid(row=3)
    st.user = Entry(st, text=user_var, relief=SUNKEN)
    st.pwd = Entry(st, text=pwd_var, relief=SUNKEN,show="*")
    st.user_int = Entry(st, text=username_interest, relief=SUNKEN)
    st.user.grid(row=1, column=2)
    st.pwd.grid(row=2, column=2)
    st.user_int.grid(row=3, column=2)
    st.submit = Button(st, text="Submit", padx=15, relief=RAISED, bd=2, bg="light green", fg="black",
                       command=highlights_submit)
    st.submit.grid(row=4, column=2, pady=15)
    sbar = Label(st, textvariable=statusvar, bd=1, anchor="n", relief=SUNKEN)
    sbar.grid(row=6)


root = Tk()
root.title("Instagram Downloader")
root.geometry("750x400")
root.minsize(750,400)
root.maxsize(750,400)
root.config(bg="white")
root.wm_iconbitmap("LOGO(2).ico")
img = Image.open("LOGO (2).png")
img = img.resize((150, 150), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

img1 = Image.open("Post.JPG")
img1 = img1.resize((150, 160), Image.ANTIALIAS)
post = ImageTk.PhotoImage(img1)

img2 = Image.open("Story.JPG")
img2 = img2.resize((150, 160), Image.ANTIALIAS)
story = ImageTk.PhotoImage(img2)

img3 = Image.open("Profile.JPG")
img3 = img3.resize((150, 160), Image.ANTIALIAS)
profile = ImageTk.PhotoImage(img3)

img4 = Image.open("Highlights.JPG")
img4 = img4.resize((150, 160), Image.ANTIALIAS)
highlights = ImageTk.PhotoImage(img4)

f = Frame(root, bg="white")
Label(f, text="Downloader", font=("Biting My Nails", 20), bg="white").grid(row=0, column=4, padx=15)
Label(f, image=photo).grid(row=0, column=3, padx=15)
f.grid(row=0)

f1 = Frame(root, bg="white")
Button(f1, text="Post", image=post, compound=TOP, bg="white", command=post_window, font="Georgia",relief=RAISED,bd=4).grid(
    row=1, column=0,
    pady=14, padx=0)
f1.grid(row=1)

Button(f1, text="Story", image=story, compound=TOP, bg="white", command=story_window, font="Georgia",relief=RAISED,bd=4).grid(row=1,
                                                                                                           column=3,
                                                                                                           pady=14,
                                                                                                           padx=34)

Button(f1, text="Profile", image=profile, compound=TOP, bg="white", command=profile_window, font="Georgia",relief=RAISED,bd=4).grid(row=1,
                                                                                                                 column=5,
                                                                                                                 pady=14,
                                                                                                                 padx=0)

Button(f1, text="Highlights", image=highlights, compound=TOP, bg="white", command=highlights_window,
       font="Georgia",relief=RAISED,bd=4).grid(row=1, column=7, pady=14, padx=24)
root.mainloop()
