#fast api
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates #UI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI(title="Text Summarizer App",description="Text Summarization using T5",version="1.0")

#load model and tokenizer
model=T5ForConditionalGeneration.from_pretrained("./saved_summary_model/saved_summary_model")
tokenizer=T5Tokenizer.from_pretrained("./saved_summary_model/saved_summary_model")

#device
if torch.backends.mps.is_available():
    device=torch.device("mps")
elif torch.cuda.is_available():
    device=torch.device("cuda")
else:
    device=torch.device("cpu")

model.to(device)

#templating
templates=Jinja2Templates(directory=".")
#input schema for dialouge
class DialougeInput(BaseModel):
    dialouge: str

#clean data
def clean_data(text):
    text=re.sub(r"\r\n"," ",text) #replacing lines
    text=re.sub(r"\s+"," ",text) #remove extra subspaces
    text=re.sub(r"<.*?>"," ",text) # remove html tags
    text=text.strip().lower()
    return text

# def summarize_dialogue(dialogue :str)->str:
#     dialogue=clean_data(dialogue) #clean

#     #tokenize
#     inputs=tokenizer(
#         dialogue,
#         padding="max_length",
#         max_length=512,
#         truncation=True,
#         return_tensors="pt"
#     ).to(device)

#     #generate summary->token ids
#     model.to(device)
#     targets=model.generate(
#         input_ids=inputs["input_ids"],
#         attention_mask=inputs["attention_mask"],
#         max_length=150,
#         num_beams=4, # means model will gives us 4 different summary
#         early_stopping=True
#     )
#     #covert tokenids to convert to text 
#     summary=tokenizer.decode(targets[0],skip_special_tokens=True)
#     return summary
def summarize_dialogue(dialogue: str) -> str:

    print(">>> Cleaning text")
    dialogue = clean_data(dialogue)

    print(">>> Tokenizing")

    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=256,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    print(">>> Tokenization completed")
    print(">>> Device:", device)

    print(">>> Starting model generation")

    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=80,
        num_beams=1
    )

    print(">>> Generation completed")

    summary = tokenizer.decode(
        targets[0],
        skip_special_tokens=True
    )

    print(">>> Summary:", summary)

    return summary

#API endpoints
# @app.post("/summarize")
# async def summarize(dialogue_input: DialougeInput):
#     summary=summarize_dialogue(dialogue_input.dialouge)
#     return {"summary":summary}

@app.post("/summarize")
async def summarize(dialogue_input: DialougeInput):

    print(">>> /summarize request received")

    summary = summarize_dialogue(dialogue_input.dialouge)

    print(">>> Summary generated")

    return {"summary": summary}


@app.get("/",response_class=HTMLResponse)
async def create_item(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html"
)
