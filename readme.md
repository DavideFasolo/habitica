# Genmon Habitica Computer Time Rewards  
  
### _This readme is work in progress._  
  
This is an ensemble of scripts, written in python with the purpose of helping myself to keep track and regulate my time at computer.  
  
It's written for XFCE4-panel, and work in genmon plugin.  
  
To make it works you need to follow these steps:

  

### install:
 - Clone the repo to your ~/scripts directory, to have the `~/scripts/habitica` path  
 - Create a text file to replace the one named `credenzialihabitica`; content of file have to be these lines:
	1. your Habitica api user-id
	2. your Habitica api user-key  
 - Encrypt `credenzialihabitica` using gpg  
 - Add two genmon to your xfce4-panel with no label, and put these command to execute:  
    Genmon 1: `python ~/scripts/habitica/timer.py`
    Genmon 2: `python ~/scripts/habitica/goldmon.py`
 
### customizations:  
I wrote these scripts with my system in mind, so i'm thinking about some config-file to make customization easier, but until now, you can edit "goldmon_click.py" file:  
  
- Edit the list of purchasable items:   Look at the voices list, and add/delete/edit existing ones with this syntax:

  	setmenuvoice("Name of the reward", minutes, price)
  |[a]()
  
- Edit title of purchasable items popup:

	Look at the `set_titolo` function and edit the first argument like this:   `set_titolo("yourtitle", popup_menu)`

- Edit the abort voice of the popup menu:

	Look for `btn_z` definition, and edit the `create_button` third argument:   `{ "nome": "abort_text" }`
