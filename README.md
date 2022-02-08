<h1 align ="center"> SAND-wich</h1>
<p align="center">
    <img src="Logo/SAND-wich_icon_720.png"/>
</p>
<br>
<p align="center"><em>NFTs are just pixelated sandwiches! <b>#ProveMeWrong</b></em></p>
<br>

## Overview

Have you ever seen NFT collections such as <a href ="https://opensea.io/collection/boredapeyachtclub">The Bored Ape Yacht Club</a> or <a href ="https://opensea.io/collection/cryptopunks">Cryptopunks</a> and wondered:
  
  ><em><h4>How these artists can mint their art so fast and so well organized without risking the quality in the process?! 🤔</h4></em> 
  
If you have, well, the short answer is by applying <a href ="https://www.lighthouselabs.ca/en/blog/how-python-is-used-in-automation">**Automation**</a> to their <a href="https://www.britannica.com/technology/standardization">**Standardized Artworks**</a>

Now, if you are wondering:
  
  ><em><h3>Oh nice! How do I do that? I'm just starting... 🤷‍♂️</h3></em> 

I'm glad to introduce **SAND-wich** 🥪 to you!
  
It's an open-source software built on Python that aims to help both new and well-experienced artists in the making of NFT collections.
  
It is capable of merging any number of layers following an specific order (provided by you), and export every single result to a folder as an independent file and also a dataframe that contains the NFTs metadata used in the process.
 
By using **SAND-wich**, you are making your work more productive and organized because of the nature of applying **Automation and Standarization** to your Art. 
🗿  

  - **Technology stack**: Python 3.9.6 [MSC v.1929 64 bit (AMD64)], Pandas 1.3.1, Itertools, PIL 8.4.0.
  - **Status**:  0.1.0
  - **Executable**: https://github.com/noahverner1995/SAND-wich/blob/main/exe/SAND-wich.exe
  - **What makes this software different from others?** The ease of use and the brand concept behind it.

## Installation

**If you are a developer**, you will first have to have installed `Python 3.9.6` or later with the following dependencies: `Pandas 1.3.1` or later, `Itertools`, `PIL 8.4.0` or later. Then you can copy the code from the `SAND-wich.py` file and run it in your preferred environment.
    
**If you ARE NOT a developer**, you will first have to deactivate your Antivirus for then <a href ="https://github.com/noahverner1995/SAND-wich/blob/main/exe/SAND-wich.exe">downloading the exe file</a>. Then you can execute the program by clicking on it and pressing ↵Enter.

## Usage

First of all, you need to make sure that you already have an ***Standardized NFT Model*** made with **Adobe Photoshop**, such as this one down below:

<p align="center">
    <img src="Sample/GIF/Sample_gif.gif"/>
</p>
<p align="center"><b>Download this Standardized NFT Model</b><a  href ="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Sample.psd"> <b>HERE 👀</b></a></p>
<br>

Then, you open that model using **Adobe Photoshop**, then select the `Zoom` 🔍 tool, then move your mouse over the icon in the center of your screen, and then hold down `Left-Click` until it's big enough, then you will see something like this:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/001.png"/>
</p>

All right, now you will create the following folders at your desired `path`:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/002.png"/>
</p>
<p align="center"><em>Make sure to name these folders with the same</em></p>
<p align="center"><em>name of the layer groups, respectively!</em></p>
<p align="center"><em><b>#KeepItOrganized</b></em></p>
<br>

Then, you will hide all the layers in the `.psd` except one, such as `Yellow` in this case:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/003.png"/>
</p>

Then, you will `export` as `.png`  that layer to the corresponding folder (`Background`, in this case) at the `path` you set:
<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/004.png"/>
</p>
<p align="center"><em>Again, make sure to name these files with the same</em></p>
<p align="center"><em>name of the layers, respectively!</em></p>
<p align="center"><em><b>#KeepItOrganized</b></em></p>
<br>

You will repeat the previous process with every single layer, individually. Once done, you will execute `SAND-wich.exe` by selecting it with `Left-Click` and pressing ↵Enter:
<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/005.png"/>
</p>
<p align="center"><em>Remember to have your antivirus deactivated when doing so</em></p>
<p align="center"><em>Otherwise, this won't work as expected. 🧐</em></p>

It will display the following program:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/006.png"/>
</p>

Now you will copy the `path` at where your exported layers are located:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/007.png"/>
</p>

And paste into the `SAND-wich.exe` input:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/008.png"/>
</p>

Then press ↵Enter:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/009.png"/>
</p>

`SAND-wich` will print first the name of the folders (in purple) together with its corresponding files (in light blue) from the `path` you passed as input, then it will print a dictionary (which is a data structure) that contains the all the previous information inside.

Then it will ask you if you want to add `'None'` as value in one or several folders (keys) of the dictionary, **this will be useful if you want to create an NFT collection with some series of images without a particular feature**.

If you don't want to do this, just type `n` and press ↵Enter.

Else, you type `y` and press ↵Enter, and then type the name of the folder (key) in which you want to add `'None'` as value and press ↵Enter, it will ask you again if you want to add another one or not, you decide from there.

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/010.png"/>
</p>

All right, this part explains why this project was named as `SAND-wich` (*sort of*). 😉
><em><h4>*A sanwdich 🥪 is an orderly sequence of elements, that usually starts and finishes with a slice of bread 🍞*.</h4></em>

Just like a sandwich, the creation of your NFTs must follow an specific order to be created, otherwise `SAND-wich` may export **abominations** 🧟. 

In this particular case, the order will be the following: **Background, Body_format, Colour, Extra**

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/011.png"/>
</p>
<p align="center"><em>Make sure to type each folder name right for then pressing ↵Enter. <b>Otherwhise, you will have to try again</b></em></p>

Once you have set the order, `SAND-wich` will print a message (in purple) confirming the order has been set, and then will print a dataframe that will contain the **NFTs Metadata**

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/012.png"/>
</p>

Then, it will ask you for a folder name, in this case it was chosen **'Sample'**:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/013.png"/>
</p>

And then ↵Enter was pressed:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/014.png"/>
</p>

Now, it will ask you for an **integer number** that will used for enlarging each one of the final pictures.

*ProTip: the reason for this is because when you work with **Pixel art**, it's better to make your layers in very low resolutions (usually a width and height less than 50p) **unless you are a Pro of course**, then what you do is to export the final result with a resolution several times bigger than the original one.* 

In case you just don't want to enlarge the final result, just type `1` as input and press ↵Enter, otherwise type a bigger integer number:
<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/015.png"/>
</p>

And press ↵Enter.

`SAND-wich` will now apply the <a href ="https://www.sciencedirect.com/topics/computer-science/cartesian-product">Cartesian Product</a>, and will export every single result and the dataframe to the folder `Sample` located at the initial `path` you had set:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/016.png"/>
</p>

Then, `SAND-wich` will say bye-bye and terminate itself after a few seconds.

Now, you will go back to the initial `path` you had set, you will see a folder new folder named **'Sample'**:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/017.png"/>
</p>

Then you will open that folder to see results and hooray! 🙌 IT'S DONE:

<p align="center">
    <img src="https://github.com/noahverner1995/SAND-wich/blob/main/Sample/Step%20by%20Step%20SCREENSHOTS/018.png"/>
</p>

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in <a href ="https://github.com/noahverner1995/SAND-wich/issues">this repository's Issue Tracker</a>. 

## Getting involved

You can follow us on our social networks to keep well informed about more developments like this one, and drop some 💓, 🔁, and 👏:

• Twitter 🐦: https://twitter.com/cryptobote
<br>
• Medium 📰: https://medium.com/@cryptobote

💚 **You can also support us by purchasing at least one NFT from <a href="https://opensea.io/noahverner?tab=created_collections">these collections</a>** 💚

## Credits and references

1. <a href ="https://www.youtube.com/watch?v=hvy9msjJdMs">Techmaker Workshop | How to Combine Images in Python with Pillow</a>
2. <a href ="https://medium.com/coinmonks/creating-generative-art-nfts-with-python-solidity-a95eaeea515e">Generative Art NFTs with Python and Solidity</a>
