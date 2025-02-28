import discord
import PyPDF2

pdf_file = open('CSB_Pew_Bible_2nd_Printing.pdf', 'rb') # Extract the text from the PDF and store the words in a set

pdf_reader = PyPDF2.PdfReader(pdf_file) # Create a PDF reader object

num_pages = len(pdf_reader.pages) # Get the number of pages

holy_words = set() # Create a set to store the words

# Loop through each page and extract the text
for page in pdf_reader.pages:
    page_text = page.extract_text()
    page_words = page_text.split()
    holy_words.update(page_words) 

pdf_file.close()



class Client(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
        print(holy_words)
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("hello"):
            await message.channel.send(f"Hello, {message.author}")
        
        if not any(word in message.content for word in holy_words):
            await message.channel.send("You are not holy!")


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run("token")