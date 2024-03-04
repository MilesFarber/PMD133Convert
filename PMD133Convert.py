#Import the libraries
from PIL import Image #If PIL stops existing this program stops existing lmfao
import math
import os

script_directory = os.path.dirname(__file__) #Get script path
print("The script is in", script_directory) #DEBUG

inputfolder = "Input"
if not os.path.exists(inputfolder): #If it doesn't exist
    print("The Input folder does not exist. The program will now create a new one so you can put PNG files in it and then immediately Kermit Sudoku.")
    os.makedirs(inputfolder) #Create output folder
    133742069 / 0
outputfolder = "Output" #Output folder name
if not os.path.exists(outputfolder): #If it doesn't exist
    os.makedirs(outputfolder) #Create output folder
tempfolder = "Temp" #Temp folder name
if not os.path.exists(tempfolder): #If it doesn't exist
    os.makedirs(tempfolder) #Create temp folder

item_sprite_size = (16, 16) #ALL Item Sprites must be 16x16, no exceptions.

palettes = [
    [(0, 127, 151), (0, 0, 0), (191, 119, 39), (223, 175, 103), (255, 231, 159), (167, 0, 23), (255, 0, 31), (255, 135, 175), (0, 103, 183), (31, 159, 231), (143, 223, 255), (127, 143, 151), (159, 175, 183), (191, 199, 207), (223, 231, 231), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (191, 119, 39), (223, 175, 103), (255, 231, 159), (199, 87, 199), (255, 143, 255), (255, 207, 255), (119, 63, 0), (167, 95, 31), (223, 119, 31), (39, 135, 0), (95, 183, 39), (127, 223, 87), (183, 255, 143), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (87, 47, 159), (143, 103, 191), (183, 151, 223), (207, 151, 0), (247, 231, 0), (255, 255, 167), (55, 63, 143), (79, 95, 151), (103, 135, 175), (71, 103, 111), (127, 143, 151), (175, 183, 191), (215, 223, 223), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (159, 0, 0), (215, 63, 0), (255, 135, 95), (0, 135, 135), (55, 191, 247), (119, 255, 255), (159, 95, 0), (207, 159, 0), (255, 247, 0), (39, 135, 0), (95, 183, 39), (127, 223, 87), (215, 239, 167), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (0, 87, 199), (0, 143, 255), (63, 207, 255), (0, 87, 199), (0, 143, 255), (63, 207, 255), (231, 63, 103), (255, 143, 175), (255, 199, 215), (159, 0, 0), (215, 63, 0), (255, 135, 95), (255, 199, 175), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (0, 111, 7), (0, 167, 63), (63, 231, 127), (23, 167, 87), (79, 223, 143), (143, 255, 207), (87, 103, 183), (135, 159, 255), (183, 207, 255), (119, 63, 0), (167, 111, 0), (223, 183, 0), (255, 247, 0), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (159, 95, 0), (207, 159, 0), (255, 247, 0), (0, 175, 0), (0, 255, 0), (127, 255, 127), (159, 0, 0), (215, 63, 0), (255, 135, 95), (0, 63, 175), (39, 135, 215), (71, 199, 255), (167, 239, 255), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (87, 0, 159), (143, 0, 215), (223, 79, 255), (191, 87, 0), (255, 151, 0), (255, 207, 55), (135, 63, 135), (175, 111, 183), (215, 151, 223), (39, 95, 199), (87, 167, 231), (127, 231, 255), (183, 255, 255), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (0, 87, 199), (0, 143, 255), (63, 207, 255), (103, 183, 0), (175, 255, 0), (247, 255, 119), (191, 119, 39), (223, 175, 103), (255, 231, 159), (87, 0, 159), (143, 0, 215), (183, 79, 255), (207, 167, 255), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (0, 135, 135), (55, 191, 247), (119, 255, 255), (0, 111, 7), (0, 167, 63), (63, 231, 127), (119, 63, 0), (223, 119, 31), (255, 151, 71), (191, 143, 0), (223, 199, 0), (255, 247, 0), (255, 255, 127), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (159, 0, 0), (215, 63, 0), (255, 135, 95), (79, 95, 111), (103, 135, 159), (183, 199, 207), (39, 135, 0), (95, 199, 55), (143, 255, 103), (7, 47, 71), (79, 111, 127), (151, 175, 183), (223, 239, 239), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (159, 95, 0), (207, 159, 0), (255, 247, 0), (135, 23, 0), (191, 79, 0), (255, 143, 63), (127, 143, 151), (175, 183, 191), (215, 223, 223), (0, 0, 0), (39, 47, 47), (79, 87, 87), (143, 151, 143), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (0, 87, 199), (0, 143, 255), (63, 207, 255), (0, 0, 143), (0, 0, 199), (119, 119, 255), (95, 167, 231), (143, 223, 255), (199, 239, 255), (95, 47, 0), (151, 87, 15), (199, 119, 31), (231, 191, 143), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (231, 63, 103), (255, 143, 175), (255, 199, 215), (87, 0, 159), (143, 0, 215), (223, 79, 255), (215, 167, 0), (231, 199, 0), (255, 247, 0), (143, 0, 215), (183, 79, 255), (207, 167, 255), (231, 215, 255), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (87, 0, 159), (143, 0, 215), (223, 79, 255), (159, 0, 183), (215, 0, 239), (255, 127, 255), (191, 87, 0), (255, 151, 0), (255, 207, 55), (39, 143, 223), (71, 199, 255), (127, 231, 255), (183, 255, 255), (255, 255, 255)],
    [(0, 127, 151), (0, 0, 0), (39, 135, 0), (95, 199, 55), (143, 255, 103), (167, 0, 63), (255, 0, 151), (255, 127, 255), (175, 183, 191), (215, 223, 223), (255, 255, 255), (175, 63, 0), (215, 127, 0), (255, 183, 0), (255, 223, 127), (255, 255, 255)]
] #Define the 16 palettes of 16 colors each as a list of lists of RGB tuples. This uses the extracted, unmodified palette from Capypara

def ecd(sprite1, sprite2): #Define a function to calculate the Euclidean Color Distance between two sprites
    pixels1 = sprite1.load() #Get the pixel data of sprite 1
    pixels2 = sprite2.load() #Get the pixel data of sprite 2
    dist = 0 #Initialize distance
    for x in range(16): #Loop through each horizontal pixel
        for y in range(16): #Loop through each vertical pixel
            r1, g1, b1 = pixels1[x, y] #Get the RGB values of each pixel in sprite 1
            r2, g2, b2 = pixels2[x, y] #Get the RGB values of each pixel in sprite 2
            dr = (r1 - r2) ** 2 #Calculate the squared difference of the red channel
            dg = (g1 - g2) ** 2 #Calculate the squared difference of the green channel
            db = (b1 - b2) ** 2 #Calculate the squared difference of the Miles channel  
            dist += dr + dg + db #Add the squared differences to the distance
    return dist #Return distance

files = os.listdir(inputfolder) #Get a list of all files in the current directory
png_files = [file for file in files if file.endswith('.png')] #Filter the list for only PNG files

for png_file in png_files: #Miles's Illusion! This whole time the entire program was literally just a giant loop for each PNG file in the same folder as the python script, get heckin bamboozled.
        png_file_path = os.path.join(script_directory, "Input\\", png_file) #Fix Image.open path bug
        png_file_basename, png_file_extension = os.path.splitext(png_file) #Prep the filename for saving in the output
        png_file_rgba = Image.open(png_file_path).convert("RGBA") #Load the PNG file as an image object and convert to RGBA
        width, height = png_file_rgba.size #Calculate dimensions
        if width != 16 or height != 16: #If dimensions are NOT 16x16
            png_file_rgba = png_file_rgba.resize((16, 16), Image.LANCZOS)
        png_file_rgb = Image.new("RGB", png_file_rgba.size, (0, 127, 151)) #Create a new RGB image with the background color
        png_file_rgb.paste(png_file_rgba, mask=png_file_rgba.split()[3]) #Paste the RGBA image over the background, using the alpha channel as mask, effectively turning it into RGB
        
        for i, palette in enumerate(palettes): #Loop through the palettes
            temp_file = Image.new("P", png_file_rgb.size, 0) #Create a new image with the same size as the RGB image, but indexed
            temp_file.putpalette(sum(palette, ())) #Set the palette of the indexed image
            temp_file.paste(png_file_rgb.convert("RGB").quantize(palette=temp_file, dither=Image.NONE)) #Convert the RGB image to the indexed image using the nearest color, without dithering. It took me like one week to find out this existed wtf
            temp_file.save(os.path.join(tempfolder, f"{png_file_basename}.SubPalette{i}.png")) #Save the indexed image with a different name

        min_distance = math.inf #Initialize minimum distance
        best_subpalette = None #Initialize best palette
        temp_files = os.listdir("temp") #Get the list of temp files
        for temp_file in temp_files: #Loop through each temp file
            temp_png = Image.open("temp/" + temp_file) #Open the temp file
            temp_png = temp_png.convert("RGB") #Convert it to RGB mode
            distance = ecd(png_file_rgb, temp_png) #Calculate the distance between the original file and the temp file.
            if distance < min_distance: #If the distance is smoler
                min_distance = distance #Update minimum distance
                best_subpalette = temp_file #Update best palette

        print("The best subpalette for", png_file ,"is", best_subpalette) #Print the best palette and the minimum distance
        print("Euclidean Color Distance:", min_distance, "Photons")
        item_sprite = Image.open(f"temp/{best_subpalette}") #Prep the best file to convert it to an item sprite, here we go

        if item_sprite.mode == "P": #Double check if the image mode is P (palette)
            for i, palette in enumerate(palettes): #Loop through the palettes
                item_sprite = Image.open(f"temp/{best_subpalette}") #Reopen the file again to reset
                item_sprite.putpalette(sum(palette, ())) #Apply the next palette to the image
                img_palette = item_sprite.getpalette() #Get palette information
                transparency = item_sprite.info.get("transparency", None) #Get transparency information
                img_palette[0:3] = [0, 127, 151] #Force the first color to be 0, 127, 151
                transparency = 0 #Set the first color in the palette to be transparent
                item_sprite.putpalette(img_palette) #Put the modified palette back into the image
                item_sprite.info["transparency"] = transparency #Put the modified transparency back into the image
                item_sprite.save(os.path.join(outputfolder, f"{png_file_basename}.Palette{i}.png"), format="PNG", optimize=True) #Save the image with each optimized palette
            print("New Item Sprites created:",png_file_basename)
        else:
            print("For some reason", best_subpalette ,"magically turned from an indexed PNG into a 24 bit RGB PNG while doing Euclidean Color Distance calculation, go screm at MilesFarber on github.")

input("Your new Item Sprites are in the Output folder! Press Enter to close the program.") #Pause