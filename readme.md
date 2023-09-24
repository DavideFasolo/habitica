# Genmon Habitica Computer Time Rewards
---
  
### _This readme is a work in progress._
---
This is an ensemble of scripts, written in python with the purpose of helping myself to keep track and regulate my time at computer.
It's written for [XFCE4-panel](https://docs.xfce.org/xfce/xfce4-panel/start), and work with [genmon](https://docs.xfce.org/panel-plugins/xfce4-genmon-plugin/start) plugin and [gnupg](https://www.gnupg.org/).

To make it works you need to follow these steps:
### Requirements
I'm running on [Garuda Raptor](https://garudalinux.org/) (Arch-based), using [i3wm](https://i3wm.org/) and xfce4-panel.

[XFCE4-panel](https://docs.xfce.org/xfce/xfce4-panel/start)

[genmon plugin](https://docs.xfce.org/panel-plugins/xfce4-genmon-plugin/start)

[gnupg](https://www.gnupg.org/)

[python 3.11](https://www.python.org/)

[python-screeninfo](https://github.com/rr-/screeninfo)

[python-pynput](https://github.com/moses-palmer/pynput)

[python-gnupg](https://github.com/vsajip/python-gnupg/)


### install
 - Clone the repo to your ~/scripts directory, to have the `~/scripts/habitica` path  
 - Create a text file to replace the one named `credenzialihabitica`; content of file have to be these lines:
	```python
	your habitica api user id
	your habitica api key
	```

	you can find Habitica api keys [here](https://habitica.com/user/settings/api)
 - Encrypt [`credenzialihabitica`](/credenzialihabitica) using gpg  
 - Add two genmon to your xfce4-panel with no label, and put these command to execute:
   
	Genmon 1 (left): `python ~/scripts/habitica/timer.py`

	Genmon 2 (right): `python ~/scripts/habitica/goldmon.py`
 
### customizations
I wrote these scripts with my system in mind, so i'm thinking about some config-file to make customization easier, but until now, you can edit "goldmon_click.py" file:  
  
- #### Edit the list of purchasable items:

	Edit [`goldmon_click.py`](/goldmon_click.py), look at the voices list, and add/delete/edit existing ones with this syntax:

  	`setmenuvoice("Name of the reward", minutes, price)`

	Here's an example:
	```python
	voices = [
 		setmenuvoice("Fooling around", 60, 5),
 		setmenuvoice("Not-so-fooling around", 60, 0.5),
  		setmenuvoice("Gaming", 60, 4),
 		setmenuvoice("TV serial or short film", 60, 4),
 		setmenuvoice("One entire film", 240, 5)
	]
	```
  
- #### Edit title of purchasable items popup:

	Look at the `set_titolo` function and edit the first argument like this:

	`set_titolo("yourtitle", popup_menu)`

- #### Edit the abort voice of the popup menu:

	Look for `btn_z` definition, and edit the `create_button` third argument:

	`{ "nome": "abort_text" }`

	Here's an example:
	```python
	btn_z = create_button(
	                  popup_menu
	                , root
	                , { "nome": "nevermind" } #here's the text
	                , "12"            # font size
	                , "#4E8392"       # fg color
	                , "#141414"       # bg color
	                , "#5B9631"       # active fg color
	                , "#141414"       # inactive fg color
	                )
 	```
 	Same text formatting arguments apply to all menu voices in the `btn_x` call, in the same file.
  	Other future format customizations will be in [`environment.py`](/pyres/environment.py)
### Testing
I'm not so skilled in test-making, i tried my best. If you want to test in your system, you have to replace the gpg public key in the [`gen_test.py`](/tests/gen_test.py):
```python
def get_public_key():
    return 'A0FCB5A27C1ED66B5BC6D030862A9198690C1B67' # replace with your gpg public key
```
### Screenshots

running timer:

![a](/images/genmoninpanel.png)

timeout:

![a](/images/timeout.png)

popup:

![a](/images/popup.png)
