# 🎉 Genshin Impact Auto Daily Check-in
Automatic claim Genshin Impact reward everyday from Mihoyo server

## ⏰ How to Use (Automatic)

**1.** `Fork` this git to your github account

   ![Fork](https://user-images.githubusercontent.com/36266025/114557579-051fe000-9c94-11eb-9941-64a1de592cfc.png)

**2.** Copy cookie account from Mihoyo Website

* For PC
    * Go to [Mihoyo Daily Check-in](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481), then login

    * Press `F12`, then select '>>' logo and select `Console`

    * Then type `copy(document.cookie)` in console
 
      ![Cookie](https://user-images.githubusercontent.com/36266025/114557672-18cb4680-9c94-11eb-867f-d3eee4f1f4a6.png)

* For Android
   * Download App name [F12 - Inspect Element](https://play.google.com/store/apps/details?id=com.asfmapps.f12)

   * Copy [Mihoyo Daily Check-in](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481) URL, then paste into `App URL` and enter

     ![URL](https://user-images.githubusercontent.com/36266025/114560843-3f3eb100-9c97-11eb-9833-52a7baf35e58.png)

   * After website loaded, login with your GI account

   * Tap on `F12` logo, tap `Console`, then type `console.log(document.cookie)`, enter

     ![Console](https://user-images.githubusercontent.com/36266025/114560167-a019b980-9c96-11eb-9c67-084e4f014ea0.png)

   * Copy your cookie, for example like this pic below

     ![Cookie](https://user-images.githubusercontent.com/36266025/114560963-58dff880-9c97-11eb-9ebe-a64126e552d7.png)


**3.** Go to your forked git, select `Settings`

   ![Settings](https://user-images.githubusercontent.com/36266025/114557766-30a2ca80-9c94-11eb-9dd4-ab0365d08d0c.png)

**4.** Select `Secret`, then `New repository secrets`

   ![Secrets](https://user-images.githubusercontent.com/36266025/114557805-3dbfb980-9c94-11eb-8f33-1217d4fa28f0.png)

**5.** At `Name` write **COOKIE**, and `Value` write that copied Cookie, then click `Add Secret` button. Carefully it's case sensitive

   ![Cookie](https://user-images.githubusercontent.com/36266025/114557856-4dd79900-9c94-11eb-90fc-f3650196f70e.png)

**5A.** If you had multiple account, repeat guide `2` for copying another account cookie, just logged in with another different account, paste with newline

   ![Multi Cookie](https://user-images.githubusercontent.com/36266025/114557928-5e880f00-9c94-11eb-8061-bde23f50b783.png)

**6.** Enable your github actions

- First, go to `Actions`, then click green button that said `I understand my workflows...`
   ![Actions](https://user-images.githubusercontent.com/36266025/114813785-0577c280-9ddd-11eb-9906-7325f28d8256.png)

- Then click `genshinDaily` at Workflows, and click `Enable workflow` button
   ![Workflow](https://user-images.githubusercontent.com/36266025/114813871-2dffbc80-9ddd-11eb-8933-639559400bb3.png)

**7.** Wait for next day, check your github Actions, Profit 😎

   ![Result](https://user-images.githubusercontent.com/36266025/114557989-6ba4fe00-9c94-11eb-85ff-9ef0bbafc68e.png)



## 🔔 Telegram Notification Integration

**1.** Create a bot from [@BotFather](https://t.me/BotFather)

* Write `/newbot`
* Write your bot name, ex: `Ayra GI Notifications`
* Write your bot username, ex: `BotFather`

   ![Bot](https://user-images.githubusercontent.com/36266025/114558041-795a8380-9c94-11eb-8d1c-3af246a37bbd.png)

* Copy bot token from there
* Go to your new bot, click `Start` to enable notification

**2.** Go to `Settings` > `Secrets` > `New repository secrets`

**3** Write
* Name: `TG_BOT_TOKEN`
* Value: `Your bot token before`

**4** Go to [@FeliciaHikariBot](https://t.me/FeliciaHikariBot), click `Start` and type `/id`. Then write below in `Secrets` like before
* Name: `OWNER_ID`
* Value: `Your user id before`

   ![Example](https://user-images.githubusercontent.com/36266025/114558092-87100900-9c94-11eb-9e9e-b8d4271235a9.png)


**5.** Save and wait for next day!


## ⚠️ WARNING
* I don't take responsibly if your account got something wrong, the script only access on [Mihoyo](https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481) website only to check, and claim reward. This script may illegal for fair-play purposes, so take you own risk!
