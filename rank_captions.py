from google import genai
import time

client = genai.Client(api_key="AIzaSyBgsBHalFqsEIedpRUBS1S__3zd2W0FrOs")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Hi!"
)

print(response.text, "\n")

#######################################
# Method 1: Prompt to rank captions #
# flavor: nar-rah-tiv

captions = '''
1. "Told boss I quit, still showed up."
2. "Adulting: when nap time becomes a luxury."
3. "Too nerdy? I call it 'future billionaire.'"
4. "Wallet so empty, even moths left."
5. "Posers be like, 'I totally read Dostoevsky.'"
6. "Swipe right: dating app or credit card?"
7. "Capitalism: where happiness is on layaway."
8. "Running a marathon? Nah, racing to last slice."
9. "Adulting: when bedtime is a social event."
10. "Being broke: ramen is the new caviar."
'''

prompt = "Please rank the following captions based on how funny they are. List just the captions, do not include quotation marks or numbers."

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"INSTRUCTION: {prompt} \n\n CAPTIONS: {captions}"
)

print(response.text, "\n")

timestamp = time.strftime("%Y%m%d_%H%M%S")
filename = f"Method1_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved to {filename}\n\n")


#######################################
# Method 2: Score each response #
# flavor: nar-rah-tiv

captions = '''
1. "Told boss I quit, still showed up."
2. "Adulting: when nap time becomes a luxury."
3. "Too nerdy? I call it 'future billionaire.'"
4. "Wallet so empty, even moths left."
5. "Posers be like, 'I totally read Dostoevsky.'"
6. "Swipe right: dating app or credit card?"
7. "Capitalism: where happiness is on layaway."
8. "Running a marathon? Nah, racing to last slice."
9. "Adulting: when bedtime is a social event."
10. "Being broke: ramen is the new caviar."
'''

prompt = "For each of the following captions, score how funny it is on a scale of 1 to 100. Save the response in JSON format, each entry should have a 'CAPTION' field and 'SCORE' field."

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"INSTRUCTION: {prompt} \n\n CAPTIONS: {captions}"
)

print(response.text)

timestamp = time.strftime("%Y%m%d_%H%M%S")
filename = f"Method2_Step1_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved to {filename}\n\n")

prompt = "Rank the CAPTIONS in this JSON based on their SCORE. List just the captions, do not include quotation marks or numbers."

ranked_response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"INSTRUCTION: {prompt} \n\n CAPTIONS: {response}"
)

print(ranked_response.text)

timestamp = time.strftime("%Y%m%d_%H%M%S")
filename = f"Method2_Step2_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(ranked_response.text)

print(f"Saved to {filename}\n\n")

