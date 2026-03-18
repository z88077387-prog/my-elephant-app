import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Page setup
st.set_page_config(page_title="Elephant Care App", layout="wide", page_icon="🐘")

st.title("🐘 အာရှဆင်များ ကာကွယ်စောင့်ရှောက်ရေး")

# Sidebar Menu
menu = st.sidebar.selectbox("သွားလိုရာရွေးချယ်ပါ", ["Home", "ဆင်စခန်းများ မြေပုံ", "လှူဒါန်းရန်", "ဆက်သွယ်ရန်"])

if menu == "Home":
    st.header("မင်္ဂလာပါ")
    st.image("https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?q=80&w=1000", caption="အာရှဆင်များ")
    st.write("ဆင်တွေကို ချစ်မြတ်နိုးပြီး ထိန်းသိမ်းစောင့်ရှောက်လိုတဲ့အတွက် ကျေးဇူးတင်ပါတယ်။")

elif menu == "ဆင်စခန်းများ မြေပုံ":
    st.header("📍 မြန်မာနိုင်ငံရှိ ဆင်စခန်းများ")
    m = folium.Map(location=[18.0, 96.5], zoom_start=7)
    # ဝင်းကန်ဆင်စခန်း
    folium.Marker([17.1524, 96.3429], popup="ဝင်းကန်ဆင်စခန်း", tooltip="ဝင်းကန်").add_to(m)
    # စိမ်းလဲ့တင်
    folium.Marker([17.3458, 96.6111], popup="စိမ်းလဲ့တင်ဆင်စခန်း", tooltip="စိမ်းလဲ့တင်").add_to(m)
    st_folium(m, width=700, height=500)

elif menu == "လှူဒါန်းရန်":
    st.header("🙏 အလှူငွေထည့်ဝင်ရန်")
    st.info("KPay / Wave: 09-xxxxxxxxx သို့ လှူဒါန်းနိုင်ပါသည်။")
    st.write("ဆင်စာနှင့် ဆေးဝါးများအတွက် အသုံးပြုသွားမည် ဖြစ်ပါသည်။")

elif menu == "ဆက်သွယ်ရန်":
    st.header("📞 ဆက်သွယ်ရန်")
    st.write("အသေးစိတ်သိရှိလိုပါက 09-xxxxxxxxx သို့ ဆက်သွယ်မေးမြန်းနိုင်ပါသည်။")
