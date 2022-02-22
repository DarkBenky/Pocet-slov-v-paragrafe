text = """
Here's a llama,
llama, llama,
Cheesecake llama,
Tablet, brick, potato,
llama,
llama, llama,
Mushroom llama,
llama, llama,
Duck,

I was once a treehouse
I lived in a cake
But I never saw the way
The orange slayed the rake
I was only three years dead
But it told a tale
And now listen, little child
To the safety rail

Did you ever see a llama
Kiss a llama
On the llama
llama's llama
Tastes of llama
llama llama
Duck

Half a llama
Twice the llama
Not a llama
Farmer llama
llama in a car
Alarm a llama
llama Duck

Is this how it's told now?
Is it all so old?
Is it made of lemon juice?
Doorknob, ankle, cold
Now my song is getting thin
I've run out of luck
Time for me to retire now
And become a duck

        """
text = text.lower()
text_array = []
veta = ""
odsek = 0
odsek_o = ""
veta2 = ""
d = 0
p = 0
for letter in text:
    veta += letter
    if letter == "\n":
        odsek_o += veta
        d = len(veta)
        d = int(d)
        if d > 1:
            d -= 1
            veta2 = " " * d
        veta2 += "\n"
                
        if veta == veta2:
            p += 1
            text_array.append(odsek_o)
            odsek_o = ""
        veta = ""
        veta2 = ""
        
lama = []
llama = ""
Duck = ""
pocet = 0
pocet1 = 0
for odsek in text_array:
    for i in odsek:
        lama.append(i)
        if len(lama) > 5:
            llama += lama[0] + lama[1] + lama[2] + lama[3] + lama[4]
            Duck += lama[0] + lama [1] + lama [2] + lama [3]
            lama.pop(0)
            if llama == "llama":
                pocet += 1
            if Duck == "duck":
                pocet1 += 1
            Duck = ""   
            llama = ""        
    print (pocet , " LLama") 
    print (pocet1 , " duck")
    pocet = 0 
    pocet1 = 0
