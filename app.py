import gradio as gr
import pickle as pkl
import numpy as np

with open('Model/model.pkl', 'rb') as file:
    model = pkl.load(file)

def predict(SC,PCV,SG,HB,Alb):
    data = np.array([[SC,PCV,SG,HB,Alb]])
    # Replace 'Yes' with 1 and 'No' with 0
    data[data == 'Yes'] = 1
    data[data == 'No'] = 0

# Convert the entire array to numeric values
    data = data.astype(float)

    print(data)
    prediction = model.predict(data)
    text=f'{prediction[0]*100}% chance of Chronic Kidney Disease!'
    return text

theme = gr.Theme.from_hub("freddyaboulton/dracula_revamped")




input=[gr.Slider(0, 500, value=0, label="Serum Creatinine Levels", info="Choose Serum Creatinine level in mg/dL (0-500)"),
       gr.Slider(0, 100, value=0, label="Packed Cell Volume", info="Choose Packed Cell Volume (0-100)"),
       gr.Slider(1.000, 1.040, value=0, label="Specific Gravity", info="Choose Specific Gravity of Urine (1.000-1.040)"),
       gr.Slider(0, 200, value=0, label="Hemoglobin Levels", info="Choose Hemoglobin level in g/dL (0-200)"),
       gr.Slider(0, 6, value=0, label="Albumin Levels", info="Choose Albumin level g/dL in Urine (0-6)")]

#create Gradio App
demo=gr.Interface(fn=predict,inputs=input,outputs="text",title="Chronic Kidney Disease Prediction Model",theme=theme)
demo.launch(debug=True,share=True) 