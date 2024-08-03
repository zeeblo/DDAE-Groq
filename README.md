This is an altered version of the [Doki Doki AI Edition](https://github.com/doki-doki-ai-edition/Mod) that uses [Groq](https://console.groq.com/docs/quickstart)--which as of writing this is completely free to use.

If Groq ever requires a paid sub then this repo will be archived or deleted to comply with Team Salvato's IP Guidelines.




## Groq

**Overview:** Groq is an API that let's you run a few open sourced models such as llama3, mixtral, mistral  etc. at amazing speeds. 

**Let's start**

- Go to https://console.groq.com/login
- Signup with your whichever account you want
- Go to https://console.groq.com/keys
- Click "Create API Key"
- Copy the key **and make sure you save it somewhere**

In DDAE click on settings and make sure "AI Type" is set to "API"

<img style="width: 180px;" src="https://i.imgur.com/jXbFL0d.png" alt="ai type">

Next click on "Model Names" and select any model you want.

<img style="width: 280px;" src="https://i.imgur.com/c0wjlPh.png" alt="model names">

Go back to the main settings and select "API Key"

<img style="width: 580px;" src="https://i.imgur.com/0AmMdUk.png" alt="ddlc api key">


Paste in the API key you copied from earlier

<img style="width: 480px;" src="https://i.imgur.com/pneebBb.png" alt="ddlc-token">

### You're done!

---

Doki Doki AI Edition (DDAE) is a DDLC mod that implements a more interactive form of roleplay by using sprites to spice up the AI generated text.
The sprites used are decided by the AI based on how you interact with it.

If you have extra questions or want to become apart of the community you can join the discord server here: https://discord.gg/rDA7ehBSq7

If you've been **banned** from the server you can appeal here: https://forms.gle/E8wyDi9aBzXdWvf99


# Setup

**video tutorial:** https://www.youtube.com/watch?v=VXvidFabia8

- Make sure you have a fresh install of DDLC https://ddlc.moe/
- Download the latest version of the DDAE mod on this github page https://github.com/doki-doki-ai-edition/Mod/releases

To setup the mod just drag the contents into the main ddlc folder:


<video controls>
  <source src="game/assets/imgs/help_page/ddae setup.mp4" type="video/mp4" />
</video>



## Ollama

**Overview:** Ollama is an open-source project that allows people to setup local language models on their machine in a far more user friendly way. They have both uncensored and censored models and the models are quantized (compressed) to run on low-end devices.


**Let's Start!**
- Go to https://ollama.com/download
- Select the Operating system you're using (For example Windows)
- Click on Download

Once it's downloaded, run the application.

If you're on windows you should see a small icon in your taskbar that looks like this

<img src="game/assets/imgs/help_page/llama_task.png">

- Open up a terminal on your device (eg. cmd+r if you're using windows, then type "cmd" and press enter)
- In the terminal type "ollama pull llama3" (or any model you find in https://ollama.com/library/)

This should be roughly 4.7 gigabytes and once it's done installing you can run the mod!



# Frequently Asked Questions

## Are my chats private?

Yes. Your chats are completely localized on your machine, even if you turn your internet off, it'll still work.


## Does this use chatgpt?

No. No paid APIs are used in the mod.

## Will it delete my files

No. The fangame in the video is different from the mod and it doesn't have the ability to execute code on your machine. I also don't plan on doing this, since that's basically just malware.

## Why does it take forever to load?

2 Main reasons for this.
1. An error happened and you should check your `log.txt` file in the main folder and send it in #support
2. Hardware limitation. If you don't have a good enough device then it's going to take a while to respond.

## Are the models uncensored

It depends on what model you're using. You can go to https://ollama.com/library to find uncensored models but they may not follow the system prompt as well which would cause the game to not function correctly.

Secondly, they may not be entirely uncensored. There are certain questions that it may refuse, but since it's a local model you can attempt to jailbreak it as much as you want.


## Can I trust Ollama?

As much as you trust all the other apps you use daily.
Jeffrey Morgan is one of the founders and he has a credible background by previously working for docker, twitter and google.

The project is also used by google in firebase https://firebase.google.com/docs/genkit/plugins/ollama

And obviously, the project is open-sourced.


## Why do the models sometime return "ERROR"?

This happens when the model doesn't respond with the instructed format. This typically happens on regular models if you say something too provacative. 

There's a few solutions to this.

The first is to use an uncensored model. 

The second thing you could try is continuing the chat by ignoring the error message and try to force the ai back into a roleplay state

And the 3rd thing you could try is just jailbreaking the ai model by editing the
system prompt to make the ai say anything.



## What hardware do I need?

You should be able to run the mod on low-end devices like a laptop with 4GB of RAM
and 4GB of VRAM but the speed at which you get a response is going to be slow.

If you want faster responses you need more VRAM. Regular RAM allows you to run models.



## I keep getting this error

<img src="game/assets/imgs/help_page/traceback.png" alt="traceback error">

When in doubt, restart.

This typically means the model didn't properly generate a background when you first loaded the game.
To fix this you can completely close the game and try loading a new one.

You could also edit the chat file for the old world and try loading it again.




# Credits

**Developer:**
[Zeeblo](https://github.com/zeeblo)

**Logo Design:**
[Infernog](https://x.com/Infernog05) (& another user who wishes to stay anonymous)

**Voice Acting:**
[Jayce Parisi](https://jayceparisi.com/) (**Note:** Jayce would not be comfortable w/ their voice being AI generated so keep that in mind if you're making a submod) 


## Special thanks

- Thanks to Retronika & iiTzWolfyy for the Character template gui & script used when a user first creates a realm
- sutemo for the male sprites https://sutemo.itch.io/male-character-sprite-for-visual-novel
- midjorney generated render of Monika (used in the only CG scene in the game)