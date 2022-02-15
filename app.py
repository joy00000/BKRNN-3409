#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask
from flask import request, render_template
from keras.models import load_model


# In[6]:


app = Flask(__name__)


# In[7]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        NP = request.form.get("NP")
        TL = request.form.get("TL")
        WC = request.form.get("WC")
        print(NP, TL, WC)
        model = load_model("bankruptcy_nn")
        pred = model.predict([[float(NP), float(TL), float(WC)]])
        res = "Prediction: "+str(pred)
        return(render_template("index.html", result=res))
    else:
        return(render_template("index.html", result="2"))


# In[8]:


if __name__ == "__main__":
    app.run()


# In[ ]:




