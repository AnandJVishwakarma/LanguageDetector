import gradio as gr
import tqdm
from detector import detect_language_free

flag_demo = False
lang_map = {
    "hi":"Hindi",
    "en":"English",
    "de":"German",
    "fr":"French",
    "ja":"Japanese",
    "es":"Spanish",
    "ru":"Russian",
    "zh":"Chinese",
    "ko":"Korean",
    "it":"Italian",
}

import gradio as gr

def get_input(input_string, history=""):
    try:
        print("history: ", history)
        code = detect_language_free(input_string)
        return lang_map[code] + " language"
    except (Exception) as error:
        raise gr.Error(error,duration=3)

def clear_all():
    return "","",""
# demo = gr.Interface(fn=get_input, inputs="text", outputs="label")
# demo = gr.ChatInterface(fn=get_input, type="messages")

with gr.Blocks(
    title = "Language Detector",
    head="Language Detector"
) as demo:
    
    gr.Markdown(
    """
    # Language Detector by Anand Vishwakarma
    # [LanguageDetector @ GitHub](https://github.com/AnandJVishwakarma/LanguageDetector)
    """
    )
    inp = gr.Textbox(
        label="Input text here", 
        placeholder="Insert text in any language...",
    )
    out = gr.Label(label="Above text is in ")
    # inp.change(get_input, inp, out)
    with gr.Row():
        clearbtn = gr.ClearButton()
        detectbtn = gr.Button(value="Detect")

    clearbtn.click(clear_all, inputs=None, outputs=[inp, out])
    detectbtn.click(get_input, inputs=inp, outputs=out)
    

def setup_gui(share=False):
    if flag_demo:
        demo.launch(server_name="0.0.0.0", inbrowser=True)
    else:
        try:
            demo.launch(server_name="0.0.0.0", debug=True, inbrowser=True, share=share)
        except Exception:
            print(
                "Error launching GUI using 0.0.0.0.\nThis may be caused by global mode of proxy software."
            )
            try:
                demo.launch(
                    server_name="127.0.0.1", debug=True, inbrowser=True, share=share
                )
            except Exception:
                print(
                    "Error launching GUI using 127.0.0.1.\nThis may be caused by global mode of proxy software."
                )
                demo.launch(debug=True, inbrowser=True, share=True)

# For auto-reloading while developing
if __name__ == "__main__":
    setup_gui()